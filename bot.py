from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils import executor

import random
import settings

test = KeyboardButton('Математический мини тестик')
echo = KeyboardButton('Эхо')

start = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True).add(test, echo)

bot = Bot(token=settings.TOKEN_TELEGRAM)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer('Добро пожаловать, дорогой пользователь!\nЧем я могу вам помочь?', reply_markup=start)


@dp.message_handler(Text(equals='Математический мини тестик'))
async def math_test(message: types.Message):
    a = random.randint(1, 20)
    b = random.randint(1, 20)
    await message.answer('Стартуем')
    await message.answer('Сколько будет ' + str(a) + '+' + str(b))

    @dp.message_handler()
    async def math_equation(message: types.Message):
        if message.text == str(a + b):
            await message.answer('Правильно')
        else:
            await message.answer('Неправильно')


@dp.message_handler(Text(equals='Эхо'))
async def echo(message: types.Message):
    await bot.send_message(message.from_user.id, message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
