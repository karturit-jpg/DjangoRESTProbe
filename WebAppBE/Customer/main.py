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


@dp.message(Command("help"))
async def handle_help(message: Message):
    await message.answer("Here are my commands:\n/start - start the bot\n/help - show this message")


@dp.message()
async def bind_telegram_account(message: Message):
    code = message.text.strip()
    telegram_id = message.from_user.id

    # here you need to check the code in Django DB
    # and then save telegram_id to the related user


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__": # для чего писать конкретно это выражение?
    asyncio.run(main())

# что за файл "main.py"? какого вида в нем должны быть написаны выражения, чтобы запускать "локально"?