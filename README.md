# gke-cicd
Google Cloud Kubernetes CI/CD example based on Cloud Build (and Spinnaker - still working on)

## Container Registry login

~~~
  gcloud auth configure-docker
~~~

## Docker Build

~~~
  $ ./build.sh
~~~

## Docker Test

~~~
  $ docker run -p 5000:5000 flask-application:latest 
  or
  $ docker run -d --name=flask-application -p 5000:5000 flask-application:latest
~~~

  * Hit http://localhost:5000 with Browser

~~~
  $ docker stop flask-application
  $ docker rm flask-application
~~~

## Cloud Build

~~~
  $ gcloud builds submit --tag gcr.io/<project-id>/flask-application .
~~~

or

~~~
  $ cat cloudbuild.yaml
  $ gcloud builds submit --config cloudbuild.yaml
~~~

Then, you can see new version of build at Cloud Build(Google Console)

---
# Kubernetes

## Pod

~~~
$ cat flask-application-pod.yaml
$ kubectl create -f flask-application.yaml
~~~

## Service

~~~
$ cat flask-application-svc.yaml
$ kubectl create -f flask-application-svc.yaml
~~~

## All-in-one YAML (Pod + Service)

~~~
$ cat flask-all.yaml
$ kubectl create -f cat flask-all.yaml
~~~

## Deployment or ReplicaSet

~~~
$ cat flask-application-deploy.yaml
$ kubectl create -f flask-application-deploy.yaml

or

$ cat flask-application-repl.yaml
$ kubectl create -f flask-application-repl.yaml
~~~






