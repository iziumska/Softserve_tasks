import sys
from unittest import TestCase
from numbers.task7_numbers.validation_numbers import is_validation_numbers


class TestValidation_numbers(TestCase):
    def test_not_completeness_of_data(self):
        list_argv = [[], [1], [1, 2, 3, 4, 5]]
        for sys.argv in list_argv:
            actual_result = is_validation_numbers()
            self.assertFalse(actual_result)

    def test_completeness_of_data(self):
        sys.argv = [1, 2]
        actual_result = is_validation_numbers()
        self.assertTrue(actual_result)

    def test_zero_negative_value_of_data(self):
        list_argv = [[1, 0], [1, -10]]
        for sys.argv in list_argv:
            actual_result = is_validation_numbers()
            self.assertFalse(actual_result)

    def test_positive_value_of_data(self):
        sys.argv = [1, 10]
        actual_result = is_validation_numbers()
        self.assertTrue(actual_result)
