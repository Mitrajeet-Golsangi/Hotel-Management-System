#!/bin/bash
APP_PORT=${PORT:-8000}
cd /app/

# Compile all the tailwindcss files
npx tailwindcss -i ./static/css/styles.css -o ./static/dist/output.css

# Run the migrations
chmod +x /app/migrate.sh && /app/migrate.sh

# Collect the static files
python3 manage.py collectstatic --noinput

# Start the production server
/opt/venv/bin/gunicorn --worker-tmp-dir /dev/shm hotel_management_system.wsgi:application --bind "0.0.0.0:${APP_PORT}"