#!/bin/sh
export FLASK_APP=./restAPI/index.py
export FLASK_DEBUG=1
source venv/Scripts/activate.bat
flask run -h 0.0.0.0