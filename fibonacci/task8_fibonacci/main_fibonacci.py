# !/usr/bin/env python

"""
Fibonacci numbers

The program allows you to output all Fibonacci numbers that are in the
specified range. The range is specified by two arguments when the main
class is called. Numbers are separated by commas.

"""

import sys
from fibonacci.task8_fibonacci.fibonacci import \
    creating_user_fibonacci_list, print_out_user_list


def is_validation_data(user_fibonacci_list):
    def user_numbers():
        try:
            return user_fibonacci_list() if (len(sys.argv) == 3) and \
                                            (int(sys.argv[1]) > 0) and \
                                            (int(sys.argv[2]) > 0) else \
                print('You entered not valuable date. Restart and enter two '
                      'positive numbers (start and end)')

        except ValueError:
            print('You entered not a number.Restart and enter two positive '
                  'numbers (start and end)')
    return user_numbers


@is_validation_data
def user_fibonacci_list():
    start = int(sys.argv[1])
    end = int(sys.argv[2])

    if start > end:
        start, end = end, start

    user_list = creating_user_fibonacci_list(start, end)
    print_out_user_list(start, end, user_list)
    return user_list


if __name__ == '__main__':
    user_fibonacci_list()
