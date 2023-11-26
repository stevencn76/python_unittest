import pytest

from myprj.basic.calculator import Calculator


@pytest.mark.parametrize("num, expected_out", [(1, True), (2, False)])
def test_is_odd(num, expected_out):
    # Setup
    cal = Calculator()

    # Action
    actual_result = cal.is_odd(num)

    # Assert
    assert actual_result == expected_out
