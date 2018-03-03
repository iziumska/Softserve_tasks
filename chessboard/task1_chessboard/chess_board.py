#!/usr/bin/python3


def drawing_chess_board(height, width):
    chess_board = [[chr(9608)] * width for _ in range(height)]
    for i in range(height):
        for j in range(width):
            if (i+j) % 2 == 0:
                chess_board[i][j] = ' '
    return chess_board


def output_chess_board(chess_board):
    print()
    for row in chess_board:
        print(' '.join([elem for elem in row]))
