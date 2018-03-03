from unittest import TestCase
from lucky_tickets.task6_lucky_tickets.ticket import tickets_list, \
    lucky_Moskow_tickets, lucky_Piter_tickets

expected_sum = 55252


class TestTicket(TestCase):
    def test_main_list(self):
        expected_result = 1000000
        actual_result = len(tickets_list())
        self.assertEqual(expected_result, actual_result)

    def test_equal_sums_Moskow(self):
        actual_sum = lucky_Moskow_tickets(tickets_list())
        self.assertEqual(expected_sum, actual_sum)

    def test_equal_sums_Piter(self):
        actual_sum = lucky_Piter_tickets(tickets_list())
        self.assertEqual(expected_sum, actual_sum)
