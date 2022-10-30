from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker#
from .config import settings
#RAW SQL
#import time
#import psycopg2
#from psycopg2.extras import RealDictCursor

# ORM 

#SQLALCHEMY_DATABASE_URL = "postgresql://<username>:<password>@<ip-adress/localhoste>/<database_name>"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"
#Before Config File
#SQLALCHEMY_DATABASE_URL = "postgresql://postgres:Ducati_999@localhost/fastapi"
SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}"

#engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
        
        
        
        
#Raw SQL      
#while True:
#    try:
#        conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres', 
#                                password='Ducati_999', cursor_factory = RealDictCursor)
#        cursor = conn.cursor()
#        print("Database connection was succesfull!")
#        break
#    except Exception as e:
#        print("Connection to database failed")
#        print(f"Error: ", e) 
#        time.sleep(2)