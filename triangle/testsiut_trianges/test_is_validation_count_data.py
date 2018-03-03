from unittest import TestCase
from triangle.task3_triangles.validation_triangles \
    import is_validation_count_data


class TestIs_validation_count_data(TestCase):
    def test_not_completeness_data(self):
        list_data = [[], [1], [1, 2], [1, 2, 3], [1, 2, 3, 4, 5]]
        for data in list_data:
            actual_result = is_validation_count_data(data)
            self.assertFalse(actual_result)

    def test_completeness_data(self):
        data = [1, 2, 3, 4]
        actual_result = is_validation_count_data(data)
        self.assertTrue(actual_result)
