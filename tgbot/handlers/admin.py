from aiogram import Dispatcher
from aiogram.types import Message

from tgbot.keyboards.reply import back_button_keyboard
from tgbot.misc.states import MagioStates
from tgbot.services.db_worker import is_user, change_user_status, get_admin_list, delete_user, is_admin
from tgbot.services.menus import send_admin_menu, send_main_menu, send_change_buttons_menu
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
        await MagioStates.admin_delete.set()

    if message.text == buttons["admin_list"]:
        admin_list = get_admin_list()
        admin_list_text = "Список Адмінів:\n"

        for adm in admin_list:
            admin_list_text += adm.username + "\n"

        await message.reply(admin_list_text)
        await send_admin_menu(message)

    if message.text == buttons["admin_change_texts"]:
        await send_change_buttons_menu(message)

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
        change_user_status(user.user_id, "user")

        await message.reply(answers["admin_delete_successfull"])
        try:
            await message.bot.send_message(user.user_id, answers["you_not_admin"])
        except Exception:
            await message.bot.send_message(message.from_user.id, answers["wrong"])

        await admin_start(message)

    else:
        await message.reply(answers["admin_delete_not_found"])


async def chose_editing(message: Message):
    kb = await back_button_keyboard()

    if message.text != buttons["back_button"]:
        await message.reply(answers["change_text"], reply_markup=kb)

        if message.text == buttons["change_first_menu_button"]:
            await MagioStates.change_button_1.set()

        if message.text == buttons["change_second_menu_button"]:
            await MagioStates.change_button_2.set()

        if message.text == buttons["change_third_menu_button"]:
            await MagioStates.change_button_3.set()

        if message.text == buttons["change_first_first_menu_button"]:
            await MagioStates.change_button_1_1.set()

        if message.text == buttons["change_first_second_menu_button"]:
            await MagioStates.change_button_1_2.set()

        if message.text == buttons["change_city_search_answer"]:
            await MagioStates.change_city_search_answer.set()

        if message.text == buttons["change_deliver_answer"]:
            await MagioStates.change_deliver_answer.set()

        if message.text == buttons["change_city_not_found_text"]:
            await MagioStates.change_city_not_found_answer.set()

        if message.text == buttons["change_send_contact_button"]:
            await MagioStates.change_button_contact.set()

        if message.text == buttons["change_second_menu_answer"]:
            await MagioStates.change_button2_answer.set()

        if message.text == buttons["change_example_text"]:
            await MagioStates.change_example_text.set()

        if message.text == buttons["change_example_photo"]:
            await MagioStates.change_example_photo.set()

        if message.text == buttons["change_contact_answer"]:
            await MagioStates.change_contact_answer.set()

        if message.text == buttons["change_welcome_photo"]:
            await MagioStates.change_welcome_photo.set()


        if message.text == buttons["change_caption_welcome_photo"]:
            await MagioStates.change_caption_welcome_photo.set()


    else:
        await send_admin_menu(message)


def register_admin(dp: Dispatcher):
    dp.register_message_handler(admin_start, commands=["start"], state="*", is_admin=True)
    dp.register_message_handler(admin_menu, state=MagioStates.admin_menu_state, is_admin=True)
    dp.register_message_handler(add_admin, state=MagioStates.admin_add, is_admin=True)
    dp.register_message_handler(delete_admin, state=MagioStates.admin_delete, is_admin=True)
    dp.register_message_handler(chose_editing, state=MagioStates.admin_chose_edit, is_admin=True)
