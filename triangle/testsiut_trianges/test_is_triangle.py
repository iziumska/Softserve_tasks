from unittest import TestCase
from triangle.task3_triangles.validation_triangles \
    import is_triangle


class TestIs_triangle(TestCase):
    def test_is_not_triangle(self):
        list_data = [[1, 2, 3], [1, 3, 2], [3, 1, 2]]
        for data in list_data:
            actual_result = is_triangle(*data)
            self.assertFalse(actual_result)

    def test_is_triangle(self):
        list_data = [[5, 5, 5], [5, 3, 3], [3, 3, 2]]
        for data in list_data:
            actual_result = is_triangle(*data)
            self.assertTrue(actual_result)
