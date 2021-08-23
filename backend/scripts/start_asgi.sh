#!/usr/bin/env bash

set -o errexit
set -o pipefail
set -o nounset
set -o xtrace

python manage.py migrate
python manage.py collectstatic --noinput --verbosity 0
daphne -b 0.0.0.0 -p 8001 backend.asgi:application
# gunicorn backend.asgi:application -k uvicorn.workers.UvicornWorker --reload --port 8001