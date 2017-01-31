from . import main
from flask import render_template
from .forms import BookSearchForm, CatgorySearchForm
from ..models import Book, Category


@main.route('/', methods=['GET', 'POST'])
def index():
	form = BookSearchForm()
	books = None

	if form.validate_on_submit():
		name = form.name.data
		books = Book.query.filter(Book.name.like(name+'%')).all()
	return render_template('index.html', form  = form, books = books)

@main.route('/category', methods=['GET', 'POST'])
def category():
	form = CatgorySearchForm()
	books = None

	if form.validate_on_submit():
		category_name = form.name.data
		category = Category.query.filter_by(name=category_name).first()
		books = Book.query.filter_by(category = category).all()
	return render_template('category.html', form  = form, books = books)

@main.route('/profile/<name>')
def profile(name):
	return 'Hello %s %s' %name
