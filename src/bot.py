import asyncio 
import logging 
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command

from config import Config
from database import get_users_str, insert_user_if_not_exists

logging.basicConfig(level=logging.INFO)  

bot_token = Config.BOT_TOKEN

bot = Bot(token=str(bot_token))  
dp = Dispatcher()  

# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await insert_user_if_not_exists(
        message.chat.id,
        message.from_user.username,
        message.from_user.full_name
    )
    msg = "Привет! Я простой эхо-бот, а еще я вывожу список моих пользователей по команде /users"
    await message.answer(msg)

@dp.message(Command("users"))
async def cmd_users(message: types.Message):
    users_str = await get_users_str()
    await message.answer(users_str)

@dp.message()
async def echo(message: types.Message):
    await message.answer(message.text if message.text else 'А где текст?')

async def main():
    await dp.start_polling(bot)

if __name__=="__main__":
    asyncio.run(main())
