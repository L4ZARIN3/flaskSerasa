from wtforms import Form, StringField, validators


class serasaEmailRequest(Form):
    email = StringField('Email', [
        validators.DataRequired(message="Parametro email obrigatorio."),
        validators.Email(message="Email informado invalido.")
    ])
