IMAGE=flask-application2
VERSION=0.2
docker rmi $IMAGE:$VERSION
docker build -t $IMAGE:$VERSION .
docker rmi $IMAGE:latest
docker tag $IMAGE:$VERSION $IMAGE:latest

