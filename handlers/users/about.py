from aiogram import types

from loader import dp


@dp.message_handler(commands=['about'], state='*')
async def bot_start(message: types.Message):
    await message.answer(f"<b>Have a great day {message.from_user.full_name} </b> 😊\n")
    await dp.bot.send_contact(message.chat.id, +998903061599, 'Ahrorjon', 'Isroilov', False)
