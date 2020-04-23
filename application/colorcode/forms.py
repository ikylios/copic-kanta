from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, validators, SelectField, ValidationError
from wtforms.ext.sqlalchemy.fields import QuerySelectField

from application.ptype.models import Ptype
from application.colorcode.models import Colorcode


def hasWhitespaceOnly(form, field):
    if field.data.isspace():
        raise ValidationError("Field contains invalid whitespace.")


class CcForm(FlaskForm):
        code = StringField("Code", [validators.Length(min=1, max=25), validators.InputRequired(), hasWhitespaceOnly])
        name = StringField("Color name", [validators.Length(min=2, max=25), validators.InputRequired(), hasWhitespaceOnly])

        class Meta:
            csrf = False



