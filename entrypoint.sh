#!/bin/bash

python manage.py makemigrations pages accounts
# Apply database migrations
python manage.py migrate --no-input

# Check if genbooks needs to be run (e.g., by checking the existence of a specific table or record)
python manage.py genbooks
# Collect static files
python manage.py collectstatic --no-input

# Start the Gunicorn server with reload option
gunicorn django_project.wsgi:application --bind 0.0.0.0:8000 --reload