import unittest

from budget_2024.budget.routes import app
import unittest

class MyFlaskTest(unittest.TestCase):

    def setUp(self):
        self.app = app(test_config=True)
        self.client = self.app.test_client()
        self.ctx = self.app.app_context()
        self.ctx.push()

    def tearDown(self):
        self.ctx.pop()
