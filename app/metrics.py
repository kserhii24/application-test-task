"""File with async function and decorator for prometheus metrics"""

import asyncio
import socket
from functools import wraps
from prometheus_client import Gauge, Counter

hostname = socket.gethostname()
prometheus_request_count = Gauge('request_count', 'Total request count', ['hostname', 'endpoint'])
prometheus_response_time = Gauge('response_time', 'Response time in milliseconds', ['hostname', 'endpoint'])
prometheus_status_code_count = Counter('positive_response_count', 'Count of positive response codes', ['hostname', 'endpoint', 'status_code'])

def record_metrics(endpoint, hostname=hostname):
    def decorator(metric_func):
        @wraps(metric_func)
        async def wrapped_function(*args, **kwargs):
            start_time = asyncio.get_event_loop().time()
            prometheus_request_count.labels(hostname=hostname, endpoint=endpoint).inc()
            result = await metric_func(*args, **kwargs)
            status_code = getattr(result, 'status_code', None)
            if not status_code and isinstance(result, tuple) and len(result) > 1:
                status_code = result[1]
            prometheus_status_code_count.labels(hostname=hostname, endpoint=endpoint, status_code=status_code).inc()
            elapsed_time_ms = (asyncio.get_event_loop().time() - start_time) * 1000 # in ms 
            prometheus_response_time.labels(hostname=hostname, endpoint=endpoint).set(elapsed_time_ms)
            return result
        return wrapped_function
    return decorator
