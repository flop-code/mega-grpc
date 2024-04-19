#!/bin/bash

python3 -m alembic upgrade head || exit 1

cd source || exit 1
gunicorn rest.main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind="0.0.0.0:$APP_PORT" \
  & python3 -m rpc.main
