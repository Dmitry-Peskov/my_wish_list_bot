from aiogram import Router
from aiogram.enums import ParseMode
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold
from orm import database as db
from sources import messages as msg
from keyboards import inline_kb as ikb

router = Router()


@router.message(CommandStart())
async def start_cmd(message: Message) -> None:
    this_user_exists = await db.this_user_exists(message.from_user.id)
    if this_user_exists:
        await message.answer(f"С возвращением, 👤{hbold(message.from_user.full_name)}!", reply_markup=ikb.main_menu())
    else:
        await db.add_user(message.from_user.id,
                          message.from_user.full_name,
                          message.from_user.username)
        await message.answer(f"Добро пожаловать, 👤{hbold(message.from_user.full_name)}!\nВы были зарегистрированы.", reply_markup=ikb.main_menu())
    await message.delete()


@router.message(Command("help"))
async def help_cmd(message: Message) -> None:
    await message.answer(text=msg.help_msg(), reply_markup=ikb.delete_message(), parse_mode=ParseMode.HTML)
    await message.delete()


@router.message(Command("about"))
async def about_cmd(message: Message) -> None:
    await message.answer(text=msg.about_msg(), reply_markup=ikb.delete_message(), parse_mode=ParseMode.HTML)
    await message.delete()
