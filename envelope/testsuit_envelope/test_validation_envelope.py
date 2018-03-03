from unittest import TestCase
from envelope.task2_envelope.validation_envelope import \
    is_valid_value


class TestValidation(TestCase):
    def test_validation_negative_value(self):
        test_list_value = [-1, -5]
        for value in test_list_value:
            actual_result = is_valid_value(value)
            self.assertFalse(actual_result)

    def test_validation_zero_value(self):
        value = 0
        actual_result = is_valid_value(value)
        self.assertFalse(actual_result)

    def test_validation_positive_value(self):
        test_list_value = [1, 111]
        for value in test_list_value:
            actual_result = is_valid_value(value)
            self.assertTrue(actual_result)
