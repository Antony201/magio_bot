import os

from aiogram import Dispatcher
from aiogram.types import Message

from tgbot.misc.states import MagioStates
from tgbot.services.menus import send_change_buttons_menu
from tgbot.texts import buttons, answers


async def edit_menu_button1(message: Message):
    if message.text != buttons["back_button"]:
        buttons["first_menu_button"] = message.text

        await message.reply(answers["editing_successfull"])

    await send_change_buttons_menu(message)


async def edit_menu_button2(message: Message):
    if message.text != buttons["back_button"]:
        buttons["second_menu_button"] = message.text

        await message.reply(answers["editing_successfull"])

    await send_change_buttons_menu(message)


async def edit_menu_button3(message: Message):
    if message.text != buttons["back_button"]:
        buttons["third_menu_button"] = message.text

        await message.reply(answers["editing_successfull"])

    await send_change_buttons_menu(message)


async def edit_menu_button1_1(message: Message):
    if message.text != buttons["back_button"]:
        buttons["first_menu_find_city_button"] = message.text

        await message.reply(answers["editing_successfull"])

    await send_change_buttons_menu(message)


async def edit_menu_button1_2(message: Message):
    if message.text != buttons["back_button"]:
        buttons["first_menu_free_deliver_button"] = message.text

        await message.reply(answers["editing_successfull"])

    await send_change_buttons_menu(message)


async def edit_city_search_answer(message: Message):
    if message.text != buttons["back_button"]:
        answers["first_menu_enter_city_name"] = message.text

        await message.reply(answers["editing_successfull"])

    await send_change_buttons_menu(message)


async def edit_deliver_answer(message: Message):
    if message.text != buttons["back_button"]:
        answers["deliver_text"] = message.text

        await message.reply(answers["editing_successfull"])

    await send_change_buttons_menu(message)


async def edit_city_not_found_answer(message: Message):
    if message.text != buttons["back_button"]:
        answers["city_not_found"] = message.text

        await message.reply(answers["editing_successfull"])

    await send_change_buttons_menu(message)


async def edit_contact_button(message: Message):
    if message.text != buttons["back_button"]:
        buttons["send_phone"] = message.text

        await message.reply(answers["editing_successfull"])

    await send_change_buttons_menu(message)


async def edit_button_2_answer(message: Message):
    if message.text != buttons["back_button"]:
        answers["not_garanted_text"] = message.text

        await message.reply(answers["editing_successfull"])

    await send_change_buttons_menu(message)


async def edit_example_text(message: Message):
    if message.text != buttons["back_button"]:
        answers["third_answer"] = message.text

        await message.reply(answers["editing_successfull"])

    await send_change_buttons_menu(message)


async def edit_contact_answer(message: Message):
    if message.text != buttons["back_button"]:
        answers["successfull_send"] = message.text

        await message.reply(answers["editing_successfull"])

    await send_change_buttons_menu(message)


async def edit_example_photo(message: Message):
    if message.text != buttons["back_button"]:
        file_path = "tgbot/media/example.jpg"
        if os.path.isfile(file_path):
            os.remove(file_path)

        await message.photo[-1].download(file_path)

        await message.reply(answers["editing_successfull"])

    await send_change_buttons_menu(message)


async def edit_welcome_photo(message: Message):
    if message.text != buttons["back_button"]:
        file_path = "./tgbot/media/welcome_photo.jpg"

        if os.path.isfile(file_path):
            os.remove(file_path)

        await message.photo[-1].download(file_path)

        await message.reply(answers["editing_successfull"])

    await send_change_buttons_menu(message)


async def edit_welcome_photo_caption(message: Message):
    if message.text != buttons["back_button"]:
        answers["welcome_text"] = message.text

        await message.reply(answers["editing_successfull"])

    await send_change_buttons_menu(message)

def register_editor(dp: Dispatcher):
    dp.register_message_handler(edit_menu_button1, state=MagioStates.change_button_1, is_admin=True)
    dp.register_message_handler(edit_menu_button2, state=MagioStates.change_button_2, is_admin=True)
    dp.register_message_handler(edit_menu_button3, state=MagioStates.change_button_3, is_admin=True)
    dp.register_message_handler(edit_menu_button1_1, state=MagioStates.change_button_1_1, is_admin=True)
    dp.register_message_handler(edit_menu_button1_2, state=MagioStates.change_button_1_2, is_admin=True)
    dp.register_message_handler(edit_city_search_answer, state=MagioStates.change_city_search_answer, is_admin=True)
    dp.register_message_handler(edit_deliver_answer, state=MagioStates.change_deliver_answer, is_admin=True)

    dp.register_message_handler(edit_city_not_found_answer,
                                state=MagioStates.change_city_not_found_answer,
                                is_admin=True)

    dp.register_message_handler(edit_contact_button, state=MagioStates.change_button_contact, is_admin=True)
    dp.register_message_handler(edit_button_2_answer, state=MagioStates.change_button2_answer, is_admin=True)
    dp.register_message_handler(edit_example_text, state=MagioStates.change_example_text, is_admin=True)
    dp.register_message_handler(edit_contact_answer, state=MagioStates.change_contact_answer, is_admin=True)

    dp.register_message_handler(edit_example_photo,
                                state=MagioStates.change_example_photo,
                                is_admin=True,
                                content_types=["photo", "text"]
                                )

    dp.register_message_handler(edit_welcome_photo,
                                state=MagioStates.change_welcome_photo,
                                is_admin=True,
                                content_types=["photo", "text"]
                                )

    dp.register_message_handler(edit_welcome_photo_caption,
                                state=MagioStates.change_caption_welcome_photo, is_admin=True)
