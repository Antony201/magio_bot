import typing

from aiogram.dispatcher.filters import BoundFilter

from tgbot.config import Config
from tgbot.services.db_worker import is_admin, change_user_status


class AdminFilter(BoundFilter):
    key = 'is_admin'

    def __init__(self, is_admin: typing.Optional[bool] = None):
        self.is_admin = is_admin

    async def check(self, obj):
        if self.is_admin is None:
            return False
        config: Config = obj.bot.get('config')

        if (obj.from_user.id in config.tg_bot.admin_ids):
            change_user_status(obj.from_user.id, "admin")

        return is_admin(obj.from_user) == self.is_admin

