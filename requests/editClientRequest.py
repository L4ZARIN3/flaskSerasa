from wtforms import Form, StringField, validators
from datetime import datetime


class editUserRequest(Form):
    username = StringField('Username', [
        validators.DataRequired(message="Parametro username obrigatorio."),
    ])

    plan = StringField('Plan', [validators.DataRequired(
        message="Data do plano obrigatoria.")])

    id = StringField('Id', [
        validators.DataRequired(message="Informe o id do usuario a ser editado."),
    ])
    
    def validate_data(form, field):
        try:
            datetime.strptime(field.data, '%Y-%m-%dT%H:%M')
        except ValueError:
            raise validators.ValidationError('Data inválida')
