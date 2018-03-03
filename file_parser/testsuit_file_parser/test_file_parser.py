from unittest import TestCase
from file_parser.task4_file_parser.work_with_file \
    import counting_string, replace_string


class TestFile(TestCase):
    def test_counting_string(self):
        actual_result = counting_string('text2.txt', 'aaa')
        expected_result = 1
        self.assertEqual(expected_result, actual_result)

    def test_replace_string(self):

        temp2 = replace_string('text2.txt', 'vaw', 'abc')
        self.assertEqual('abc', temp2)
        temp3 = replace_string('text2.txt', 'abc', 'vaw')
        self.assertEqual('vaw', temp3)
