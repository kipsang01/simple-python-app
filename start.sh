#!/bin/bash
set -e

docker pull $DOCKERHUB_USERNAME/customer-service:latest

docker stop customer-service || true
docker rm customer-service || true

echo "Running migrations..."
docker run --rm \
  --env-file .env \
  $DOCKERHUB_USERNAME/customer-service:latest \
  python manage.py migrate

echo "Starting Application..."
docker run -d \
  --name customer-service \
  -p 8000:8000 \
  --restart unless-stopped \
  --env-file .env \
  $DOCKERHUB_USERNAME/customer-service:latest \
  gunicorn core.wsgi:application --bind 0.0.0.0:8000 --workers 3 --timeout 120

echo "Deployment completed successfully"