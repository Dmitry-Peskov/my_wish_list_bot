from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold
from orm import database as db

router = Router()

@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    this_user_exists = await db.this_user_exists(message.from_user.id)
    if this_user_exists:
        await message.answer(f"С возвращением, 👤{hbold(message.from_user.full_name)}!")
    else:
        await db.add_user(message.from_user.id,
                          message.from_user.full_name,
                          message.from_user.username)
        await message.answer(f"Добро пожаловать, 👤{hbold(message.from_user.full_name)}!\nВы были зарегистрированы.")
    await message.delete()