
from flask_wtf import FlaskForm
from wtforms import StringField, validators


def hasWhitespace(form, field):
    if ' ' in field.data:
        raise ValidationError("Field contains whitespace")


class PtypeForm(FlaskForm):
    name = StringField("Product type name", [validators.Length(min=2, max=25), validators.InputRequired(), hasWhitespace])

    class Meta:
        csrf = False
