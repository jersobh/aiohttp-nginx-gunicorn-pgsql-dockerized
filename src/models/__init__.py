import asyncio
import peewee
import logging
from peewee_async import Manager, PostgresqlDatabase

database = PostgresqlDatabase(
    'app',
    user='postgres',
    host='db',
    port='5432',
    password='khW5w5B9MCStJE63'
)
objects = Manager(database)


class UnknownField(object):
    def __init__(self, *_, **__): pass


class BaseModel(peewee.Model):
    class Meta:
        database = database


class User(BaseModel):
    user_id = peewee.PrimaryKeyField()
    username = peewee.CharField(max_length=40, unique=True,  null=False)
    password = peewee.CharField(max_length=40, null=False)
    email = peewee.CharField(max_length=64, null=True)
    created_on = peewee.TimestampField(null=False)
    last_login = peewee.TimestampField()

    class Meta:
        db_table = 'user'


User.create_table(True)
