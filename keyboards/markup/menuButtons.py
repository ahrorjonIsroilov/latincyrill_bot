from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

mainMenu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🐱‍👤 courses'),
            KeyboardButton(text='🐱‍👤 machine learning'),
            KeyboardButton(text='❤ love'),
        ],
        [
            KeyboardButton(text='🤦‍♂ shy'),
            KeyboardButton(text='🎂 happy birthday')
        ],

    ], resize_keyboard=True
)
