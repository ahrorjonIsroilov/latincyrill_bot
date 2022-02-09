from aiogram.dispatcher.filters.state import StatesGroup, State


class ConversationState(StatesGroup):
    tolatin = State()
    tocyril = State()
