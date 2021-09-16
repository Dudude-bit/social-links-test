#!/bin/bash
if [[ "${DEBUG:-true}" == "true" ]]; then
  python3 app.py
else
  gunicorn --bind 0.0.0.0:5000 app:app
fi