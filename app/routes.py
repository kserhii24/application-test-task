"""Python3 file with application routes"""

import random
from quart import jsonify, Response
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST
from .metrics import record_metrics
from . import app
from .fibonacci import generate_fibonacci

@app.route('/metrics')
@record_metrics(endpoint='/metrics')
async def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

@app.route('/health')
@record_metrics(endpoint='/health')
async def health():
    # Potential place to check DB connection and other services
    return 'OK', 200

@app.route('/ready')
@record_metrics(endpoint='/ready')
async def ready():
    # Potential place to have an initial checks 
    return 'Service is ready', 200

@app.route('/payload')
@record_metrics(endpoint='/payload')
async def payload():
    random_number = random.randint(0, 30)
    fibonacci_result = generate_fibonacci(random_number)
    return jsonify({'fibonacci': fibonacci_result})
