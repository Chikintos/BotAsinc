from aiogram import types, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message
from create_bot import dp, bot
from service.database import SessionLocal
from service.db_operations import AddUser

# Define a handler for the /start command
@dp.message(CommandStart()) 
async def cmd_start(message: types.Message, db=SessionLocal()):
    # Get the username of the user who sent the message
    username = message.from_user.username

    # Add user to db
    user=AddUser(username,db)
    await message.answer(user['message'])
