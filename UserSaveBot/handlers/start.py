from aiogram import types, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message
from create_bot import dp, bot
from service.database import SessionLocal
from service.user import User

# Define a handler for the /start command
@dp.message(CommandStart()) 
async def cmd_start(message: types.Message, db=SessionLocal()):
    # Get the username of the user who sent the message
    username = message.from_user.username

    # Check if the user already exists in the database
    existing_user = db.query(User).filter(User.username == username).first()

    if not existing_user:
        # If the user doesn't exist, add them to the database
        user = User(username=username)
        db.add(user)
        db.commit()
        await message.answer("Added to db")
    else:
        # If the user already exists, notify them
        await message.answer("Already in db")
