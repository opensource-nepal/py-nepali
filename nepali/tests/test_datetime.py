import unittest

from nepali.datetime import NepaliDate, nepalidate


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
        self.nepali_datetime = nepalidate()

    def test_todays_date(self):
        todays_date = nepalidate.today()
        self.assertEqual(todays_date, self.nepali_datetime)

