from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#creating engine
engine = sqlalchemy.create_engine(
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

Session = sessionmaker(bind=engine)
Base = declarative_base()
