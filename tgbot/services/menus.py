from aiogram.types import Message
from tgbot.keyboards.reply import admin_menu_keyboard, menu_keyboard, deliver_keyboard
from tgbot.misc.states import MagioStates
from tgbot.texts import answers



async def send_admin_menu(message: Message):
    kb = await admin_menu_keyboard()

    await message.reply(answers["menu"], reply_markup=kb)
    await MagioStates.admin_menu_state.set()


async def send_main_menu(message: Message, text=None):
    kb = await menu_keyboard(message)

    if not text:
        text = answers["menu"]

    await message.reply(text, reply_markup=kb)
    await MagioStates.menu_state.set()


async def send_first_menu(message: Message):
    keyboard = await deliver_keyboard()

    await message.reply(answers["menu"], reply_markup=keyboard)
    await MagioStates.first_menu.set()