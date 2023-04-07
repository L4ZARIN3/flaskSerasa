from flask import Flask, request, jsonify

from controllers.serasaCpfController import serasaCpf
from controllers.serasaNomeController import serasaNome
from controllers.serasaEmailController import serasaEmail
from controllers.serasaTelefoneController import serasaTelefone




def route(app):
    @app.route('/SerasaCpf', methods=['GET'])
    def cpf():
        return serasaCpf(request);

    @app.route('/SerasaNome', methods=['GET'])
    def nome():
        return serasaNome(request.args.get('nome'))

    @app.route('/SerasaTelefone', methods=['GET'])
    def telefone():
        return serasaTelefone()

    @app.route('/SerasaEmail', methods=['GET'])
    def email(email):
        return serasaEmail(email)
