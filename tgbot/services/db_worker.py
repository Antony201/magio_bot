from tgbot.models.User import User


def is_user(username):
    query = User.select().where(User.username == username)

    if query.exists():
        return query[0]

    else:
        return None


def get_admin_list():
    query = User.select().where(User.status == "admin")

    return query


def delete_user(username):
    query = User.select().where(User.username == username)

    if query.exists():
        query[0].delete_instance()

        return True

    else:
        return False


def create_user(username, user_id, status):
    query = User.select().where(User.user_id == user_id)

    if not query.exists():
        user = User.create(
            username=username,
            user_id=user_id,
            status=status
        )

        user.save()

        return user


    return None



def change_user_status(user_id, status):
    query = User.select().where(User.user_id == user_id)

    if query.exists():
        user = query[0]
        user.status = status
        user.save()

        return True

    return None


def change_user_photo_1(user_id, message_id):
    query = User.select().where(User.user_id == user_id)

    if query.exists():
        user = query[0]
        user.first_photo_id = message_id
        user.save()

        return True

    return None


def change_user_photo_2(user_id, message_id):
    query = User.select().where(User.user_id == user_id)

    if query.exists():
        user = query[0]
        user.second_photo_id = message_id
        user.save()

        return True

    return None


def change_user_phone(user_id, phone):
    query = User.select().where(User.user_id == user_id)

    if query.exists():
        user = query[0]
        user.phone = phone
        user.save()

        return True

    return None


def is_admin(user):
    query = User.select().where(User.user_id == user.id)

    if query.exists():
        user_status = query[0].status

        return user_status == "admin"


    return False


def get_admin_ids():
    query = User.select().where(User.status == "admin")

    if query.exists():
        admins = []

        for admin in query:
            admins.append(admin.user_id)

        return admins

    else:
        return []


def get_user(user_id):
    query = User.select().where(User.user_id == user_id)

    if query.exists():
        user = query[0]

        return user

    else:
        return None