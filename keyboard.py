from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def get_start_keyboard():
    start = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button_1 = KeyboardButton('Спорт \U000026F9')
    button_2 = KeyboardButton('Последние кинопремьеры \U0001F3AC')
    start.add(button_1, button_2)
    return start


def get_sport_keyboard():
    sport_keyboard = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    sport_button1 = KeyboardButton('Sport-Express \U0001F3D0')
    sport_button2 = KeyboardButton('SovSport \U0001F94A')
    sport_button3 = KeyboardButton('Championat \U0001F93E')
    sport_button4 = KeyboardButton('Назад \U0001F519')
    sport_keyboard.add(sport_button1, sport_button2, sport_button3, sport_button4)
    return sport_keyboard


def get_films_keyboard():
    films_keyboard = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    films_button1 = KeyboardButton('Премьеры месяца \U0001F3A5')
    films_button3 = KeyboardButton('Назад \U0001F519')
    films_keyboard.add(films_button1, films_button3)
    return films_keyboard