# Second Pod (Multi-Container) & Ingress

## Build a pod and deploy as ReplicaSet

~~~
$ cat cloudbuild.yaml
$ gcloud builds submit --config cloudbuild.yaml

$ cat flask-application-repl2.yaml
$ kubectl create -f flask-application-repl2.yaml
~~~

## Ingress

~~~
$ cat flask-application-svc2.yaml
$ kubectl create -f flask-application-svc2.yaml

$ cat flask-application-ingress2.yaml
$ kubectl create -f flask-application-ingress2.yaml

$ kubectl get ingress
~~~

  * Hit http://<ingress ip>/hello
