from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup



async def inline():
    inline_keyboard = InlineKeyboardMarkup(row_width=1)

    btn1 = InlineKeyboardButton("DO'STLARNI TAKLIF QILISH ↩️", callback_data="btn1")


    inline_keyboard.add(btn1)

    return inline_keyboard