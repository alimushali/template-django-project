#!/bin/bash
/opt/app/venv/bin/gunicorn -w 4 -b 0.0.0.0:8000 --env DJANGO_SETTINGS_MODULE=core.settings core.wsgi