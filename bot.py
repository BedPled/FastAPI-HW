import logging
import asyncio
from aiogram import Bot, types, Dispatcher
from aiogram.filters import Command
from aiogram import F
import requests
import os

BOT_TOKEN = os.environ.get('BOT_TOKEN')
FASTAPI_URL = 'http://localhost:8000'


bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot=bot)


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    buttons = [
        [
            types.KeyboardButton(text="GET /", callback_data='root'),
            types.KeyboardButton(text="POST /post", callback_data='post'),
            types.KeyboardButton(text="GET /dog", callback_data='get_dog'),
            types.KeyboardButton(text="POST /dog", callback_data='post_dog'),
            types.KeyboardButton(text="GET /dog/{pk}", callback_data='get_dog_by_id'),
            types.KeyboardButton(text="PATCH /dog/{pk}", callback_data='get_dog_by_type'),
        ]
    ]

    keyboard = types.ReplyKeyboardMarkup(
        keyboard=buttons,
        resize_keyboard=True,
        input_field_placeholder="Выбери запрос:"
    )
    await message.answer("Привет!", reply_markup=keyboard)

@dp.message(F.text == "GET /")
async def root(message: types.Message):
    x = requests.get(FASTAPI_URL)
    await message.reply(str(x.status_code))

@dp.message(F.text == "POST /post")
async def post(message: types.Message):
    x = requests.post(FASTAPI_URL + '/post', json={"id": 0, "timestamp": 0})
    await message.reply(str(x.status_code))

@dp.message(F.text == "GET /dog")
async def get_dog(message: types.Message):
    x = requests.get(FASTAPI_URL + '/dog')
    await message.reply(str(x.text))

@dp.message(F.text == "POST /dog")
async def post_dog(message: types.Message):
    x = requests.post(FASTAPI_URL + '/dog/add?name=NEW_DOG&kind=dalmatian')
    await message.reply(str(x.status_code))

@dp.message(F.text == "GET /dog/{pk}")
async def get_dog_by_id(message: types.Message):
    x = requests.get(FASTAPI_URL + '/dog/1')
    await message.reply(str(x.text))

@dp.message(F.text == "PATCH /dog/{pk}")
async def get_dog_by_type(message: types.Message):
    x = requests.patch(FASTAPI_URL + '/dog/3?name=PUPA')
    await message.reply(str(x.status_code))

async def main():
    logging.basicConfig(level=logging.DEBUG)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
