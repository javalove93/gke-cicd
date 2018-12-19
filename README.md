# gke-cicd

## Container Registry login

~~~
  gcloud auth configure-docker
~~~

## Docker Build

~~~
  cat hello.py
  cat Docker file
  ./build.sh
~~~

## Docker Test

~~~
  docker run -p 5000:5000 flask-application:latest 
  or
  docker run -d --name=flask-application -p 5000:5000 flask-application:latest
~~~

  * Hit http://localhost:5000 with Browser

~~~
  docker stop flask-application
  docker rm flask-application
~~~

## Cloud Build

~~~
  gcloud builds submit --tag gcr.io/<project-id>/flask-application .
~~~

or

~~~
  $ cat cloudbuild.yaml
  steps:
  - name: 'gcr.io/cloud-builders/docker'
    args: [ 'build', '-t', 'gcr.io/$PROJECT_ID/flask-application', '.' ]
  images:
  - 'gcr.io/$PROJECT_ID/flask-application'

  $ gcloud builds submit --config cloudbuild.yaml
~~~

