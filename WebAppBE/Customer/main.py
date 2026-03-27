import asyncio
import os
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command

bot = Bot(token=os.environ.get('BOT_TOKEN')) # каким синтаксисом передать секрет?
dp = Dispatcher(bot)

@dp.message(Command("start"))
async def handle_start(message: Message): # асинхронная библиотека, всегда писать асинхронные функции
    await message.answer("Hello! I'm your bot. Type /help for commands.")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

