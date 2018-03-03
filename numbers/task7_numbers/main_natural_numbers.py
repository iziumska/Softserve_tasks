# !/usr/bin/env python

"""
Numerical sequence

The program displays a series of natural numbers separated
by a comma, the square of which is less than the given
number n. The program is launched via the main class call
with parameters.
"""

import sys
from numerical_sequence import natural_number
from validation_numbers import is_validation_numbers


def main():
    try:
        if is_validation_numbers():
            max_number = int(sys.argv[1])
            user_list = natural_number(max_number)
            print(user_list)
        else:
            print('You must enter one positive number. '
                  'Restart and enter, please')
    except ValueError:
        print('You entered not a number. Restart and '
              'enter one positive number, please')


if __name__ == '__main__':
    main()
