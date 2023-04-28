from flask import jsonify

from models.srs_contatos import SRS_CONTATOS
from models.srs_emails import SRS_EMAIL
from models.srs_telefones import SRS_TELEFONES
from models.srs_enderecos import SRS_ENDERECOS

from requests.cpfRequest import serasaCpfRequest


def serasaCpf(request):
    form = serasaCpfRequest(request.args)
    if not form.validate():
        return jsonify(form.errors), 400

    cpf = request.args.get("cpf")
    contato = SRS_CONTATOS.select().where(SRS_CONTATOS.CPF == cpf).first()
    if contato:
        contato_dict = {
            "status": True,
            "search": cpf,
            "result": {
                "CONTATOS_ID": contato.CONTATOS_ID,
                "CPF": contato.CPF,
                "NOME": contato.NOME,
                "SEXO": contato.SEXO,
                "NASC": contato.NASC,
                "NOME_MAE": contato.NOME_MAE,
                "NOME_PAI": contato.NOME_PAI,
                "CADASTRO_ID": contato.CADASTRO_ID,
                "ESTCIV": contato.ESTCIV,
                "RG": contato.RG,
                "NACIONALID": contato.NACIONALID,
                "CONTATOS_ID_CONJUGE": contato.CONTATOS_ID_CONJUGE,
                "SO": contato.SO,
                "CD_SIT_CAD": contato.CD_SIT_CAD,
                "DT_SIT_CAD": contato.DT_SIT_CAD,
                "DT_INFORMACAO": contato.DT_INFORMACAO,
                "CBO": contato.CBO,
                "ORGAO_EMISSOR": contato.ORGAO_EMISSOR,
                "UF_EMISSAO": contato.UF_EMISSAO,
                "DT_OB": contato.DT_OB,
                "CD_MOSAIC": contato.CD_MOSAIC,
                "RENDA": contato.RENDA,
                "FAIXA_RENDA_ID": contato.FAIXA_RENDA_ID,
                "TITULO_ELEITOR": contato.TITULO_ELEITOR,
                "CD_MOSAIC_NOVO": contato.CD_MOSAIC_NOVO,
                "CD_MOSAIC_SECUNDARIO": contato.CD_MOSAIC_SECUNDARIO,
                "EMAILS": [],
                "TELEFONES": [],
                "ENDERECOS": [],
            },
        }

        # CONSULTA TELEFONES
        UserPhones = SRS_TELEFONES.select().where(
            SRS_TELEFONES.CONTATOS_ID == contato.CONTATOS_ID
        )

        if UserPhones:
            for phone in UserPhones:
                contato_dict["result"]["TELEFONES"].append(phone.DDD + phone.TELEFONE)
        else:
            contato_dict["result"]["TELEFONES"] = None

        # CONSULTA ENDERECOS
        UserEnderecos = SRS_ENDERECOS.select().where(
            SRS_ENDERECOS.CONTATOS_ID == contato.CONTATOS_ID
        )

        if UserEnderecos:
            for endereco in UserEnderecos:
                contato_dict["result"]["ENDERECOS"].append(
                    {
                        "CONTATOS_ID": endereco.CONTATOS_ID,
                        "LOGR_TIPO": endereco.LOGR_TIPO,
                        "LOGR_NOME": endereco.LOGR_NOME,
                        "LOGR_NUMERO": endereco.LOGR_NUMERO,
                        "LOGR_COMPLEMENTO": endereco.LOGR_COMPLEMENTO,
                        "BAIRRO": endereco.BAIRRO,
                        "CIDADE": endereco.CIDADE,
                        "UF": endereco.UF,
                        "CEP": endereco.CEP,
                        "DT_ATUALIZACAO": endereco.DT_ATUALIZACAO,
                        "DT_INCLUSAO": endereco.DT_INCLUSAO,
                        "TIPO_ENDERECO_ID": endereco.TIPO_ENDERECO_ID,
                    }
                )
        else:
            contato_dict["result"]["ENDERECOS"] = None

        # CONSULTA EMAILS
        UserEmails = SRS_EMAIL.select().where(
            SRS_EMAIL.CONTATOS_ID == contato.CONTATOS_ID
        )

        if UserEmails:
            for email in UserEmails:
                contato_dict["result"]["EMAILS"].append(email.EMAIL)
        else:
            contato_dict["result"]["EMAILS"] = None

        return jsonify(contato_dict)
    else:
        return jsonify({"status": False, "msg": "Cpf nao encontrado."}), 404
