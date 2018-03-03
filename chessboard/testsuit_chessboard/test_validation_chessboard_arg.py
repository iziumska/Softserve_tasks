from unittest import TestCase
from chessboard.task1_chessboard.validation_chessboard_arg import \
    is_validation_chessboard_arg


class TestValidation_arg(TestCase):
    def test_not_valid_arg(self):
        # check for zero and negative data
        list_argv = [[-1, 5], [0, 4], [0, 0]]
        for argv in list_argv:
            actual_result = is_validation_chessboard_arg(*argv)
            self.assertFalse(actual_result)

    def test_valid_arg(self):
        # check for positive data
        list_argv = [[1, 1], [5, 4], [10, 4]]
        for argv in list_argv:
            actual_result = is_validation_chessboard_arg(*argv)
            self.assertTrue(actual_result)
