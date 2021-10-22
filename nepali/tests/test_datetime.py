import unittest

from nepali.datetime import nepalidate


class TestNepaliDateTime(unittest.TestCase):

    def setUp(self):
        self.nepali_datetime = nepalidate()

    def test_todays_date(self):
        todays_date = nepalidate.today()
        self.assertEqual(todays_date, self.nepali_datetime)

