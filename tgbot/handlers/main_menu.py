from aiogram import Dispatcher
from aiogram.types import Message

from tgbot.keyboards.reply import back_button_keyboard
from tgbot.misc.states import MagioStates
from tgbot.services.city_parser import find_address
from tgbot.services.db_worker import is_admin
from tgbot.services.menus import send_admin_menu, send_main_menu, send_first_menu
from tgbot.texts import buttons, answers


async def menu_chose(message: Message):
    if message.text == buttons["admin_panel_button"] and is_admin(message.from_user):
        await send_admin_menu(message)

    elif message.text == buttons["first_menu_button"]:
        await send_first_menu(message)

    elif message.text == buttons["second_menu_button"]:
        await message.reply(answers["not_garanted_text"])
        await send_main_menu(message)

    elif message.text == buttons["third_menu_button"]:
        photo = open("./tgbot/media/example.jpg", "rb")
        kb = await back_button_keyboard()

        await message.bot.send_photo(
            message.from_user.id,
            photo=photo,
            caption=answers["third_answer"],
            reply_markup=kb
        )

        await MagioStates.third_menu_photo_1.set()


async def first_menu(message: Message):
    if message.text == buttons["first_menu_find_city_button"]:
        kb = await back_button_keyboard()

        await message.reply(answers["first_menu_enter_city_name"], reply_markup=kb)
        await MagioStates.first_menu_process.set()

    elif message.text == buttons["first_menu_free_deliver_button"]:
        await message.reply(answers["deliver_text"])
        await send_main_menu(message)

    elif message.text == buttons["back_button"]:
        await send_main_menu(message)


async def process_user_city(message: Message):
    if message.text == buttons["back_button"]:
        await send_first_menu(message)

    else:
        city_text = await find_address(message.text)

        await message.reply(city_text)
        await send_main_menu(message)


def register_menu(dp: Dispatcher):
    dp.register_message_handler(menu_chose, state=MagioStates.menu_state)
    dp.register_message_handler(first_menu, state=MagioStates.first_menu)
    dp.register_message_handler(process_user_city, state=MagioStates.first_menu_process)