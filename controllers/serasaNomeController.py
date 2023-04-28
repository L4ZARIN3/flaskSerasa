from flask import jsonify

from models.srs_contatos import SRS_CONTATOS


def serasaNome(request):
    nome = request.args.get("nome")
    peoples = SRS_CONTATOS.select().where(SRS_CONTATOS.NOME == nome.upper())

    if peoples:
        people_dict = {'status': True, 'rows': peoples.count(), 'result': []}
        for user in peoples:
            people_dict['result'].append({
                'NOME': user.NOME,
                'NOME_MAE': user.NOME_MAE,
                'CPF': user.CPF,
                'SEXO': user.SEXO,
                'NASC': user.NASC,
                'RENDA': user.RENDA,
                'TITULO_ELEITOR': user.TITULO_ELEITOR
            })

        return jsonify(people_dict)

    else:
        return jsonify({'status': False, 'msg': 'nenhuma pessoa encontrada.'}), 404
