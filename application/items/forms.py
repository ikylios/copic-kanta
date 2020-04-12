from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, validators, SelectField, ValidationError
from wtforms.ext.sqlalchemy.fields import QuerySelectField

from application.ptype.models import Ptype
from application.colorcode.models import Colorcode


def hasWhitespaceOnly(form, field):
    if field.data.isspace():
        raise ValidationError("Field contains invalid whitespace.")


class ItemForm(FlaskForm):
	name = StringField("Item name", [validators.Length(min=2, max=25), validators.InputRequired(), hasWhitespaceOnly])
	colorcode = StringField("Item colorcode", [validators.Length(min=2, max=25), validators.InputRequired(), hasWhitespaceOnly])
	ptype = QuerySelectField(u'Item ptype', query_factory = Ptype.ptype_list, get_label='name')

	class Meta:
		csrf = False


class PersonalItemForm(FlaskForm):
	colorcode = QuerySelectField(u'Item colorcode', query_factory = Colorcode.colorcode_list, get_label='code')
	ptype = QuerySelectField(u'Item type', query_factory = Ptype.ptype_list, get_label='name')

	class Meta:
		csrf = False


