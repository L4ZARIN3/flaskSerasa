from peewee import *

db = SqliteDatabase('databases/srs_contatos.db')


class SRS_CONTATOS(Model):
    CONTATOS_ID = CharField(primary_key=True)
    CPF = CharField()
    NOME = CharField()
    SEXO = CharField()
    NASC = CharField()
    NOME_MAE = CharField()
    NOME_PAI = CharField()
    CADASTRO_ID = CharField()
    ESTCIV = CharField()
    RG = CharField()
    NACIONALID = CharField()
    CONTATOS_ID_CONJUGE = CharField()
    SO = CharField()
    CD_SIT_CAD = CharField()
    DT_SIT_CAD = CharField()
    DT_INFORMACAO = CharField()
    CBO = CharField()
    ORGAO_EMISSOR = CharField()
    UF_EMISSAO = CharField()
    DT_OB = CharField()
    CD_MOSAIC = CharField()
    RENDA = CharField()
    FAIXA_RENDA_ID = CharField()
    TITULO_ELEITOR = CharField()
    CD_MOSAIC_NOVO = CharField()
    CD_MOSAIC_SECUNDARIO = CharField()

    class Meta:
        database = db
        table_name = 'SRS_CONTATOS'


db.connect()
