from peewee import *

db = SqliteDatabase('databases/srs_telefones.db')


class SRS_TELEFONES(Model):
    CONTATOS_ID = CharField()
    DDD = CharField()
    TELEFONE = CharField()
    TIPO_TELEFONE = CharField()
    DT_INCLUSAO = CharField()
    DT_INFORMACAO = CharField()
    SIGILO = CharField()
    NSU = CharField()
    CLASSIFICACAO = CharField()

    class Meta:
        database = db
        table_name = 'SRS_HISTORICO_TELEFONES'
        primary_key = False


db.connect()
