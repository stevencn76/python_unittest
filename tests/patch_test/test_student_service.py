import unittest
from unittest.mock import patch, Mock
from myprj.service import student_service


class TestStudentService(unittest.TestCase):

    @patch("myprj.service.student_service.save_student")
    @patch("myprj.service.student_service.find_student_by_id")
    def test_change_name_decorator(self, find_student_mock, save_student_mock):
        # Setup
        student = Mock(id=1, name='Jack')
        find_student_mock.return_value = student

        # Action
        student_service.change_name(1, 'Tom')

        # Assert
        self.assertEqual('Tom', student.name)

    def test_change_name_contextmanager(self):
        # Setup
        student = Mock(id=1, name='Jack')

        with patch("myprj.service.student_service.find_student_by_id") \
                as find_student_mock, \
                patch("myprj.service.student_service.save_student"):
            find_student_mock.return_value = student

            # Action
            student_service.change_name(1, 'Tom')

        # Assert
        self.assertEqual('Tom', student.name)

    @patch("myprj.service.student_service.find_student_by_id")
    def test_change_name_manual(self, find_student_mock):
        # Setup
        student = Mock(id=1, name='Jack')
        find_student_mock.return_value = student

        patcher = patch("myprj.service.student_service.save_student")
        patcher.start()

        # Action
        student_service.change_name(1, 'Tom')

        patcher.stop()

        # Assert
        self.assertEqual('Tom', student.name)
