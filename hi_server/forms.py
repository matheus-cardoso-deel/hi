# -*- coding : utf8 -*-

from wtforms import Form, TextAreaField, TextField, PasswordField, validators

class RegisterForm(Form):
    name = TextField('Nome', [validators.Length(min=4, max=25)])
    email = TextField('Email', [validators.Length(min=6, max=35)])
    description = TextAreaField('Descricao')
    password = PasswordField('Senha', [
        validators.Required(),
        validators.EqualTo('confirm', message='Senhas')
    ])
    confirm = PasswordField('Repita senha')

class LoginForm(Form):
    email = TextField('Email', [validators.Length(min=6, max=35)])
    password = PasswordField('Senha', [validators.Required()])