import pytest

from myprj.domain.student import Student


class TestStudent:
    @pytest.fixture
    def valid_student(self):
        student = Student(id=1, name="Mary")
        # print("11111")
        yield student
        # print("22222")

    @pytest.fixture
    def invalid_student_1(self, valid_student):
        valid_student.name = "lasdfjkalsfkdjsalf"

        yield valid_student

    def test_rename_false(self, valid_student):
        # Setup
        new_name = "alsdkfjaslfkjaslfkd"
        expected_result = False

        # Action
        actual_result = valid_student.rename(new_name)

        # Assert
        assert actual_result == expected_result

    def test_valid_name_false(self, invalid_student_1):
        # Setup
        expected_result = False

        # Action
        actual_result = invalid_student_1.valid_name()

        # Assert
        assert actual_result == expected_result

    def test_valid_gender_true(self, male_student_fixture, female_student_fixture):
        # Setup
        expected_result = True

        # Action
        actual_result1 = male_student_fixture.valid_gender()
        actual_result2 = female_student_fixture.valid_gender()

        # Assert
        assert actual_result1 == expected_result
        assert actual_result2 == expected_result
