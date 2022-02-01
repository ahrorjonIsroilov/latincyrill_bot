from aiogram import types

from loader import dp


@dp.message_handler(commands=['start'], state='*')
async def bot_start(message: types.Message):
    await message.answer(f"<b>Hello dear, {message.from_user.full_name} </b> 😊\n\n"
                         f"I am a bot that transfers files from cyril to latin and from latin to cyril.\n"
                         f"Send me a text file or type any message")
