from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import Dispatcher
from aiogram.types import ReplyKeyboardRemove

from keyboard import *


class FSMPhone(StatesGroup):
    phone = State()
    phone_code = State()
    user_phone = State()
    first_name = State()
    last_name = State()


async def get_phone(message: types.Message):
    await FSMPhone.phone.set()
    await message.answer(f'Введите Ваш номер телефона(+7....без пробелов):', reply_markup=ReplyKeyboardRemove())


async def stop_bot(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply('Ок')


async def load_phone(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['phone'] = message.text
    await FSMPhone.next()
    await message.answer('Введите код подтверждения:')


async def load_phone_code(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['phone_code'] = message.text
    await FSMPhone.next()
    await message.answer('Введите телефон для рассылки:')


async def load_phone_user(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['user_phone'] = message.text
    await FSMPhone.next()
    await message.answer('Введите имя:')


async def first_name_phone(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['first_name'] = message.text
    await FSMPhone.next()
    await message.answer('Введите фамилию:')


async def last_name_phone(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['last_name'] = message.text
    async with state.proxy() as data:
        await message.reply(str(data))
    await state.finish()


def register_handler_state(dp: Dispatcher):
    dp.register_message_handler(get_phone, commands=['Авторизация'], state=None)
    dp.register_message_handler(load_phone, state=FSMPhone.phone)
    dp.register_message_handler(load_phone_code, state=FSMPhone.phone_code)
    dp.register_message_handler(load_phone_user, state=FSMPhone.user_phone)
    dp.register_message_handler(first_name_phone, state=FSMPhone.first_name)
    dp.register_message_handler(last_name_phone, state=FSMPhone.last_name)
    dp.register_message_handler(stop_bot, state='*', commands='отмена')
    dp.register_message_handler(stop_bot, Text(equals='отмена', ignore_case=True), state='*')