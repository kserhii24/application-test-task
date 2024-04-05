# Conclusions and explanations

## Explanations
### Python3 application: 
- I created a simple Python3 repository structure and split all functions across different files. 
- I decided to use Quart instead of Flask because Quart is more suitable for async. So, because of that, I needed to ASGI server instead of WSGI for production needs (Hypercorn)
- To expose metrics, I decided to use Prometheus client, it's a special package to expose Prometheus readable metrics. I expose: the last response time, amount of responses (per response code), and total requests. 
- **I decided not to use an async function for Fibonacci calculation, because Fibonacci calculation is a CPU-bound task and according to Pyhton GIL it makes no sense. I tried to use "process pools", but didn't get any significant performance increase, so I decided to leave the function as is and optimize**


### Build
- For the build, I use a regular multistage dockerfile, despite, using a multistage being much more valuable when we use a compiled programming language, I decided to use it to rid of any caches after the pip3 modules installation. 
- To improve security and create a lightweight env for our application, I used Python3-venv
- Improved security by running applications under non-root user

### Deploy
#### For application deployment I decided to use a minikube with YAML file for deployment: 
- I used our custom endpoints for [readinessProbe](../../deploy/behavox.yaml#L37) and [livenessProbe](../../deploy/behavox.yaml#L43)
- Set a default amount of [replicas in the deployment to 3](../../deploy/behavox.yaml#L9)
- Ensured a load balancing by creatig a [service](../../deploy/behavox.yaml#L51) and point it to our deployment
- Ensured a zero-downtime update by configuring a [RollingUpdate](../../deploy/behavox.yaml#L14) deployment strategy with 0 maxUnavailable replicas during deployment process. Also created a [PDB](../../deploy/behavox.yaml#L64) to make sure, that we will not have any downtime in case of rebalancing worker nodes in the cluster. 
- Created an [Ingress](../../deploy/behavox.yaml#L74) to have normal access through port 80 to our application
- I used a newly built [image](../../deploy/behavox.yaml#L25) for our deployment. It's available on [DockerHub](https://hub.docker.com/layers/sergey2410/behavox/latest/images/sha256-e889668a4886492ebdfe7ade113a9c7098862933ad09f6cac08dcc998ab9cf4d?context=repo)

### Script
- I created a [script](../../scripts/send_requsts.py) to send 100 requests using Python3 aiohttp to our application

## Conclusions
### After running a script and reviewing [metrics](./METRICS.md) (I provided metrics in a text format, but it's better to have prometheus/vmagent in the cluster and scrape metrics to the prometheus/VM) we ensured: 
- All our locations work: health, ready, payload, metrics
- We calculated a fibonacci sequence fast enough (no more, than 1ms)
- Our load-balancing logic works well, all 100 requests were split across all 3 pods in our deployment
- Based on all information, we got a small, simple, but robust application
### There are a lot of ways to improve our application: 
- Add HPA for our application to scale it. As far as we have a stateless application, it would not be a complicated task
- Probably it could be a good idea to add a cache, for caching results to optimize our application

### Logging and monitoring proposals:
#### Monitoring: 
- As I mentioned before, I already used a prometheus client in our application. So, it's 100% suitable for Prometheus-like applications to scrape application metrics. 
- To monitor hardware metrics, I would use kube-state-metrics and also collect it with prometheus-like tool. 
- To display metrics, I would use grafana
- Based on all proposed bullet point's I would say, that it's enough information to track application performance: CPU and RAM consumption, error rates and responce times. 
- Also, I added a hostname to our metrics to have the possibility to track from which pod we got metrics

#### Logging:
- All of our hypercorn logs are going to the [stdout of the container](../../Dockerfile#L30). I think the best and simplest way to collect all of the logs - use Loki and, for example, promtail/fluent bit. We could deploy log collectors like sidecar in out pod or like a daemonset (in case we don't use serverless resources), collect logs and send them to Loki. After that, we could display it in Grafana. 