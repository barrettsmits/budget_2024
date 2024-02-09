import os
import unittest
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from budget.app import create_app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()
        self.db = SQLAlchemy(self.app)
        self.db.create_all()

    def tearDown(self):
        self.db.session.remove()
        self.db.drop_all()
        self.app_context.pop()

    def test_create_app_development(self):
        os.environ['FLASK_ENV'] = 'development'
        app = create_app()
        self.assertEqual(app.config['ENV'], 'development')

    # def test_create_app_production(self):
    #     os.environ['FLASK_ENV'] = 'production'
    #     app = create_app()
    #     self.assertEqual(app.config['ENV'], 'production')

    def test_create_app_testing(self):
        os.environ['FLASK_ENV'] = 'testing'
        app = create_app()
        self.assertEqual(app.config['ENV'], 'testing')

if __name__ == '__main__':
    unittest.main()