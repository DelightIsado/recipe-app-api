"""
Sample tests
"""
from django.test import SimpleTestCase

from app import cal


class CalTests(SimpleTestCase):
    """ Test the cal module. """

    def test_add_numbers(self):
        """Test adding numbers together"""
        res = cal.add(5, 6)

        self.assertEqual(res, 11)

    def test_subtract_numbers(self):
        """Test subtracting numbers together """
        res = cal.subtract(29, 17)

        self.assertEqual(res, 12)
