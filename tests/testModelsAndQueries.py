from unittest import TestCase
from app import create_app, db
from app.models import Book, Category

class TestModelsAndQueries(TestCase):
	def setUp(self):
		self.app = create_app('testing')
		self.app_context = self.app.app_context()
		self.app_context.push()
		db.create_all()

	def tearDown(self):
		db.drop_all()
		self.app_context.pop()

	def testBookObjectsCanBeCreated(self):
		book = Book(name='Clean Code', author='Uncle Bob')
		db.session.add(book)
		self.assertIsNone(book.id)
		db.session.commit()
		self.assertIsNotNone(book.id)

	def testCategoryObjectsCanBeCreated(self):
		category = Category(name='tech')
		db.session.add(category)
		self.assertIsNone(category.id)
		db.session.commit()
		self.assertIsNotNone(category.id)

	def testCanSearchByBookName(self):
		book = Book(name='Clean Code', author='Uncle Bob')
		db.session.add(book)
		db.session.commit()
		book = Book.query.filter_by(name='Clean Code').all()[0]
		self.assertEquals(book.name, 'Clean Code')

	def testCanFindBooksInCategory(self):
		tech = Category(name='tech')
		book = Book(name='Clean Code', category=tech)
		book2 = Book(name='Eloquent JavaScript', category=tech)
		db.session.add_all([book, book2, tech])
		db.session.commit()
		books = Book.query.filter_by(category=tech).all()
		self.assertIsNotNone(books)






