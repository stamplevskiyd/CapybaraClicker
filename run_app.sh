#!/usr/bin/env bash

# Upgrade db
echo "Applying db migrations"
poetry run python -m flask db upgrade
echo "Migrations applied!"

# Run flask
echo "Starting flask app"
poetry run python -m flask run --port=8090 --with-threads --reload --debugger --host=0.0.0.0
