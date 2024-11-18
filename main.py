import asyncio
import logging 
import sys

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.client.bot import DefaultBotProperties
from aiogram.enums import ParseMode

from config.config import TOKEN_API, maintenance_mode
from utils.bot_commands import set_commands
from handlers import start_handler, help_handler, maintenance, profile_handler
from databases.database import create_db
# from server.background import keep_alive


logger = logging.getLogger(__name__)
bot = Bot(TOKEN_API, default=DefaultBotProperties(parse_mode='HTML'))
dp = Dispatcher(storage=MemoryStorage(), maintenance_mode=maintenance_mode)


async def main() -> None:
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    logger.info("Starting Bot...")

    await create_db()


    dp.include_routers(
        maintenance.maintenance_router,
        start_handler.start_router,
        profile_handler.profile_router,
        help_handler.help_router, 
    )

    await set_commands(bot)

    # await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, handle_signals=False)


if __name__ == "__main__":
    try:
        # keep_alive()
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.info("Bot stopped!")