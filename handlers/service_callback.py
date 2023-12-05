from aiogram import Router, F
from aiogram.types import CallbackQuery

router = Router()


@router.callback_query(F.data == "delete_message")
async def delete_message_clbk(callback: CallbackQuery) -> None:
    await callback.message.delete()
