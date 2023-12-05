from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def delete_message() -> InlineKeyboardMarkup:
    mrk = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="🗑 Убрать сообщение", callback_data="delete_message")]])
    return mrk
