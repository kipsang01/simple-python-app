#!/bin/bash

python manage.py migrate

gunicorn shop.wsgi:application --bind 0.0.0.0:8000 --workers 3 --timeout 120

