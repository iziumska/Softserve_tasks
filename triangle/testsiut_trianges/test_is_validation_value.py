from unittest import TestCase
from triangle.task3_triangles.validation_triangles \
    import is_validation_value


class TestIs_validation_value(TestCase):
    def test_is_not_valid_value(self):
        list_data = [['tt', 0, -4, 6], ['u1', -9, 7, 2],
                     ['1', 0, 'er', 7], ['?', 7, 7, 7]]
        for data in list_data:
            actual_result = is_validation_value(data)
            self.assertFalse(actual_result)

    def test_is_valid_value(self):
        data = ['tt', 4, 4, 6]
        actual_result = is_validation_value(data)
        self.assertTrue(actual_result)
