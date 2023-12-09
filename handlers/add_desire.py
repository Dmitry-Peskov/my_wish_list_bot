from aiogram import Router, F
from aiogram.filters import StateFilter, Command
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message
from states.add_desire import AddDesire
from sources import messages as msg
from utils.formated import TextFormate
from keyboards import inline_kb as ikb
from models.desire import Desire
from core.database import DBHelper

router = Router()


@router.message(StateFilter(AddDesire), Command("cancel"))
async def cancel_add_desire(message: Message, state: FSMContext):
    username = message.from_user.full_name
    answer = msg.back_to_main_menu_msg(username)
    keyboard = ikb.main_menu()
    await state.clear()
    await message.answer(text=answer, reply_markup=keyboard)
    await message.delete()


@router.callback_query(StateFilter(None), F.data == "add_desire")
async def start_add_desire(callback: CallbackQuery, state: FSMContext):
    username = callback.from_user.full_name
    answer = msg.get_desire_title(username)
    await callback.message.edit_text(text=answer)
    await state.set_state(AddDesire.get_desire_title)


@router.message(AddDesire.get_desire_title)
async def choice_desire_title(message: Message, state: FSMContext):
    desire_title = TextFormate.cut_off_120_characters(message.text)
    await state.update_data(title=desire_title)
    await state.set_state(AddDesire.get_desire_url)
    answer = msg.get_desire_url()
    await message.answer(text=answer)
    await message.delete()


@router.message(AddDesire.get_desire_url)
async def choice_desire_url(message: Message, state: FSMContext):
    # TODO Нужно не забыть сделать валидатор, для проверки корреткности URL
    # TODO Если URL кривой, заного просить иначе кидать на следующий шаг
    keyboard = ikb.confirm_correctness()
    check_result = True  # пока заглушка, до реализации валидатора
    if check_result:
        await state.update_data(url=message.text)
        await state.set_state(AddDesire.get_desire_confirm)
        desire_info = await state.get_data()
        title, url = str(desire_info["title"]), str(desire_info["url"])
        answer = msg.get_confirmed_desire(title, url)
        await message.answer(text=answer, reply_markup=keyboard, disable_web_page_preview=True)
    else:
        answer = msg.not_valid_url_msg()
        await message.answer(text=answer, reply_markup=keyboard)
        await state.set_state(AddDesire.get_desire_url)
    await message.delete()


@router.callback_query(AddDesire.get_desire_confirm, F.data.in_({"confirm_desire", "cancel_add_desire"}))
async def choice_desire_confirm(callback: CallbackQuery, state: FSMContext):
    if callback.data == "confirm_desire":
        desire_info = await state.get_data()
        title = str(desire_info["title"])
        url = str(desire_info["url"])
        user_id = callback.from_user.id
        answer = msg.add_desire_msg_completed(title, url)
        new_desire = Desire(title=title,
                            url=url,
                            user_id=user_id)
        await DBHelper.add_desire(new_desire)
        await callback.message.answer(text=answer, disable_web_page_preview=True)
        await state.clear()
    else:
        username = callback.from_user.full_name
        answer = msg.get_desire_title(username)
        await state.clear()
        await state.set_state(AddDesire.get_desire_title)
        await callback.message.answer(text=answer)
    await callback.message.delete()
