import sys
from unittest import TestCase
from lucky_tickets.task6_lucky_tickets.validation_argv_ticket \
    import is_validation_argv


class TestValidation_argv(TestCase):
    def test_not_completeness_of_data(self):
        list_argv = [[], [1], [1, 2, 3, 4, 5]]
        for sys.argv in list_argv:
            actual_result = is_validation_argv()
            self.assertFalse(actual_result)

    def test_completeness_of_data(self):
        sys.argv = [1, 2]
        actual_result = is_validation_argv()
        self.assertTrue(actual_result)
