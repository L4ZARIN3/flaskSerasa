from flask import Flask, request

from controllers.serasaCpfController import serasaCpf
from controllers.serasaNomeController import serasaNome
from controllers.serasaEmailController import serasaEmail
from controllers.serasaTelefoneController import serasaTelefone
    
def SerasaBase(app):
    @app.route('/SerasaCpf', methods=['GET'])
    def cpf():
        return serasaCpf(request)

    @app.route('/SerasaNome', methods=['GET'])
    def nome():
        return serasaNome(request)

    @app.route('/SerasaTelefone', methods=['GET'])
    def telefone():
        return serasaTelefone(request)

    @app.route('/SerasaEmail', methods=['GET'])
    def email():
        return serasaEmail(request)
