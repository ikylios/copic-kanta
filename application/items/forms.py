from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, validators, SelectField, ValidationError
from wtforms.ext.sqlalchemy.fields import QuerySelectField

from application.ptype.models import Ptype
from application.colorcode.models import Colorcode


def hasWhitespace(form, field):
    if ' ' in field.data:
        raise ValidationError("Field contains whitespace")


class ItemForm(FlaskForm):
	name = StringField("Item name", [validators.Length(min=2, max=25), validators.InputRequired(), hasWhitespace])
	colorcode = StringField("Item colorcode", [validators.Length(min=2, max=25), validators.InputRequired(), hasWhitespace])
	ptype = QuerySelectField(u'Item ptype', query_factory = Ptype.ptype_list, get_label='name')

	class Meta:
		csrf = False


class PersonalItemForm(FlaskForm):
	colorcode = QuerySelectField(u'Item colorcode', query_factory = Colorcode.colorcode_list, get_label='code')
	ptype = QuerySelectField(u'Item type', query_factory = Ptype.ptype_list, get_label='name')

	class Meta:
		csrf = False


