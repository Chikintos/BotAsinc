from aiogram import Bot
from aiogram import Dispatcher
from config import TOKEN

# Initialize the bot with the provided TOKEN and set parse mode to HTML
bot = Bot(token=TOKEN, parse_mode="HTML")

# Initialize the dispatcher
dp = Dispatcher()
