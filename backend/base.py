from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db_string = 'postgresql://postgres:San611909@localhost/flaskPractice'

#engine is created to talk to database and passed to a session to work with ORM(sqlAlchemy)
engine = create_engine(db_string)  
Session = sessionmaker(bind=engine)

#session controls all objects (objects for tables created for orm) which consists of
# the connection with db, queries, managing stored changes in memory and push to db  etc
session = Session()

#Construct a base class for declarative class definitions.
# also callss appropriate mapper() based on subclasses of the base. Think of virtual base class functions in oop 
Base = declarative_base()

