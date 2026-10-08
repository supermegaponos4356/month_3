import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from src.handlers import router
from config import BOT_TOKEN



bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
dp = Dispatcher(storage=MemoryStorage())



async def main():
    dp.include_router(router)
    await dp.start_polling(bot)
    print("бот успешно запущен")


if __name__ == "__main__":
  asyncio.run(main())
