import unittest
from myprj.basic.calculator import Calculator


class TestCalculator(unittest.TestCase):
    def test_add(self):
        # Setup
        cal = Calculator()
        expected_result = 9

        # Action
        actual_result = cal.add(1, 3, 5)

        # Assert
        self.assertEqual(expected_result, actual_result)

    def test_add_for_two(self):
        # Setup
        cal = Calculator()
        expected_result = 13

        # Action
        actual_result = cal.add(1, 2, 5)

        # Assert
        self.assertEqual(expected_result, actual_result)
