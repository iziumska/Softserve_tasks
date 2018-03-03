#!/usr/bin/python3

"""
5. The number into word
It is necessary to convert the whole number into a capital variant:
12 - twelve. The program is launched via the main class call with
parameters.
"""

from number_to_word import number_to_word
from validation_argv_number import is_valid_number


def main():
    try:
        user_number = int(input('Enter a number from -999 to 999 for '
                                'converting to word: '))
    except ValueError:
        print('You did not enter a number. Restart and enter a number '
              'from -999 to 999 for converting to word')
        quit()

    if is_valid_number(user_number):
        result = number_to_word(user_number)
        print(result)
    else:
        print('You enter a number that bigger than 999 or less than -999. '
              'Restart and enter a number from -999 to 999 '
              'for converting to word')
        quit()


if __name__ == '__main__':
    main()
