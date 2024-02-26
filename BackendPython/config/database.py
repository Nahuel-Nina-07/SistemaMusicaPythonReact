from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv
import os

load_dotenv()

DB_NAME=os.getenv('DB_NAME')
DB_HOST=os.getenv('DB_HOST')
DB_PASSWORD=os.getenv('DB_PASSWORD')
DB_DIALECT=os.getenv('DB_DIALECT')
DB_USER=os.getenv('DB_USER')

URL_DATABASE = '{}://{}:{}@{}/{}'.format(DB_DIALECT, DB_USER, DB_PASSWORD, DB_HOST, DB_NAME)

engine = create_engine(URL_DATABASE)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()