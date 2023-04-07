import peewee
from flask import jsonify

from models.srs_emails import SRS_EMAIL
from models.srs_contatos import SRS_CONTATOS

from requests.emailRequest import serasaEmailRequest


def serasaEmail(request):
    form = serasaEmailRequest(request.args)
    if not form.validate():
        return jsonify(form.errors), 400

    email = request.args.get('email')
    emails = SRS_EMAIL.select().where(SRS_EMAIL.EMAIL == email)
    if emails:
        emailUsers = []
        for currentEmail in emails:
            emailUsers.append(currentEmail.CONTATOS_ID)

        users = SRS_CONTATOS.select().where(SRS_CONTATOS.CONTATOS_ID.in_(emailUsers))

        mailOwners = {'status': True, 'rows': emails.count(),
                      'search': email, 'result': []}

        for user in users:
            mailOwners['result'].append({
                'NOME': user.NOME,
                'NOME_MAE': user.NOME_MAE,
                'CPF': user.CPF,
                'SEXO': user.SEXO,
                'NASC': user.NASC,
                'RENDA': user.RENDA,
                'TITULO_ELEITOR': user.TITULO_ELEITOR
            })

        return jsonify(mailOwners)
    else:
        return 'nada encontrado'
