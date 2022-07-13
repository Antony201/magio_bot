from aiogram.dispatcher.filters.state import StatesGroup, State


class MagioStates(StatesGroup):
    menu_state = State()

    admin_menu_state = State()
    admin_add = State()
    admin_delete = State()

    first_menu = State()
    first_menu_process = State()

    third_menu_photo_1 = State()
    third_menu_photo_2 = State()
    enter_phone = State()