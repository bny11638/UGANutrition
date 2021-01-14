#!/bin/sh
export FLASK_APP=./app/index.py
source venv/Scripts/activate.bat
flask run -h 0.0.0.0