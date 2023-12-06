from aiogram import Router, F
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message
from states.add_desire import AddDesire
from sources import messages as msg
from utils import formated_text
from keyboards import inline_kb as ikb
from orm import database as db

router = Router()


@router.callback_query(StateFilter(None), F.data == "add_desire")
async def choice_desire_title(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text(text=msg.get_desire_title(callback.from_user.full_name))
    await state.set_state(AddDesire.get_desire_title)


@router.message(AddDesire.get_desire_title)
async def choice_desire_url(message: Message, state: FSMContext):
    desire_title = formated_text.cut_off_120_characters(message.text)
    await state.update_data(title=desire_title)
    await state.set_state(AddDesire.get_desire_url)
    await message.answer(text=msg.get_desire_url())


@router.message(AddDesire.get_desire_url)
async def choice_desire_url(message: Message, state: FSMContext):
    # TODO Нужно не забыть сделать валидатор, для проверки корреткности URL
    # TODO Если URL кривой, заного просить иначе кидать на следующий шаг
    check_result = True  # пока заглушка, до реализации валидатора
    if check_result:
        await state.update_data(url=message.text)
        await state.set_state(AddDesire.get_desire_confirm)
        desire_info = await state.get_data()
        title, url = str(desire_info["title"]), str(desire_info["url"])
        await message.answer(text=msg.get_confirmed_desire(title, url), reply_markup=ikb.confirm_correctness())
    else:
        await message.answer(text=msg.not_valid_url_msg(), reply_markup=ikb.confirm_correctness())
        await state.set_state(AddDesire.get_desire_url)


@router.callback_query(AddDesire.get_desire_confirm, F.data == "confirm_desire")
async def choice_desire_confirm(callback: CallbackQuery, state: FSMContext):
    desire_info = await state.get_data()
    title = str(desire_info["title"])
    url = str(desire_info["url"])
    user_id = callback.from_user.id
    message = msg.add_desire_msg_completed(title, url)
    await db.add_desire(user_id,
                        title,
                        url)
    await callback.message.answer(message)
    await state.clear()
