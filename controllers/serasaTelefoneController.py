from flask import jsonify

from models.srs_telefones import SRS_TELEFONES
from models.srs_contatos import SRS_CONTATOS

from requests.telefoneRequest import serasaTelefoneRequest


def serasaTelefone(request):
    form = serasaTelefoneRequest(request.args)
    if not form.validate():
        return jsonify(form.errors), 400
    
    telefone = request.args.get('telefone')

    UserPhones = SRS_TELEFONES.select().where(
        SRS_TELEFONES.DDD == telefone[:2]).where(SRS_TELEFONES.TELEFONE == telefone[2:])
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
