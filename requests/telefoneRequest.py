from wtforms import Form, StringField, TextAreaField, validators


class serasaTelefoneRequest(Form):
    telefone = StringField('telefone', [
        validators.DataRequired(message="Parametro telefone obrigatorio."),
        validators.Length(
            min=10, max=11, message="O campo telefone deve ter de 10 a 11 digitos.")
    ])
