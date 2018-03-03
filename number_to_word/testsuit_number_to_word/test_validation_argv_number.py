from unittest import TestCase
from number_to_word.task5_number_to_word.validation_argv_number \
    import is_valid_number


class TestValidation_number(TestCase):
    def test_not_valid_number(self):
        list_data = [1000, -1000]
        for data in list_data:
            actual_result = is_valid_number(data)
            self.assertFalse(actual_result)

    def test_valid_number(self):
        list_data = [999, 0, -999]
        for data in list_data:
            actual_result = is_valid_number(data)
            self.assertTrue(actual_result)
