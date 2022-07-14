from aiogram import Dispatcher
from aiogram.types import Message

from tgbot.config import Config
from tgbot.services.db_worker import create_user
from tgbot.services.menus import send_main_menu
from tgbot.texts import answers


async def user_start(message: Message):
    config: Config = message.bot.get('config')

    status = "user"

    if (message.from_user.id in config.tg_bot.admin_ids):
        status = "root"

    create_user(str(message.from_user.username), message.from_user.id, status)
    base_photo = open("./tgbot/media/welcome_photo.jpg", "rb")

    await message.bot.send_photo(
        message.from_user.id,
        photo=base_photo,
        caption=answers["welcome_text"]
    )
    await send_main_menu(message)


def register_user(dp: Dispatcher):
    dp.register_message_handler(user_start, commands=["start"], state="*")
