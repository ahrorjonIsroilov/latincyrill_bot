import os
from pathlib import Path

from aiogram import types
from aiogram.types.input_file import InputFile

import utils
from loader import dp
from states.ConversationState import ConversationState

download_path = Path().joinpath('downloads')
download_path.mkdir(parents=True, exist_ok=True)


@dp.message_handler(commands=['tolatin'], state='*')
async def set_state_to_latin(message: types.Message):
    await message.answer("State changed to: <b>cyril ➔ latin</b>")
    await ConversationState.tolatin.set()


@dp.message_handler(commands=['tocyril'], state='*')
async def set_state_to_cyril(message: types.Message):
    await message.answer("State changed to: <b>latin ➔ cyril</b>")
    await ConversationState.tocyril.set()


@dp.message_handler(state=ConversationState.tolatin, content_types='document')
async def convert_to_latin(message: types.Message):
    file_name = f'downloads/documents/{message.document.file_name}'
    if not file_name.endswith('.txt'):
        await message.answer('<b>Please send only text document ⚠️ </b>')
        return
    await message.document.download(destination_file=file_name)
    await utils.to_latin(f'downloads/documents/{message.document.file_name}')
    await dp.bot.send_document(message.chat.id, InputFile(f'downloads/documents/{message.document.file_name}'),
                               None,
                               '<b>Successfully converted ✅</b>')
    os.remove(f'downloads/documents/{message.document.file_name}')


@dp.message_handler(state=ConversationState.tocyril, content_types='document')
async def convert_to_cyril(message: types.Message):
    file_name = f'downloads/documents/{message.document.file_name}'
    if not file_name.endswith('.txt'):
        await message.answer('<b>Please send only text document ⚠️</b>')
        return
    await message.document.download(destination_file=file_name)
    await utils.to_cyril(f'downloads/documents/{message.document.file_name}')
    await dp.bot.send_document(message.chat.id, InputFile(f'downloads/documents/{message.document.file_name}'),
                               None,
                               '<b>Successfully converted ✅</b>')
    os.remove(f'downloads/documents/{message.document.file_name}')


@dp.message_handler(state=ConversationState.tolatin, content_types='text')
async def convert_to_latin(message: types.Message):
    txt = message.text
    txt = utils.con_to_latin(txt)
    await message.answer(txt)


@dp.message_handler(state=ConversationState.tocyril, content_types='text')
async def convert_to_cyril(message: types.Message):
    txt = message.text
    txt = utils.con_to_cyril(txt)
    await message.answer(txt)
