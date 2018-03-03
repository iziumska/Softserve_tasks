from unittest import TestCase
from numbers.task7_numbers.numerical_sequence import natural_number


class TestNumerical_sequence(TestCase):
    def test_natural_number_list(self):
        expected_result = [1, 2, 3, 4, 5, 6, 7]
        actual_result = natural_number(50)
        self.assertListEqual(expected_result, actual_result)

    def test_not_list(self):
        expected_result = [1, 2, 3, 6, 7]
        actual_result = natural_number(50)
        self.assertNotEqual(expected_result, actual_result)
