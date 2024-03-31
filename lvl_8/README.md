# Overview

Let's quickly ship this to validate this set up is good for shipping...

## Requirements

google-cloud-sdk aka gcloud - https://cloud.google.com/sdk/docs/install (seems to work best with Python 3.11)
    - I installed to ~/Library/google-cloud-sdk
    - check $PATH
    - gcloud --version

GCP Services used

- Cloud Run
- Artifact Registry
- Cloud Build

# CREATE A CLOUDRUN SERVICE

- gcloud builds submit --config=cloudbuild.yaml .
- gcloud run services replace service.yaml --region us-east1
- gcloud run services set-iam-policy agents-api policy.yaml
    - Replace existing policy (Y/n)? Y

## Reference links

- https://cloud.google.com/run/docs/deploying#yaml
- https://cloud.google.com/run/docs/authenticating/public
- https://cloud.google.com/run/docs/authenticating/public#yaml