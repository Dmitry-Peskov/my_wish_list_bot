from aiogram import Router
from aiogram.enums import ParseMode
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold
from models.user import User
from sources import messages as msg
from keyboards import inline_kb as ikb
from core.database import DBHelper

router = Router()


@router.message(CommandStart())
async def start_cmd(message: Message) -> None:
    this_user_exists = await DBHelper.this_user_exists(message.from_user.id)
    if this_user_exists:
        await message.answer(f"С возвращением, 👤{hbold(message.from_user.full_name)}!", reply_markup=ikb.main_menu())
    else:
        new_user = User(telegram_id=message.from_user.id,
                        fullname=message.from_user.full_name,
                        nickname=message.from_user.username)
        await DBHelper.add_user(new_user)
        await message.answer(f"Добро пожаловать, 👤{hbold(message.from_user.full_name)}!\nВы были зарегистрированы.", reply_markup=ikb.main_menu())
    await message.delete()


@router.message(Command("help"))
async def help_cmd(message: Message) -> None:
    await message.answer(text=msg.help_msg(), reply_markup=ikb.delete_message(), disable_web_page_preview=True, parse_mode=ParseMode.HTML)
    await message.delete()


@router.message(Command("about"))
async def about_cmd(message: Message) -> None:
    await message.answer(text=msg.about_msg(), reply_markup=ikb.delete_message(), parse_mode=ParseMode.HTML)
    await message.delete()
