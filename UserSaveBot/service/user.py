from sqlalchemy import Column, Integer, String
from service.database import Base

# Define the User model
class User(Base):
    # Define the table name
    __tablename__ = "users"

    # Define the columns of the table
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)

    # Define a string representation for the model
    def __repr__(self):
        return f"<User(id={self.id}, username={self.username})>"
