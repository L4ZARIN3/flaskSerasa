# from requests.cpfRequest import ContactForm
from wtforms import Form, StringField, TextAreaField, validators


class serasaCpfRequest(Form):
    cpf = StringField('Cpf', [
        validators.DataRequired(message="Parametro cpf obrigatorio."),
        validators.Length(
            min=11, max=11, message="O campo cpf deve ter exatamente 11 digitos.")
    ])
