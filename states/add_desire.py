from aiogram.fsm.state import StatesGroup, State


class AddDesire(StatesGroup):
    get_desire_title = State()
    get_desire_url = State()
    get_desire_confirm = State()

