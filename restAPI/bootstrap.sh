#!/bin/sh
source .venv/bin/activate
pip3 install -r requirements.txt 
export FLASK_APP=./main.py
flask run -h 0.0.0.0