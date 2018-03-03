from unittest import TestCase
from number_to_word.task5_number_to_word.number_to_word \
    import number_to_word


class TestNumber_to_word(TestCase):
    def test_null_to_word(self):
        actual_result = number_to_word(0)
        expected_result = 'ноль'
        self.assertEqual(actual_result, expected_result)

    def test_positive_number_to_word(self):
        actual_result = number_to_word(66)
        expected_result = 'шестьдесят шесть'
        self.assertEqual(actual_result, expected_result)

    def test_negative_number_to_word(self):
        actual_result = number_to_word(-66)
        expected_result = 'минус шестьдесят шесть'
        self.assertEqual(actual_result, expected_result)
