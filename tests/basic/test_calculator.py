import unittest

from parameterized import parameterized

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

    @parameterized.expand([[1, True], [2, False]])
    def test_is_odd(self, num, expected_out):
        # Setup
        cal = Calculator()

        # Action
        actual_result = cal.is_odd(num)

        # Assert
        assert actual_result == expected_out
