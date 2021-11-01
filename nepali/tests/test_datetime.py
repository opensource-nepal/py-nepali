import datetime
import unittest

from nepali.datetime import nepalidate


class TestNepaliDateTime(unittest.TestCase):
    '''
    TODO:
        - nepalidate now vs today
        - nepalidate from_date
        - nepalidate from_nepalidatetime
        - nepalidate year, month, day, weekDay test
        - nepalitime now vs datetime.time.now
        - nepalidatetime from_datetime vs to_datetime
        - nepalidatetime date vs from_date
        - nepalidatetime strftime
        - nepalidatetime from_datetime vs from_nepalidatetime
    '''
    def setUp(self):
        self.nepali_datetime = nepalidate.today()

    def test_todays_date(self):
        todays_date = nepalidate.today()
        self.assertEqual(todays_date, self.nepali_datetime)

    def test_date_conversion(self):
        self.assertEqual(datetime.date.today(), nepalidate.today(), msg='Today\'s date is not matching.')

