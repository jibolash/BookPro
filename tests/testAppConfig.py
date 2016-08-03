from unittest import TestCase
from app import create_app
from flask import current_app

class TestAppConfig(TestCase):
	def setUp(self):
		self.app = create_app('testing')
		self.app_context = self.app.app_context()
		self.app_context.push()

	def tearDown(self):
		self.app_context.pop()

	def testAppExists(self):
		self.assertFalse(current_app is None)

	def testAppConfigIsTesting(self):
		self.assertTrue(self.app.config['TESTING'])