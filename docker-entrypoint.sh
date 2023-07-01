#!/bin/bash

# Wait for the database to be ready
echo "Waiting for database connection..."
while ! nc -z $DATABASE_HOST $DATABASE_PORT; do
    sleep 0.1
done
echo "Database connection established"

# Apply database migrations
echo "Applying database migrations..."
python manage.py migrate --noinput

# Generate fake data
echo "Generating fake data..."
python manage.py generate_fake_data

rm -rf static
# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Start Gunicorn server
echo "Starting Gunicorn server..."
gunicorn project.wsgi:application \
    --bind 0.0.0.0:$PORT \
    --workers $GUNICORN_WORKERS \
    --log-level=info \
    --access-logfile=-