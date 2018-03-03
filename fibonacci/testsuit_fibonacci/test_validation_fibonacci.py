import sys
from unittest import TestCase
from fibonacci.task8_fibonacci.main_fibonacci import user_fibonacci_list


class TestValidation_fibonacci(TestCase):
    def test_not_valid_data(self):
        list_argv = [[], [0], [1, -2, 3], [0, 4], [0, 4, 5, 6], [1, 'g', 8]]
        for sys.argv in list_argv:
            actual_result = user_fibonacci_list()
            self.assertIsNone(actual_result)

    def test_valid_data(self):
        sys.argv = [1, 2, 3]
        actual_result = user_fibonacci_list()
        expected_result = [2, 3]
        self.assertEqual(actual_result, expected_result)
