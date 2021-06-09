from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

USER = os.getenv('DBUSER')
PASSWORD = os.getenv('DBPASS')
HOST = os.getenv('DBHOST')
PORT = os.getenv('DBPORT')
DBNAME = os.getenv('DBNAME')

engine = create_engine('postgresql://{0}:{1}@{2}:{3}/{4}'.format(USER, PASSWORD, HOST, PORT, DBNAME))
Session = sessionmaker(bind=engine)
Base = declarative_base()
