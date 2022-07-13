from peewee import *
from tgbot.engine import db


class User(Model):
    username = CharField()
    user_id = CharField()
    status = CharField()

    first_photo_id = CharField(null=True)
    second_photo_id = CharField(null=True)
    phone = CharField(null=True)

    class Meta:
        database = db


db.create_tables([User, ])