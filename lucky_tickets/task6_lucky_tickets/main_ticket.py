# !/usr/bin/env python

""""
Lucky tickets

There are 2 ways to calculate lucky tickets:
1. Moscow - if a six-figure number is printed on a bus ticket,
and the sum of the first three digits is equal to the sum
the last three, then this ticket is considered happy.
2. Leningrad - if the sum of even numbers of the ticket is
equal to the sum of odd figures of the ticket,
then the ticket is considered happy.
A task:
Ticket number is a six-digit number. You need to write a
console application that can calculate the number of happy
tickets. To select a counting algorithm, a text file is read.
The path to the text file is set in the console after
start the program. Algorithm indicators:
1 - the word 'Moskow'
2 - the word 'Piter'
After setting all the necessary parameters, the program in
the console should output the number of happy
tickets for the specified method of calculation
"""


import sys
from ticket import tickets_list, lucky_Moskow_tickets, lucky_Piter_tickets
from validation_argv_ticket import is_validation_argv


def lucky_tickets():
    if not is_validation_argv():
        print('Restart and enter the correct data for processing: \n '
              '<path to the indicator file> ')
        quit()

    file_name = sys.argv[1]

    tickets = tickets_list()
    for line in open(file_name):
        if 'Moskow' in line:
            Moskow_tickets = lucky_Moskow_tickets(tickets)
            print('According to the Moscow method of counting {} '
                  'a lucky tickets '.format(Moskow_tickets))
        elif 'Piter' in line:
            Piter_tickets = lucky_Piter_tickets(tickets)
            print('According to the Petersburg method of counting {} '
                  'a lucky tickets '.format(Piter_tickets))


if __name__ == '__main__':
    lucky_tickets()
