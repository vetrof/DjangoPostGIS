#!/bin/sh

python manage.py migrate
python manage.py runserver 0.0.0.0:8000
#gunicorn project.wsgi:application --bind 0.0.0.0:8000 --workers=$GUNICORN_WORKERS --threads=$GUNICORN_THREADS --reload
#daphne project.asgi:application -b 0.0.0.0 -p 8000

exec "$@"