from unittest import TestCase
from triangle.task3_triangles.traingle import Triangle


class TestTriangle(TestCase):
    def test_calculation_perimeter(self):
        test_triangle = Triangle(5, 5, 5, 5)
        actual_result = test_triangle.calculation_perimeter_triangle()
        expected_result = 15
        self.assertEqual(actual_result, expected_result)

    def test_calculation_square(self):
        test_triangle2 = Triangle(6, 6, 6, 6)
        test_triangle2.perimeter = \
            test_triangle2.calculation_perimeter_triangle()
        actual_result = test_triangle2.calculation_square_triangle()
        expected_result = 15.59
        self.assertEqual(actual_result, expected_result)
