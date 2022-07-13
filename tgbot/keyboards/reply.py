from aiogram import types

from tgbot.services.db_worker import is_admin
from tgbot.texts import buttons



async def menu_keyboard(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)

    button1 = types.KeyboardButton(text=buttons["first_menu_button"])
    button2 = types.KeyboardButton(text=buttons["second_menu_button"])
    button3 = types.KeyboardButton(text=buttons["third_menu_button"])

    keyboard.add(button1, button2, button3)

    if is_admin(message.from_user):
        admin_button = types.KeyboardButton(buttons["admin_panel_button"])
        keyboard.add(admin_button)


    return keyboard


async def admin_menu_keyboard():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)

    button1 = types.KeyboardButton(text=buttons["admin_add_button"])
    button2 = types.KeyboardButton(text=buttons["admin_delete_button"])
    button3 = types.KeyboardButton(text=buttons["admin_list"])
    button4 = types.KeyboardButton(text=buttons["back_button"])

    keyboard.add(button1)
    keyboard.add(button2)
    keyboard.add(button3)
    keyboard.add(button4)



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