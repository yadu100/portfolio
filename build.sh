#!/usr/bin/env bash
set -o errexit
python -m pip install --upgrade pip
pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py makemigrations
python manage.py migrate

# Create admin user automatically. '|| true' prevents the build from failing on future deploys when the user already exists.
python manage.py createsuperuser --noinput --username admin --email ykbs100@gmail.com || true