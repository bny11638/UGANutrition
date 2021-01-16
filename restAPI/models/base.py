from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import sqlalchemy
from sqlalchemy.ext.declarative import DeclarativeMeta
import json


class AlchemyEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj.__class__, DeclarativeMeta):
            # an SQLAlchemy class
            fields = {}
            for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
                data = obj.__getattribute__(field)
                try:
                    json.dumps(data) # this will fail on non-encodable values, like other classes
                    fields[field] = data
                except TypeError:
                    fields[field] = None
            # a json-encodable dict
            return fields

        return json.JSONEncoder.default(self, obj)

#Creating an encoder object
encoder = AlchemyEncoder()

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

#creating engine
engine = sqlalchemy.create_engine(
            sqlalchemy.engine.url.URL(
                drivername=driver_name,
                host="35.224.143.155",
                username=db_user,
                password=db_password,
                database=db_name,
                query=query_string
            ),
            pool_size=5,
            max_overflow=2,
            pool_timeout=30,
            pool_recycle=1800
            )

Session = sessionmaker(bind=engine)
Base = declarative_base()

def object_as_dict(obj):
    return {c.key: getattr(obj, c.key)
            for c in sqlalchemy.inspect(obj).mapper.column_attrs}
