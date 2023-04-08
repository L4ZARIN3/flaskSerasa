from peewee import *

db = SqliteDatabase('databases/system.db')


class Admins(Model):
    id = PrimaryKeyField(unique=True)
    username = CharField(unique=True)
    password = CharField()

    class Meta:
        database = db

class Tokens(Model):
    id = PrimaryKeyField(unique=True)
    admin_id = ForeignKeyField(Admins, backref='Tokens')
    username = CharField()
    token = CharField(unique=True)
    plan = DateTimeField()

    class Meta:
        database = db


class Dbs(Model):
    id = PrimaryKeyField(unique=True)
    token_id = ForeignKeyField(Tokens, backref='Dbs')
    status = CharField()

    class Meta:
        database = db



db.connect()

if not Admins.table_exists():
    db.create_tables([Admins])
    
if not Tokens.table_exists():
    db.create_tables([Tokens])

if not Dbs.table_exists():
    db.create_tables([Dbs])