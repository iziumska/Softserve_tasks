#!/usr/bin/python3


"""
Comparison of envelopes

There are two envelopes with sides (a, b) and (c, d) to determine
whether one envelope can be put in another.
The program must handle the input of floating-point numbers. The
program asks the user for the dimensions envelopes one parameter at
a time. After each count, the program asks the user whether
he continued. If the user answers "y" or "yes" (not case sensitive),
the program continues to work first, otherwise - completes the execution.
"""

from envelope import Envelope
from validation_envelope import is_valid_value


warning = "You entered a non positive number. Let's try again? "


def main():
    answer = 'y'
    print('Date for envelope ...')
    while answer in ('y', 'yes'):
        envelope1 = make_envelope()
        envelope2 = make_envelope()

        if envelope1 == envelope2:
            print('Envelopes are equal. Dimensions of the contours do not '
                  'allow to put one into the other')
        elif envelope1 > envelope2:
            print('You can put the second envelope in the first one')
        elif envelope1 < envelope2:
            print('The first envelope can be put in the second one')

        answer = (input('Compare again? ')).lower()
    print('Have a nice day!')


def make_envelope():
    restart = 'y'
    while restart in ('y', 'yes'):
        try:
            width = float(input('Width for envelope  = '))
            if is_valid_value(width):
                height = float(input('Height for envelope = '))
                if is_valid_value(height):
                    envelope = Envelope(width, height)
                    print('Date for second envelope...')
                    return envelope
                else:
                    restart = input(warning)
            else:
                restart = input(warning)
        except ValueError:
            restart = input("You entered not a number.Let's try again? ")
    print('The end')
    quit()


if __name__ == '__main__':
    main()
