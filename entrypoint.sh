#!/bin/bash

# Apply database migrations
python manage.py migrate --no-input

# Check if genbooks needs to be run (e.g., by checking the existence of a specific table or record)
if python manage.py showmigrations | grep -q '\[ \] genbooks'; then
  echo "Running genbooks command..."
  python manage.py genbooks
else
  echo "genbooks command already run, skipping..."
fi

# Collect static files
python manage.py collectstatic --no-input

# Start the Gunicorn server with reload option
exec gunicorn django_project.wsgi:application --bind 0.0.0.0:8000 --reload