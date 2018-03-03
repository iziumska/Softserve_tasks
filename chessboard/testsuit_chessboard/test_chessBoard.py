from unittest import TestCase
from chessboard.task1_chessboard.chess_board import drawing_chess_board


class TestChessBoard(TestCase):
    def test_drawing_chess_board(self):
        actual_result = drawing_chess_board(3, 5)
        expected_result = [' ', chr(9608)]
        self.assertEqual(expected_result, actual_result[0][:2])
