#!/bin/sh
set -x

python3 ./setupdb.py

export FLASK_APP=./api.py
flask run -h 0.0.0.0
