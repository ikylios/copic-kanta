
from flask_wtf import FlaskForm
from wtforms import StringField, validators, ValidationError


def hasWhitespaceOnly(form, field):
    if field.data.isspace():
        raise ValidationError("Field contains invalid whitespace.")

class PtypeForm(FlaskForm):
    name = StringField("Product type name", [validators.Length(min=2, max=25), validators.InputRequired(), hasWhitespaceOnly])

    class Meta:
        csrf = False
