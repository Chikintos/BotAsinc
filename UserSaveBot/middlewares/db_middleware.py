from aiogram.dispatcher.middlewares.base import BaseMiddleware
from service.db_operations import CreateSession,CloseSession
# Define a middleware for interacting with the database
class DbMiddleware(BaseMiddleware):
    def __init__(self):
        super().__init__()

    # This method is called before processing a message
    async def on_pre_process_message(self, message, data):
        # Create a new database session and attach it to the 'data' dictionary
        data['db'] = CreateSession()

    # This method is called after processing a message
    async def on_post_process_message(self, message, data):
        # Retrieve the database session from the 'data' dictionary
        CloseSession(data)
