from flask import escape
import sqlalchemy

# Uncomment and set the following variables depending on your specific instance and database:
connection_name = "precise-truck-301217:us-central1:nutrition-uga"
#table_name = ""
#table_field = ""
#table_field_value = ""
db_name = "nutrition_app"
db_user = "guest"
db_password = "password"

# If your database is MySQL, uncomment the following two lines:
driver_name = 'mysql+pymysql'
query_string = dict({"unix_socket": "/cloudsql/{}".format(connection_name)})

# If your database is PostgreSQL, uncomment the following two lines:
#driver_name = 'postgres+pg8000'
#query_string =  dict({"unix_sock": "/cloudsql/{}/.s.PGSQL.5432".format(connection_name)})

# If the type of your table_field value is a string, surround it with double quotes.

def hello_http(request):
    request_json = request.get_json()
    request_args = request.args
    if request_json and 'name' in request_json:
        name = request_json['name']
    elif request_args and 'name' in request_args:
        name = request_args['name']
    else:
        name = 'World'
    return 'It worked ! Hello {}!'.format(escape(name))

def insert_test(request):
    request_json = request.get_json()
    request_args = request.args
    if request_json and 'name' and 'password' in request_json:
        name = request_json['name']
        password = request_json['password']
    elif request_args and 'name' in request_args:
        name = request_args['name']
    else:
        name = 'World'
    return 'It worked ! Hello{} your password is {}!'.format(name,password)
