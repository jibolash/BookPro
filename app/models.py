from . import db

class Book(db.Model):
	__tablename__ = 'books'
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String)
	author = db.Column(db.String)
	category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))

	def __repr__(self):
		return '<Book %r>' %self.name

class Category(db.Model):
	__tablename__ = 'categories'
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String)
	books = db.relationship('Book', backref='category', lazy='dynamic')

	def __repr__(self):
		return '<Category %r>' %self.name

