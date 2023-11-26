import pytest

from myprj.domain.student import Student
from tests.fixtures.male_student_fixture import male_student_fixture


@pytest.fixture
def female_student_fixture():
    student = Student(id=2, name="Mary")
    yield student
