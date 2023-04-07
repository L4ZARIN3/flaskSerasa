from flask import jsonify

from models.srs_telefones import SRS_TELEFONES
from models.srs_contatos import SRS_CONTATOS


def serasaTelefone():
    UserPhones = SRS_TELEFONES.select().where(
        SRS_TELEFONES.DDD == '11').where(SRS_TELEFONES.TELEFONE == '972146724')
    phoneUsers = []
    if UserPhones:
        for phone in UserPhones:
            phoneUsers.append(phone.CONTATOS_ID)

        users = SRS_CONTATOS.select().where(SRS_CONTATOS.CONTATOS_ID.in_(phoneUsers))
        contactUsers = {'status': True, 'rows': users.count(), 'result': []}
        for user in users:
            contactUsers['result'].append({
                'NOME': user.NOME,
                'NOME_MAE': user.NOME_MAE,
                'CPF': user.CPF,
                'SEXO': user.SEXO,
                'NASC': user.NASC,
                'RENDA': user.RENDA,
                'TITULO_ELEITOR': user.TITULO_ELEITOR
            })

        return jsonify(contactUsers)
    else:
        return jsonify({'status': False, 'msg': 'Contato não encontrado.'}), 404
