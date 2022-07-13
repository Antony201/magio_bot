from aiogram import Dispatcher
from aiogram.types import Message

from tgbot.keyboards.reply import get_contact
from tgbot.misc.states import MagioStates
from tgbot.services.menus import send_main_menu
from tgbot.texts import buttons, answers
from tgbot.services.db_worker import (
    change_user_photo_1,
    change_user_photo_2,
    change_user_phone, get_admin_ids, get_user
)


async def third_text_type(message: Message):
    if message.text == buttons["back_button"]:
        await send_main_menu(message)

    else:
        await message.reply(answers["send_photo"])


async def first_photo_type(message: Message):
    try:
        print(message.message_id)
        change_user_photo_1(message.from_user.id, message.message_id)

        await message.reply(answers["second_photo"])
        await MagioStates.third_menu_photo_2.set()

    except Exception as e:
        print(e)
        await message.reply(answers["wrong"])
        await send_main_menu(message)


async def third_text_2_type(message: Message):
    if message.text == buttons["back_button"]:
        await send_main_menu(message)

    else:
        await message.reply(answers["send_photo"])


async def second_photo_type(message: Message):
    try:
        change_user_photo_2(message.from_user.id, message.message_id)

        kb = await get_contact()

        await message.reply(answers["enter_phone"], reply_markup=kb)
        await MagioStates.enter_phone.set()

    except Exception:
        await message.reply(answers["wrong"])
        await send_main_menu(message)


async def get_user_phone(message: Message):
    try:
        change_user_phone(message.from_user.id, message.contact.phone_number)

        admins = get_admin_ids()


        user = get_user(message.from_user.id)


        result_text = answers["result_text"].format(
            str(message.from_user.first_name),
            str(message.from_user.username),
            str(message.from_user.id),
            str(user.phone)
        )

        for admin_id in admins:

            await message.bot.forward_message(
                admin_id,
                user.user_id,
                user.first_photo_id
            )

            await message.bot.forward_message(
                admin_id,
                user.user_id,
                user.second_photo_id
            )

            await message.bot.send_message(admin_id, result_text)

        await message.reply(answers["successfull_send"])

        await send_main_menu(message)

    except Exception:
        await message.reply(answers["wrong"])
        await send_main_menu(message)


def register_offer(dp: Dispatcher):
    dp.register_message_handler(third_text_type, state=MagioStates.third_menu_photo_1)
    dp.register_message_handler(
        first_photo_type,
        state=MagioStates.third_menu_photo_1,
        content_types=["photo"]
    )

    dp.register_message_handler(third_text_2_type, state=MagioStates.third_menu_photo_2)
    dp.register_message_handler(
        second_photo_type,
        state=MagioStates.third_menu_photo_2,
        content_types=["photo"]
    )

    dp.register_message_handler(get_user_phone, state=MagioStates.enter_phone, content_types=["contact"])

