### A scalable polling web app built on Django frameowork (admin backend to manage polls), Python & PostgreSQL.



Overview
======
- A scalable polling web app built on Django frameowork (admin backend to manage polls), Python & PostgreSQL.
- Static content stored on Google Cloud  Storage Bucket
- Docker container image: gcr.io
- Auto deployed on Google Cloud Platform with Dockerfile (Kuberenetes Engine). 

**NOTES**
> Gcp Connected (Cloudbuild.Yaml Not Active)**

#### Prerequisites:
> Python 3.7
> Django-Admin 2.2.6
> PostgreSQL 11
>  **For Local Development ** : Download Google SQL Cloud Proxy
>> Setup Google Cloud SQL Instance
>> Create GCP Service Account (secret + key.json)

#####  Google Cloud SQL Instance Config :
>  DATABASE VERSION IS POSTGRESQL 11
>  AUTO STORAGE INCREASE IS DISABLED
> AUTOMATED BACKUPS ARE DISABLED
> NOT HIGHLY AVAILABLE (ZONAL)

### `pip install -t requirements`


--------------------------------------------------------------------------------


## CONFIG

1. MODIFY: settings.py (SECRET_KEY,DATABASES,STATIC_URL,ETC.)
2. MODIFY: polls.yaml
3. CREATE/CONFIG: virtualenv
    - EXPORT variables
4. START cloud_sql_proxy + runserver
5. Django migrations
6. CREATE Superuser

## CLOUD STORAGE BUCKET 
1. CREATE Bucket
2. Enable public access on Google IAM Policy for AllUsers (NOT ACL)
3. RUN COLLECTSTATIC 
3. RSYNC: `gsutil rsync -R static/ gs://[GCloud_Storage_Bucket]/static`


## KUBERNETES ENGINE CLUSTER INIT

1. CREATE: container cluster (gcloud)  
2. CONFIRM: `gcloud container clusters get-credentials ##CHANGE_ME## --zone "us-central1-a"`

## CLOUD SQL INIT
1. kubectl: create OAuth secrets from key.json
2. Get docker image from Cloud SQL Proxy  (docker pull/build)
3. CONFIG: gcloud as auth-helper for docker (`gcloud auth configure-docker`)
    - Authenticat service account for write access into cloud storage: `gcloud auth activate-service-account`
4. `docker push gcr.io/#projectid#/#appname#`
5. CREATE GKE resource: kubectl create -f polls.yaml

## KUBERNETES ENGINE DEPLOYMENT
1. RUN `kubectl get #`
    - 3 PODS ON CLUSTER
2. WAIT (Pod Status = Running)

# RESOURCES & TROUBLESHOTTING
- `kubectl get services ###`

####  **kubectl=cluster interaction tool**
- `kubectl log pod_id`
- `kubectl cluster-info`
- `kubectl describe pod_id`
- `kubectl describe --namespace default`
- `kubectl describe deployment #`
- `kubectl describe node #`

####  **PostgreSQL/GCLOUD CONNECT**
- `gcloud sql connect myinstance --user=postgres`
-  userlist:`gcloud sql users list --instance=#`
-  adduser:`gcloud sql users create [USER_NAME] --instance=# --password=#`
-  `mysql --host=ip --user=root --password`
-  `mysql --ssl-ca=server-ca.pem --ssl-cert=client-cert.pem --ssl-key=client-key.pem --host=[ip] --user=root --password`
- 

-----------------------------

## OTHER INFO

0.0.1
=========

[Django](https://www.djangoproject.com/) 
[GKE](https://cloud.google.com/python/django/kubernetes-engine)
[Internationalization](https://docs.djangoproject.com/en/1.8/topics/i18n/)

*NOTE: DJANGO IS A REGISTERED TRADEMARK OF THE DJANGO SOFTWARE FOUNDATION.
*******
