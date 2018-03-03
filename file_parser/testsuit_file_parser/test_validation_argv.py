import sys
from unittest import TestCase
from file_parser.task4_file_parser.validation_argv_file\
    import is_validation_argv


class TestValidation_argv(TestCase):
    def test_not_completeness_data(self):
        list_argv = [[], [1], [1, 2], [1, 2, 3, 4, 5]]
        for sys.argv in list_argv:
            actual_result = is_validation_argv()
            self.assertFalse(actual_result)

    def test_completeness_data(self):
        list_argv = [[1, 2, 3], [1, 2, 3, 4]]
        for sys.argv in list_argv:
            actual_result = is_validation_argv()
            self.assertTrue(actual_result)
