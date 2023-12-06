import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from handlers import commands
from handlers import service_callback
from handlers import add_desire
from config import API_BOT

# инициализируем диспетчера
dp = Dispatcher(storage=MemoryStorage())
# подключаем к диспетчеру обработчики событий
dp.include_router(commands.router)
dp.include_router(service_callback.router)
dp.include_router(add_desire.router)

async def main() -> None:
    bot = Bot(API_BOT.TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
