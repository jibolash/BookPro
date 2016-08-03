from flask_wtf import Form
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import Required

class BookSearchForm(Form):
	name = StringField('Enter book name', validators=[Required()])
	submit = SubmitField('Find Book')

class CatgorySearchForm(Form):
	name = SelectField('Select a category', choices=[('History', 'History'), ('Politics', 'Politics'), ('Fiction', 'Fiction'), ('tech', 'tech')])
	submit = SubmitField('Find books in category')
