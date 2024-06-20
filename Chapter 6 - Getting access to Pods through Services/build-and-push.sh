#!/bin/bash

docker build -t flask-app:$1 .

docker tag flask-app:$1 cosminionita/flask-app:$1

docker push cosminionita/flask-app:$1
