# -*- coding : utf8 -*-

from wtforms import Form, TextAreaField, TextField, PasswordField, validators

class RegisterForm(Form):
    name = TextField('Nome', [validators.required(), validators.Length(min=4, max=25)])
    username = TextField('Usuario', [validators.Length(min=5, max=35)])
    email = TextField('Email', [validators.required(), validators.Length(min=6, max=35)])
    description = TextAreaField('Descricao', [validators.required()])
    password = PasswordField('Senha', [
        validators.Required(),
        validators.EqualTo('confirm', message='Senhas')
    ])
    confirm = PasswordField('Repita senha')

class LoginForm(Form):
    username = TextField('Usuario', [validators.Length(min=5, max=35)])
    password = PasswordField('Senha', [validators.Required()])