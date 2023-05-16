# Kubernetes Deployment of Application <!-- omit in toc -->

---

# Contents <!-- omit in toc -->

- [1. Project Structure](#1-project-structure)
- [2. Deploying application to Minikube](#2-deploying-application-to-minikube)
  - [2.1. Prerequisites](#21-prerequisites)
  - [2.2. Steps to Deploy on Minikube](#22-steps-to-deploy-on-minikube)
    - [Start the Minikube cluster](#start-the-minikube-cluster)
    - [Build images using Minikube docker env](#build-images-using-minikube-docker-env)
    - [Database Deployment](#database-deployment)
    - [Application Deployment](#application-deployment)

---

## 1. Project Structure

![Project Structure](./assets/structure.dio.svg)

## 2. Deploying application to Minikube

### 2.1. Prerequisites

- You must have Docker installed
- You must have the Kubernetes extension installed on the Docker desktop
- You must have the Minikube CLI installed
- You must have the KubeCTL CLI installed

<div style="background-color: #CCFFFF; padding:10px; border-radius:10px;font-size:0.8em; margin-bottom:10px">
  <span style="color: #5F9EA0">💡Note: </span>
  <span style="color: #666666">Minikube uses its own docker engine to run images, thus in order to run the local docker images we either have to upload them to docker hub or enable the Minikube docker engine</span>
</div>

### 2.2. Steps to Deploy on Minikube

#### Start the Minikube cluster

- Open the command prompt and run the command below to start the minikube cluster

```
minikube start
```

![minikube start output](./assets/command%20outputs/1.png)

- Now, run the command below to open the dashboard

```
minikube dashboard
```

#### Build images using Minikube docker env

- To enable the Minikube docker engine run the command below

```
minikube docker-env | Invoke-Expression
```

- Build the current projects docker image using

```
docker compose build
```

![Build Output](./assets/command%20outputs/3.png)

#### Database Deployment

- Now, apply the database secrets and persistent volumes using the command

```
kubectl apply -f ./db/secret.yaml
kubectl apply -f ./db/storage.yaml
```

![applying secret and persistent volumes](./assets/command%20outputs/2.png)

- Now, deploy the database using the command

```
kubectl apply -f ./db/deployment.yml
```

![DB Deployment](./assets/command%20outputs/4.png)

- Check the status of the deployment using the command

```
kubectl get pods
```

![Deployment Status](./assets/command%20outputs/5.png)

- Now, deploy the database service using the command and get the database local IP and Port

```
kubectl apply -f ./db/service.yaml
kubectl get service
```

![Service Deployment](./assets/command%20outputs/6.png)

- Now, copy the IP for the database service and put it in the application's config map

#### Application Deployment

- Now that the database is deployed, we can deploy the application

- Apply all the applications secrets, configMap, Deployment and Service as previously done for the database

```bash
kubectl apply -f ./app/nginx-conf.yml && \
kubectl apply -f ./app/secret.yml && \
kubectl apply -f ./app/configmap.yml && \
kubectl apply -f ./app/deployment.yml && \
kubectl apply -f ./app/service.yml
```

- Now we will open a terminal inside the django container, to do this run the command

```
kubectl get pods
kubectl exec -it <pod-name> -- /bin/bash
```

![App Deployment](./assets/command%20outputs/7.png)

- Done !