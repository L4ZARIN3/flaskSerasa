from wtforms import Form, StringField, TextAreaField, validators


class serasaEmailRequest(Form):
    email = StringField('Email', [
        validators.DataRequired(message="Parametro email obrigatorio."),
        validators.Email(message="Email informado invalido.")
    ])
