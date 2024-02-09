import unittest
from budget.models import Withholdings

class WithholdingsTestCase(unittest.TestCase):
    def test_withholdings_attributes(self):
        withholding = Withholdings(amount=500, description='Tax', frequency='Monthly')
        self.assertEqual(withholding.amount, 500)
        self.assertEqual(withholding.description, 'Tax')
        self.assertEqual(withholding.frequency, 'Monthly')

if __name__ == '__main__':
    unittest.main()