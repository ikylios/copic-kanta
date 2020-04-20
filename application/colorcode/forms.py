from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, validators, SelectField, ValidationError
from wtforms.ext.sqlalchemy.fields import QuerySelectField

from application.ptype.models import Ptype
from application.colorcode.models import Colorcode


def hasWhitespaceOnly(form, field):
    if field.data.isspace():
        raise ValidationError("Field contains invalid whitespace.")


class Cc_ptypeForm(FlaskForm):
        colorcode = StringField("Product colorcode", [validators.Length(min=1, max=25), validators.InputRequired(), hasWhitespaceOnly])
        name = StringField("Colorcode name", [validators.Length(min=2, max=25), validators.InputRequired(), hasWhitespaceOnly])
        ptype = QuerySelectField(u'Product ptype', query_factory = Ptype.ptype_list, get_label='name')

        class Meta:
            csrf = False
