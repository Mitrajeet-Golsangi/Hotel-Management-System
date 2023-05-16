#!/bin/bash
echo "*************************************** Performing Migrations ***************************************"

# Create the required variables for the values of the create superuser command
DJANGO_SUPERUSER_EMAIL=${DJANGO_SUPERUSER_EMAIL:-"mitrajeetgolsangi@gmail.com"}
DJANGO_SUPERUSER_USERNAME=${DJANGO_SUPERUSER_USERNAME:-"mitrajeet"}

cd /app/

# Perform model migrations to database
/opt/venv/bin/python manage.py migrate --noinput

# || true => makes sure it will not fail even after running multiple times
/opt/venv/bin/python manage.py createsuperuser --email=${DJANGO_SUPERUSER_EMAIL} --username=${DJANGO_SUPERUSER_USERNAME} --noinput || true