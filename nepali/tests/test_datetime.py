import datetime
import unittest

from nepali.datetime import nepalidate


class TestNepaliDateTime(unittest.TestCase):

    def setUp(self):
        self.nepali_datetime = nepalidate.today()

    def test_todays_date(self):
        todays_date = nepalidate.today()
        self.assertEqual(todays_date, self.nepali_datetime)

    def test_date_conversion(self):
        self.assertEqual(datetime.date.today(), nepalidate.today(), msg='Today\'s date is not matching.')

