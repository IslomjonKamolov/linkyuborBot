Token = "7296367500:AAHPmQq7HeJrwCF8oMHYUNxKOPywaWBrC_c"

import logging
import asyncio
from aiogram import F
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from Keyboard import Hello_button

from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application
from aiohttp import web
WEBHOOK_URL = "https://1ebc-188-113-203-4.ngrok-free.app/webhook" 

# Tokenni o'zgartiring
API_TOKEN = Token

# Loggingni sozlash
logging.basicConfig(level=logging.INFO)

# Botni yaratish
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def say_hello(message:Message):
    await message.answer("Hello user!\nWelcome to me :)", reply_markup=Hello_button)

@dp.message(F.text == "Linkni olish")
async def give_link(message:Message):
    await message.answer("https://t.me/botlar_io,\n\nBu sizning linkingiz!")
    await bot.send_message(6150443453, f"user {'@'+message.from_user.username if message.from_user.username else f'<a href=\"tg://user?id={message.from_user.id}\">{message.from_user.full_name}</a>'} Link oldi.", parse_mode="HTML")

# Botni ishga tushirish
async def on_startup(app: web.Application):
    await bot.set_webhook(WEBHOOK_URL)

async def on_shutdown(app: web.Application):
    await bot.delete_webhook()

async def main():
    app = web.Application()
    app.on_startup.append(on_startup)
    app.on_shutdown.append(on_shutdown)

    SimpleRequestHandler(dispatcher=dp, bot=bot).register(app, path="/webhook")
    setup_application(app, dp)

    return app

if __name__ == "__main__":
    web.run_app(main(), host="0.0.0.0", port=8080)
