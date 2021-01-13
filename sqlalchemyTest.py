import sqlalchemy
import json

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

db = sqlalchemy.create_engine(
            sqlalchemy.engine.url.URL(
                drivername=driver_name,
                host="35.224.143.155",
                username=db_user,
                password=db_password,
                database=db_name,
            ),
            pool_size=5,
            max_overflow=2,
            pool_timeout=30,
            pool_recycle=1800
            )

name = input()
password = input()
stmt = sqlalchemy.text("SELECT * FROM user_data where username =\'" + name + "\' AND password=\'" + password + "\';")
with db.connect() as conn:
    query = conn.execute(stmt)
    tmp = query.fetchone()
if tmp is None:
    print( "False")
else:
    tmp = tmp.items()
    tmp = tuple(tmp)
    if type(tmp) is tuple:
        print("SUCCESS")
        print(tmp)