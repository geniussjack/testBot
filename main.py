from aiogram import html
from aiogram.filters import CommandStart
from aiogram.utils.keyboard import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import Message, Update
from aiogram.fsm.context import FSMContext

from quart import Quart, request

import asyncio

from config import bot, dp, Form, welcome_message

app = Quart(__name__)

@dp.message(CommandStart())
async def hello(message: Message, state: FSMContext) -> None:
    await message.answer(f'Добро пожаловать, {message.from_user.username}!')
    await message.answer(html.bold("Введите ваш город: "))
    await state.set_state(Form.waiting_for_city)

@dp.message(Form.waiting_for_city)
async def process_city(message: Message, state: FSMContext) -> None:
    await state.update_data(city=message.text)
    buttons = [
        [KeyboardButton(text="Личный кабинет"), KeyboardButton(text="Модели"), KeyboardButton(text="О нас")]
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)
    await message.answer(welcome_message, reply_markup=keyboard)
    await state.clear()

async def set_webhook():
    await bot.set_webhook(url="https://escortscumbot.pythonanywhere.com/webhook",
                          allowed_updates=dp.resolve_used_update_types(),
                          drop_pending_updates=True)

async def delete_webhook():
    await bot.delete_webhook()

@app.route('/webhook', methods=['POST'])
async def webhook():
    update = Update.model_validate(await request.json, context={"bot": bot})
    await dp.feed_update(bot, update)
    return "", 200

@app.before_serving
async def startup():
    await set_webhook()

@app.after_serving
async def cleanup():
    await delete_webhook()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)