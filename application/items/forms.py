from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, validators, SelectField, ValidationError
from wtforms.ext.sqlalchemy.fields import QuerySelectField

from application.ptype.models import Ptype
from application.colorcode.models import Colorcode


def hasWhitespaceOnly(form, field):
    if field.data.isspace():
        raise ValidationError("Field contains invalid whitespace.")


class ItemForm(FlaskForm):
	colorcode = QuerySelectField(u'Item colorcode', query_factory = Colorcode.colorcode_list, get_label='code')
	ptype = QuerySelectField(u'Item type', query_factory = Ptype.ptype_list, get_label='name')

	class Meta:
		csrf = False


class CodeSearchForm(FlaskForm):
     search = StringField([validators.Length(min=1, max=10), validators.InputRequired(), hasWhitespaceOnly])
#    incl = BooleanField()

     class Meta:
                csrf = False
