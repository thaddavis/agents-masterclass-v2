
# CREATE A CLOUDRUN SERVICE

- gcloud builds submit --config=cloudbuild.yaml .
- gcloud run services replace service.yaml --region us-east1
- gcloud run services set-iam-policy agents-api policy.yaml
    - Replace existing policy (Y/n)? Y

## Reference links

- https://cloud.google.com/run/docs/deploying#yaml
- https://cloud.google.com/run/docs/authenticating/public
- https://cloud.google.com/run/docs/authenticating/public#yaml