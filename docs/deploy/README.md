# Deploy manual
**This manual is intended to be used with Minikube**

## Pre-requirements: 
  - Docker (or any other virtualization service for running minikube)
  - [Minikube](https://minikube.sigs.k8s.io/docs/start/)
  - Enabled Igress addon for minikube: 
  ```
  minikube addons enable ingress
  ```

## Deployment
The [deployment file](../../deploy/application.yaml) is consist of 4 kubernetes entities: 
- Deployment
- Service
- Pod Disruption Budget
- Ingress

## Deploy command: 
**Asuming, that you are in a root folder of the repository:**
```
kubectl apply -f deploy/application.yaml
```

## To have an access to the ingress we need to run: 
```
minikube tunnel
```

## For any other explanations and conclusions please refer to [Conclusion](../report/README.md)