#!/bin/sh
set -e
mkdir -p ./static
pipenv run python ./manage.py collectstatic --noinput
pipenv run python ./manage.py migrate --noinput
pipenv run gunicorn --bind=0.0.0.0:8000 --max-requests=1200 --timeout=60 api.wsgi --log-file -
