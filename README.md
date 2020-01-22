# Chewtacca

The code behind www.wookietranslator.com

### Run locally

⬇️ [Install Google Cloud SDK](https://cloud.google.com/appengine/docs/standard/python/download)

```
 $ git clone git@github.com:kevando/chewy.git
 $ cd chewy
 $ dev_appserver app.yaml
```

### Deployment commands

```
 # Smoke test first
 $ gcloud app deploy --project chewtacca -v 12-boilerplate --no-promote
    
 # Deploy with a new cron job
 $ gcloud app deploy cron.yaml --project chewtacca -v 12-boilerplate
    
 # Sometimes datastore acts up and neeeds to be re-indexed
 $ gcloud datastore create-indexes index.yaml --project chewtacca
    
 # Map custom domain
 $ gcloud beta app domain-mappings --project chewtacca create wookietranslator.com
