import asyncio
import logging

from aiogram import Bot, Dispatcher
from handles import router

bot = Bot(token="")
dp = Dispatcher()

async def main():
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())