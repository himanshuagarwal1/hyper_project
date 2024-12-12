#!/bin/sh

# Wait for PostgreSQL
echo "Waiting for PostgreSQL to be ready..."
while ! nc -z db 5432; do
  sleep 10
done
echo "PostgreSQL started"

# Run Django commands
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --noinput


exec "$@"
