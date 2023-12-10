from aiogram.fsm.state import StatesGroup, State


class DeleteDesire(StatesGroup):
    choice_of_desire = State()
    confirm_the_deletion = State()
