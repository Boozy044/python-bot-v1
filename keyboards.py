from aiogram import types

from databese import get_buttons


async def get_main_keyboard():
    buttons_text = await get_buttons()
    buttons = []

    for text in buttons_text:
        buttons.append(types.KeyboardButton(text=text[0]))

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=2)
    keyboard.add(*buttons)
    return keyboard
