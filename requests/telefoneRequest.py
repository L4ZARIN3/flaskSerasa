from wtforms import Form, StringField, TextAreaField, validators


class serasaTelefoneRequest(Form):
    telefone = StringField('Telefone', [
        validators.DataRequired(message="Parametro telefone obrigatorio."),
        validators.Length(
            min=8, max=11, message="O campo telefone deve ter de 8 a 11 digitos.")
    ])
