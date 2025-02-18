from aiogram.fsm.state import StatesGroup, State

class SurveyStates(StatesGroup):
    AWAITING_ANSWER = State()