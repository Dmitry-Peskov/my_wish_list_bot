from aiogram import Router, F
from aiogram.types import CallbackQuery
from core.database import DBHelper
from sources import messages as msg

router = Router()


@router.callback_query(F.data == "get_desire")
async def get_desire(callback: CallbackQuery) -> None:
    user_id = callback.from_user.id
    nickname = callback.from_user.username
    desires = await DBHelper.get_desires(user_id)
    answer = msg.get_desire(desires, user_id, nickname)
    await callback.message.edit_text(text=answer, disable_web_page_preview=True)
