import sys
import pytest
from myprj.domain.student import Student


def is_skip():
    return sys.platform.casefold() == "linux".casefold()


# @pytest.mark.skip(reason="expired")
@pytest.mark.skipif(condition=is_skip(), reason="skip on macos")
def test_student():
    print("testing student __init__")
    # Action
    student = Student(id=1, name="Jack")

    # Assert
    assert student.id == 1
    assert student.name == "Jack"


class TestStudent:
    def test_student(self):
        # Action
        student = Student(id=1, name="Jack")

        # Assert
        assert student.id == 1
        assert student.name == "Jack"
