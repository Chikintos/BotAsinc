import asyncio
import logging
import sys
from create_bot import dp, bot

async def main() -> None:
    # Import the start handler
    from handlers import start

    # Configure logging
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)

    # Start polling the bot for updates
    await dp.start_polling(bot, skip_updates=False)

if __name__ == "__main__":
    # Run the main function using asyncio
    asyncio.run(main())
