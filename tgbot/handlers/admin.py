from aiogram import Dispatcher
from aiogram.types import Message

from tgbot.keyboards.reply import back_button_keyboard
from tgbot.misc.states import MagioStates
from tgbot.services.db_worker import is_user, change_user_status, get_admin_list, delete_user
from tgbot.services.menus import send_admin_menu, send_main_menu
from tgbot.texts import buttons, answers


async def admin_start(message: Message):
    await send_main_menu(message)


async def admin_menu(message: Message):
    if message.text == buttons["admin_add_button"]:
        kb = await back_button_keyboard()

        await message.reply(answers["enter_admin_username"], reply_markup=kb)
        await MagioStates.admin_add.set()

    if message.text == buttons["admin_delete_button"]:
        kb = await back_button_keyboard()

        await message.reply(answers["enter_admin_username"], reply_markup=kb)
        await MagioStates.admin_add.set()

    if message.text == buttons["admin_list"]:
        admin_list = get_admin_list()
        admin_list_text = "Список Адмінів:\n"

        for adm in admin_list:
            admin_list_text += adm.username + "\n"

        await message.reply(admin_list_text)
        await send_admin_menu(message)

    if message.text == buttons["back_button"]:
        await admin_start(message)


async def add_admin(message: Message):
    user = is_user(message.text)

    if message.text == buttons["back_button"]:
        await send_admin_menu(message)


    elif user:
        change_user_status(user.user_id, "admin")

        await message.reply(answers["admin_add_successfull"])
        await admin_start(message)

        await message.bot.send_message(user.user_id, answers["admin_message"])


    else:
        await message.reply(answers["admin_add_not_found"])


async def delete_admin(message: Message):
    user = is_user(message.text)

    if message.text == buttons["back_button"]:
        await send_admin_menu(message)


    elif user:
        delete_user(message.text)

        await message.reply(answers["admin_delete_successfull"])
        await admin_start(message)

    else:
        await message.reply(answers["admin_delete_not_found"])


def register_admin(dp: Dispatcher):
    dp.register_message_handler(admin_start, commands=["start"], state="*", is_admin=True)
    dp.register_message_handler(admin_menu, state=MagioStates.admin_menu_state, is_admin=True)
    dp.register_message_handler(add_admin, state=MagioStates.admin_add, is_admin=True)
