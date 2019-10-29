# Getting started with Django on Google Container Engine

Python 3.7
Django-Admin 2.2.6
PostgreSQL 11

Prerequisites:
-------------------------
1. CREATE: SQL Instance 
    --Database version is PostgreSQL 11
    --Auto storage increase is disabled
    --Automated backups are disabled
    --Not highly available (zonal)
2. CREATE: Service Account (secret + key.json)
3. DOWNLOAD INSTALL: SQL Cloud Proxy

1.CONFIG
------------------
1. MODIFY: settings.py (SECRET_KEY,DATABASES,STATIC_URL,ETC.)
2. MODIFY: polls.yaml
3. CREATE/CONFIG: virtualenv
    - EXPORT variables
4. START cloud_sql_proxy + runserver
5. Django migrations
6. CREATE Superuser

2.CLOUD STORAGE BUCKET 
----------------------
1. CREATE Bucket
2. Enable public access on Google IAM Policy for AllUsers (NOT ACL)
3. RUN COLLECTSTATIC 
3. RSYNC: `gsutil rsync -R static/ gs://[GCloud_Storage_Bucket]/static`


3.KUBERNETES ENGINE CLUSTER INIT
-----------------------
1. CREATE: container cluster (gcloud)  
2. CONFIRM: `gcloud container clusters get-credentials ##CHANGE_ME## --zone "us-central1-a"`

4.CLOUD SQL INIT
------------------------
1. kubectl: create OAuth secrets from key.json
2. Get docker image from Cloud SQL Proxy  (docker pull/build)
3. CONFIG: gcloud as auth-helper for docker (`gcloud auth configure-docker`)
    - Authenticat service account for write access into cloud storage: `gcloud auth activate-service-account`
4. `docker push gcr.io/#projectid#/shivanswebpolls`
5. CREATE GKE resource: kubectl create -f polls.yaml

5.KUBERNETES ENGINE DEPLOYMENT
-----------------------------
1. RUN `kubectl get #`
    - 3 PODS ON CLUSTER
2. WAIT (Pod Status = Running)

================
`kubectl get services ###`
===============

TROUBLESHOOTING 
-------------------------
- kubectl=cluster interaction tool
- `kubectl log pod_id`
- `kubectl cluster-info`
- `kubectl describe pod_id`
- `kubectl describe --namespace default`
- `kubectl describe deployment #`
- `kubectl describe node #`


RELATED DOCS/LINKS
-----------------------------
[Django](https://www.djangoproject.com/) 
[GKE] https://cloud.google.com/python/django/kubernetes-engine
[Internationalization] https://docs.djangoproject.com/en/1.8/topics/i18n/

