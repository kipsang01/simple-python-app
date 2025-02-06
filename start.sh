#!/bin/bash

docker pull $DOCKERHUB_USERNAME/customer-service:latest

docker stop customer-service || true
docker rm customer-service || true

docker run --rm \
  --env-file .env \
  $DOCKERHUB_USERNAME/customer-service:latest \
  python manage.py migrate

docker run -d \
  --name customer-service \
  -p 8000:8000 \
  --env-file .env \
  $DOCKERHUB_USERNAME/customer-service:latest \
  gunicorn core.wsgi:application --bind 0.0.0.0:8000