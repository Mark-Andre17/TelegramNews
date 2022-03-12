import asyncio
import logging
from aiogram import Bot, Dispatcher, executor
from aiogram.types import ReplyKeyboardRemove
from aiogram.dispatcher.filters import Text
from token2 import token
from parsing_news import parsing_SportExpress, parsing_SovSport, parsing_championat
from parsing_films import get_releases
from keyboard import *

bot = Bot(token)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)


@dp.message_handler(commands=['start'])
async def start_bot(message):
    await message.answer(
        f'Aloha,{message.from_user.first_name},\U0001F44B!\nЗдесь можно посмотреть актуальные новости.',
        reply_markup=get_start_keyboard())


@dp.message_handler(commands=['end'])
async def command_end(message):
    await message.answer(f'{message.from_user.first_name} ,Bye-Bye \U0001F44B ',
                         reply_markup=ReplyKeyboardRemove())


@dp.message_handler(Text(equals='Спорт \U000026F9'))
async def bot_message(message):
    await message.answer(f'Выберите спортивное издание', reply_markup=get_sport_keyboard())


@dp.message_handler(Text(equals='Sport-Express \U0001F3D0'))
async def pars_SE(message):
    for link_se in parsing_SportExpress():
        await message.answer(f'{link_se}')
        await asyncio.sleep(2)


@dp.message_handler(Text(equals='SovSport \U0001F94A'))
async def pars_SS(message):
    for link_ss in parsing_SovSport():
        await message.answer(f'{link_ss}')
        await asyncio.sleep(2)


@dp.message_handler(Text(equals='Championat \U0001F93E'))
async def pars_CH(message):
    for link_champ in parsing_championat():
        await message.answer(f'{link_champ}')
        await asyncio.sleep(2)


@dp.message_handler(Text(equals='Назад \U0001F519'))
async def get_back(message):
    await message.answer(f'{message.from_user.first_name}, Вы вернулись в главное меню!\nЗдесь можно '
                         f'посмотреть актуальные '
                         'новости. ', reply_markup=get_start_keyboard())


@dp.message_handler(Text(equals='Последние кинопремьеры \U0001F3AC'))
async def pars_films(message):
    await message.answer(f'Выберите нужный пункт меню', reply_markup=get_films_keyboard())


@dp.message_handler(Text(equals='Премьеры месяца \U0001F3A5'))
async def pars_releases(message):
    for film_release in get_releases():
        await message.answer(f'{film_release}')
        await asyncio.sleep(2)


@dp.message_handler()
async def unknown_message(message):
    await message.answer(f'Неизвестная команда.Возвращаю в главное меню.', reply_markup=get_start_keyboard())


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
