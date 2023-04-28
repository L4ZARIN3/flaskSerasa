from peewee import *

db = SqliteDatabase('databases/srs_enderecos.db')


class SRS_ENDERECOS(Model):
    CONTATOS_ID = CharField()
    LOGR_TIPO = CharField()
    LOGR_NOME = CharField()
    LOGR_NUMERO = CharField()
    LOGR_COMPLEMENTO = CharField()
    BAIRRO = CharField()
    CIDADE = CharField()
    UF = CharField()
    CEP = CharField()
    DT_ATUALIZACAO = CharField()
    DT_INCLUSAO = CharField()
    TIPO_ENDERECO_ID = CharField()
    class Meta:
        database = db
        table_name = 'SRS_ENDERECOS'
        primary_key = False


db.connect()
