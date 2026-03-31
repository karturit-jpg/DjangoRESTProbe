import asyncio
import os

import aiohttp
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message


BOT_TOKEN = os.environ["BOT_TOKEN"] # каким синтаксисом передать секрет?
BACKEND_BIND_URL = os.environ["BACKEND_BIND_URL"]

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def handle_start(message: Message): # асинхронная библиотека, всегда писать асинхронные функции
    await message.answer(
        "Hello! Send me the code from the website, and I will link your Telegram account."
    )


@dp.message()
async def handle_bind_code(message: Message):
    code = message.text.strip()
    telegram_id = message.from_user.id

    payload = {
        "code": code,
        "telegram_id": telegram_id,
    }

    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(BACKEND_BIND_URL, json=payload) as response:
                data = await response.json()
    except aiohttp.ClientError:
        await message.answer("Could not connect to the backend. Please try again later.")
        return

    if response.status == 200 and data.get("status") == "ok":
        await message.answer("Your Telegram account has been successfully linked.")
    else:
        await message.answer(data.get("message", "Binding failed."))


# @dp.message(Command("help")) # чтобы закоментировать фрагмент кода -- Ctrl + /
# async def handle_help(message: Message):
#     await message.answer("Here are my commands:\n/start - start the bot\n/help - show this message")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main()) # для чего писать конкретно это выражение?

# что за файл "main.py"? какого вида в нем должны быть написаны выражения, чтобы запускать "локально"?
# как пакет бота завязан на main.py?
# интересный комментарий от ai ниже

# значит, main.py - это файл, который содержит точку входа в приложение. В нем должны быть написаны выражения, которые запускают приложение в режиме "локального" тестирования или разработки. Это может включать инициализацию приложения, настройку конфигурации, инициализацию базы данных и других зависимостей, а также запуск основного цикла приложения.
