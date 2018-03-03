from unittest import TestCase
from fibonacci.task8_fibonacci.fibonacci import creating_user_fibonacci_list


class TestFibonacci(TestCase):
    def test_user_fibonacci_list(self):
        actual_result = creating_user_fibonacci_list(1, 10)
        expected_result = [1, 1, 2, 3, 5, 8]
        self.assertListEqual(actual_result, expected_result)
