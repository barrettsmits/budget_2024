import unittest
from unittest.mock import patch
from budget.calc import Sums

class SumsTestCase(unittest.TestCase):
    # @patch('calc.Expense')
    # def test_total_expenses(self, mock_expense):
    #     mock_expense.query.with_entities.return_value.scalar.return_value = 100
    #     result = Sums.total('expenses')
    #     self.assertEqual(result, 100)

    @patch('calc.Income')
    def test_total_incomes(self, mock_income):
        mock_income.query.with_entities.return_value.scalar.return_value = 200
        result = Sums.total('incomes')
        self.assertEqual(result, 200)

    # @patch('calc.Investments')
    # def test_total_investments(self, mock_investments):
    #     mock_investments.query.with_entities.return_value.scalar.return_value = 300
    #     result = Sums.total('investments')
    #     self.assertEqual(result, 300)

    # @patch('calc.Assets')
    # def test_total_assets(self, mock_assets):
    #     mock_assets.query.with_entities.return_value.scalar.return_value = 400
    #     result = Sums.total('assets')
    #     self.assertEqual(result, 400)

    # @patch('calc.Withholdings')
    # def test_total_withholdings(self, mock_withholdings):
    #     mock_withholdings.query.with_entities.return_value.scalar.return_value = 500
    #     result = Sums.total('withholdings')
    #     self.assertEqual(result, 500)

    @patch('calc.Sums.total')
    def test_balance(self, mock_total):
        mock_total.side_effect = [1000, 2000, 3000, 4000, 5000]
        result = Sums.balance()
        self.assertEqual(result, -1000)

if __name__ == '__main__':
    unittest.main()