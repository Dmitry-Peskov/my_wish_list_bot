from aiogram import Router, F
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from states.delete_desire import DeleteDesire
from keyboards import inline_kb as ikb
from core.database import DBHelper
from sources import messages as msg


router = Router()


@router.callback_query(StateFilter(None), F.data == "delete_desire")
async def delete_desire_start_process(callback: CallbackQuery, state: FSMContext) -> None:
    user_id = callback.from_user.id
    user_desires = await DBHelper.get_desires(telegram_id=user_id)
    keyboards = ikb.desire_delete_buttons(desires=user_desires)
    answer = msg.what_desire_delete()
    await callback.message.answer(text=answer, reply_markup=keyboards)
    await state.set_state(DeleteDesire.choice_of_desire)
    await callback.message.delete()


@router.callback_query(DeleteDesire.choice_of_desire)
async def delete_desire_confirmed(callback: CallbackQuery, state: FSMContext) -> None:
    desire_id = callback.data
    await state.update_data(desire_id=desire_id)
    answer = msg.confirmed_delete_desire()
    keyboards = ikb.desire_delete_confirmed_buttons()
    await state.set_state(DeleteDesire.confirm_the_deletion)
    await callback.message.edit_text(text=answer, reply_markup=keyboards)


@router.callback_query(DeleteDesire.confirm_the_deletion, F.data.in_({"confirmed_delete", "abort_delete"}))
async def confirmed_delete(callback: CallbackQuery, state: FSMContext) -> None:
    if callback.data == "confirmed_delete":
        state_data = await state.get_data()
        user_id = callback.from_user.id
        desire_id = int(state_data["desire_id"])
        delete_desire_name = await DBHelper.delete_desire(user_id=user_id, desire_id=desire_id)
        answer = msg.delete_desire(delete_desire_name)
        await callback.message.edit_text(text=answer)
    else:
        username = callback.from_user.full_name
        answer = msg.back_to_main_menu_msg(username)
        keyboards = ikb.main_menu()
        await callback.message.edit_text(text=answer, reply_markup=keyboards)
    await state.clear()