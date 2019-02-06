from datetime import datetime

from peewee import *

from .settings import database


class BaseModel(Model):
    add_time = DateTimeField(default=datetime.now, verbose_name='加入时间')

    class Meta:
        database = database
