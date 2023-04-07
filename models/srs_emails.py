from peewee import *

db = SqliteDatabase('databases/srs_emails.db')


class SRS_EMAIL(Model):
    CONTATOS_ID = CharField()
    EMAIL = CharField()
    PRIORIDADE = CharField()
    EMAIL_SCORE = CharField()
    EMAIL_PESSOAL = CharField()
    EMAIL_DUPLICADO = CharField()
    BLACKLIST = CharField()
    ESTRUTURA = CharField()
    STATUS_VT = CharField()
    DOMINIO = CharField()
    MAPAS = CharField()
    PESO = CharField()
    CADASTRO_ID = CharField()
    DT_INCLUSAO = CharField()

    class Meta:
        database = db
        table_name = 'SRS_EMAIL'
        primary_key = False


db.connect()
