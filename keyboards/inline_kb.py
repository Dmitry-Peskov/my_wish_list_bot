from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def delete_message() -> InlineKeyboardMarkup:
    mrk = InlineKeyboardMarkup(
        inline_keyboard=[[InlineKeyboardButton(text="🗑 Убрать сообщение", callback_data="delete_message")]])
    return mrk


def main_menu() -> InlineKeyboardMarkup:
    mrk = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🎁 Загадать желание", callback_data="add_desire")],
        [InlineKeyboardButton(text="🙅‍♀ Отказаться от мечты", callback_data="delete_desire"),
         InlineKeyboardButton(text="✍ Скорректировать планы", callback_data="edit_desire")],
        [InlineKeyboardButton(text="📝 Получить список", callback_data="get_desire")],
        [InlineKeyboardButton(text="🔙 Скрыть меню", callback_data="delete_message")]
    ])
    return mrk


def confirm_correctness() -> InlineKeyboardMarkup:
    mrk = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🟢 Корректно", callback_data="confirm_desire")],
        [InlineKeyboardButton(text="🔴 Давай заново", callback_data="cancel_add_desire")]
    ])
    return mrk


def desire_delete_buttons(desires: list[dict[str]]) -> InlineKeyboardMarkup:
    buttons = list()
    for desire in desires:
        btn = [InlineKeyboardButton(text=desire["title"], callback_data=str(desire["id"]))]
        buttons.append(btn)
    mrk = InlineKeyboardMarkup(inline_keyboard=buttons)
    return mrk
