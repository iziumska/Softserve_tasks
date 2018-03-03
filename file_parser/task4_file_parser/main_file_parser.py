# !/usr/bin/env python

"""
File parser

The program operates in two modes:
1. Reads the number of occurrences of a string in a text file.
2. Makes changing a string to another in the specified file
The program accepts input arguments at startup:
1. <path to file> <string for counting>
2. <path to file> <string to search> <string to replace>
"""


import sys
from validation_argv_file import is_validation_argv
from work_with_file import counting_string, replace_string


def main():
    if not is_validation_argv():
        print('Enter the correct data for processing:\n'
              '<path to file> <string for counting> or <path '
              'to file> <string to search> <string to replace>')
        quit()

    file_name = sys.argv[1]
    sourse_text = sys.argv[2]

    if len(sys.argv) == 3:
        counting_string(file_name, sourse_text)
    elif len(sys.argv) == 4:
        replace_text = sys.argv[3]
        replace_string(file_name, sourse_text, replace_text)


if __name__ == '__main__':
    main()
