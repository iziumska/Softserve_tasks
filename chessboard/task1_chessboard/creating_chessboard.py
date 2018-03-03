#!/usr/bin/python3


"""
Creating a chessboard

Program 'Chessboard'
Displays the chess board with the given width and height parameters.
The program is run through a call to a public class with the parameters.

"""


from chess_board import drawing_chess_board, output_chess_board
from validation_chessboard_arg import is_validation_chessboard_arg


def creating_chessboard():
    try:
        height = int(input('Enter value for height - '))
        width = int(input('Enter value for width - '))
        if is_validation_chessboard_arg(height, width):
            user_chess_board = drawing_chess_board(height, width)
            output_chess_board(user_chess_board)
        else:
            print('You entered not a positive number. Restart and '
                  'enter positive numerical values for the height and '
                  'width of the chessboard that you draw')
    except ValueError:
        print('You entered not a number. Restart and enter positive '
              'numerical values for the height and '
              'width of the chessboard that you draw')


if __name__ == "__main__":
    creating_chessboard()
