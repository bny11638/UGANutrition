from flask import escape
import localPackage.mysql.connector

conn = localPackage.mysql.connector.connect (
        host="35.224.143.155",
        user="guest",
        password="password",
        database="nutrition_app",
)

def insert(request):
    request_json = request.get_json()
    if request_json and 'name' and 'password' in request_json:
        name = request_json['name']
        password = request_json['password']
    return 'Hello {}! Your Password is {}'.format(escape(name,password))

def hello_http(request):
    request_json = request.get_json(silent=True)
    request_args = request.args
    if request_json and 'name' in request_json:
        name = request_json['name']
    elif request_args and 'name' in request_args:
        name = request_args['name']
    else:
        name = 'World'
    return 'Hello {}!'.format(escape(name))

def show_user(request):
    request_json = request.get_json(silent=True)
    request_args = request.args
    if request_json and 'name' in request_json:
        name = request_json['name']
    elif request_args and 'name' in request_args:
        name = request_args['name']
    else:
        name = 'World'
    return 'Hello {}!'.format(escape(name))