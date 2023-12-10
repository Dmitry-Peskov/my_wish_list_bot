from aiogram import Router, F
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from states.delete_desire import DeleteDesire
from keyboards import inline_kb as ikb
from core.database import DBHelper


router = Router()


@router.callback_query(StateFilter(None), F.data == "delete_desire")
async def delete_desire_start_process(callback: CallbackQuery, state: FSMContext) -> None:
    user_id = callback.from_user.id
    user_desires = await DBHelper.get_desires(telegram_id=user_id)
    keyboards = ikb.desire_delete_buttons(desires=user_desires)
    await callback.message.answer(text="Какое желание необходимо удалить?", reply_markup=keyboards)
    await state.set_state(DeleteDesire.choice_of_desire)
    await callback.message.delete()
