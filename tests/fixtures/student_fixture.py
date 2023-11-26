import pytest

from myprj.domain.student import Student


@pytest.fixture
def male_student_fixture():
    male_student = Student(id=1, name="Jack")
    male_student.gender = "male"

    yield male_student
