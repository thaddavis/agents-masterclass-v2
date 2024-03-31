# Overview

So now let's quickly ship this to validate how fire this set up is...

## Requirements

google-cloud-sdk - https://cloud.google.com/sdk/docs/install (seems to work best with Python 3.11)
k8s - https://kubernetes.io/docs/tasks/tools/install-kubectl-macos/#install-with-homebrew-on-macos

GCP Services used

- GKE
- Artifact Registry
- Cloud Build

## step 1

Created a project called `Agents`

## step 2

Add Credit Card and enable the following API's in the GCP account

- Artifact Registry API
- Cloud Build API
- Kubernetes Engine API

## step 3

Install the `gcloud` CLI

- https://cloud.google.com/sdk/docs/install
- verify install with `gcloud -v`
- `gcloud init` - configure your CLI

## step 4

Install k8s

- brew install kubectl
- verify install with `kubectl version --client`

## step 5 

Create test project

- mkdir helloworld-gke
- create `helloworld-gke` project

## step 6

- gcloud config get-value project
- gcloud artifacts repositories create hello-repo \
    --project=PROJECT_ID \
    --repository-format=docker \
    --location=us-central1 \
    --description="Docker repository"
- ie: gcloud artifacts repositories create hello-repo \
    --project=agents-418900 \
    --repository-format=docker \
    --location=us-central1 \
    --description="Docker repository"

- https://console.cloud.google.com/artifacts?referrer=search&project=agents-418900

## step 7

- gcloud config get-value project
- gcloud builds submit \
  --tag us-central1-docker.pkg.dev/PROJECT_ID/hello-repo/helloworld-gke .
- gcloud builds submit \
  --tag us-central1-docker.pkg.dev/agents-418900/hello-repo/helloworld-gke .

## step 8

Create a GKE cluster

- gcloud container clusters create-auto helloworld-gke \
--location us-east1

TIP: Will take about 10 minutes

## step 9

- Reinstalled `google-cloud-sdk`
- Using Python 3.11.x on my machine *IMPORTANT*

CRITICAL: ACTION REQUIRED: gke-gcloud-auth-plugin, which is needed for continued use of kubectl, was not found or is not executable. Install gke-gcloud-auth-plugin for use with kubectl by following https://cloud.google.com/blog/products/containers-kubernetes/kubectl-auth-changes-in-gke

- gcloud components install gke-gcloud-auth-plugin

## step 10

Deploy k8s components

- gcloud config get-value project
- kubectl config view
- kubectl config current-context
- kubectl apply -f k8s/deployment.yaml
- kubectl get deployments
- kubectl get pods
- kubectl apply -f k8s/service.yaml
- kubectl get services
- curl 34.139.47.140

It works! 🎉


## DEBUGGING

- kubectl config get-contexts
- kubectl get context gke_agents-418900_us-east1_helloworld-gke
- gcloud components install gke-gcloud-auth-plugin

## FINALLY

- gcloud compute addresses create helloworld-ip --global
- gcloud compute addresses describe helloworld-ip --global
- kubectl delete -f k8s/deployment.yaml

- kubectl apply -f k8s/deployment.yaml
- kubectl apply -f k8s/ingress.yaml