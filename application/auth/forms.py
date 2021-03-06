from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators, ValidationError 


def hasWhitespace(form, field):
    if ' ' in field.data:
        raise ValidationError("Field contains whitespace.")

class LoginForm(FlaskForm):
    username = StringField("Username", [validators.Length(min=2, max=25), validators.InputRequired(), hasWhitespace])
    password = PasswordField("Password", [validators.Length(min=2, max=25), validators.InputRequired(), hasWhitespace]) 

    class Meta:
        csrf = False


