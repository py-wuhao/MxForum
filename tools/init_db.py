from peewee import MySQLDatabase

from MxForum.settings import settings
from apps.users.models import User

database = MySQLDatabase(**settings['db'])


def init():
    database.create_tables([User])


if __name__ == '__main__':
    init()
