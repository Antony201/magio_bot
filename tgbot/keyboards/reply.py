from aiogram import types

from tgbot.services.db_worker import is_admin, is_root
from tgbot.texts import buttons



async def menu_keyboard(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)

    button1 = types.KeyboardButton(text=buttons["first_menu_button"])
    button2 = types.KeyboardButton(text=buttons["second_menu_button"])
    button3 = types.KeyboardButton(text=buttons["third_menu_button"])

    keyboard.add(button1, button2, button3)

    if is_root(message.from_user):
        admin_button = types.KeyboardButton(buttons["admin_panel_button"])
        keyboard.add(admin_button)


    return keyboard


async def admin_menu_keyboard():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)

    button1 = types.KeyboardButton(text=buttons["admin_add_button"])
    button2 = types.KeyboardButton(text=buttons["admin_delete_button"])
    button3 = types.KeyboardButton(text=buttons["admin_list"])
    button4 = types.KeyboardButton(text=buttons["admin_change_texts"])
    button5 = types.KeyboardButton(text=buttons["back_button"])

    keyboard.add(button1)
    keyboard.add(button2)
    keyboard.add(button3)
    keyboard.add(button4)
    keyboard.add(button5)



    return keyboard


async def deliver_keyboard():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)

    button1 = types.KeyboardButton(text=buttons["first_menu_find_city_button"])
    button2 = types.KeyboardButton(text=buttons["first_menu_free_deliver_button"])
    button3 = types.KeyboardButton(text=buttons["back_button"])

    keyboard.add(button1)
    keyboard.add(button2)
    keyboard.add(button3)

    return keyboard


async def back_button_keyboard():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)

    button1 = types.KeyboardButton(text=buttons["back_button"])
    keyboard.add(button1)

    return keyboard

async def get_contact():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)

    button1 = types.KeyboardButton(text=buttons["send_phone"], request_contact=True)

    keyboard.add(button1)

    return keyboard


async def change_menu_keyboard():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)

    button1 = types.KeyboardButton(text=buttons["change_first_menu_button"])
    button2 = types.KeyboardButton(text=buttons["change_second_menu_button"])
    button3 = types.KeyboardButton(text=buttons["change_third_menu_button"])
    button4 = types.KeyboardButton(text=buttons["change_first_first_menu_button"])
    button5 = types.KeyboardButton(text=buttons["change_first_second_menu_button"])
    button6 = types.KeyboardButton(text=buttons["change_city_search_answer"])
    button7 = types.KeyboardButton(text=buttons["change_deliver_answer"])
    button8 = types.KeyboardButton(text=buttons["change_city_not_found_text"])
    button9 = types.KeyboardButton(text=buttons["change_send_contact_button"])
    button10 = types.KeyboardButton(text=buttons["change_second_menu_answer"])
    button11 = types.KeyboardButton(text=buttons["change_example_photo"])
    button12 = types.KeyboardButton(text=buttons["change_example_text"])
    button13 = types.KeyboardButton(text=buttons["change_welcome_photo"])
    button14 = types.KeyboardButton(text=buttons["change_caption_welcome_photo"])
    button15 = types.KeyboardButton(text=buttons["change_contact_answer"])

    back_button = types.KeyboardButton(text=buttons["back_button"])

    keyboard.add(button1)
    keyboard.add(button2)
    keyboard.add(button3)
    keyboard.add(button4)
    keyboard.add(button5)
    keyboard.add(button6)
    keyboard.add(button7)
    keyboard.add(button8)
    keyboard.add(button9)
    keyboard.add(button10)
    keyboard.add(button11, button13)
    keyboard.add(button12, button14)
    keyboard.add(button15)

    keyboard.add(back_button)


    return keyboard