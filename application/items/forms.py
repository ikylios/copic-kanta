from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, validators, SelectField
from wtforms.ext.sqlalchemy.fields import QuerySelectField

from application.ptype.models import Ptype
from application.colorcode.models import Colorcode

class ItemForm(FlaskForm):
	name = StringField("Item name", [validators.Length(min=3)])
	colorcode = StringField("Item colorcode", [validators.Length(min=3)])
	ptype = QuerySelectField(u'Item ptype', query_factory = Ptype.ptype_list, get_label='name')

	class Meta:
		csrf = False


class PersonalItemForm(FlaskForm):
	colorcode = QuerySelectField(u'Item colorcode', query_factory = Colorcode.colorcode_list, get_label='code')
	ptype = QuerySelectField(u'Item type', query_factory = Ptype.ptype_list, get_label='name')

	class Meta:
		csrf = False


