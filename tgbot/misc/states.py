from aiogram.dispatcher.filters.state import StatesGroup, State


class MagioStates(StatesGroup):
    menu_state = State()

    admin_menu_state = State()
    admin_add = State()
    admin_delete = State()
    admin_chose_edit = State()

    change_button_1 = State()
    change_button_2 = State()
    change_button_3 = State()
    change_button_1_1 = State()
    change_button_1_2 = State()
    change_button_contact = State()

    change_city_search_answer = State()
    change_deliver_answer = State()
    change_city_not_found_answer = State()
    change_button2_answer = State()
    change_example_text = State()
    change_example_photo = State()
    change_contact_answer = State()
    change_welcome_photo = State()
    change_caption_welcome_photo = State()

    first_menu = State()
    first_menu_process = State()

    third_menu_photo_1 = State()
    third_menu_photo_2 = State()
    enter_phone = State()