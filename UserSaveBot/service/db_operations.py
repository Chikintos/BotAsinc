from service.database import SessionLocal
from service.user import User

# Function to create a database session
def CreateSession():
    return SessionLocal()

# Function to close a database session
def CloseSession(data):
    db = data.get('db')
    if db:
        # Close the database session
        db.close()

# Function to add a user to the database
def AddUser(username, db):
    # Check if the user already exists in the database
    existing_user = db.query(User).filter(User.username == username).first()
    
    if not existing_user:
        # If the user doesn't exist, add them to the database
        user = User(username=username)
        db.add(user)
        db.commit()
        return {"status": 1, "message": "User added to db"}
    else:
        # If the user already exists, return a message indicating that
        return {"status": 0, "message": "User already in db"}
