#!/bin/sh
export FLASK_APP=./rest/main.py
source ../venv/Scripts/activate.bat
flask run -h 0.0.0.0