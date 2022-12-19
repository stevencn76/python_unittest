import unittest
from unittest.mock import Mock

from myprj.service import student_service


class TestStudentService(unittest.TestCase):

    def test_change_name_with_record(self):
        # Setup
        student_service.find_student_by_id = Mock()
        student = Mock(id=1, name='Tom')
        student_service.find_student_by_id.return_value = student

        student_service.save_student = Mock()

        # Action
        student_service.change_name(1, 'Jack')


        # Assert
        self.assertEqual('Jack', student.name)
        student_service.save_student.assert_called()

    def test_change_name_without_record(self):
        # Setup
        student_service.find_student_by_id = Mock()
        student_service.find_student_by_id.return_value = None

        student_service.save_student = Mock()

        # Action
        student_service.change_name(1, 'Jack')

        # Assert
        student_service.save_student.assert_not_called()
