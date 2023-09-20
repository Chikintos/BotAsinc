from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Import the DATABASE_URL from config
from config import DATABASE_URL

# Create a base class for declarative models
Base = declarative_base()

# Create an engine for the database using the provided DATABASE_URL
engine = create_engine(DATABASE_URL)

# Import the User model
from .user import User

# Create the tables defined in the models
Base.metadata.create_all(engine)

# Create a session factory for creating sessions with the database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
