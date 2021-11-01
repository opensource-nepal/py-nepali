import datetime
import unittest

from nepali.datetime import nepalidate


class TestNepaliDateTime(unittest.TestCase):
    '''
    TODO:
        - nepalidate year, month, day, weekDay test
        - nepalidate strftime
        - nepalitime now vs datetime.time.now
        - nepalidatetime from_datetime vs to_datetime
        - nepalidatetime date vs from_date
        - nepalidatetime strftime
        - nepalidatetime from_datetime vs from_nepalidatetime
        - nepalidatetime timedelta
    '''
    def setUp(self):
        pass

    #
    # nepali date

    def test_nepalidate_now_and_today(self):
        today = nepalidate.today()
        now = nepalidate.now()
        self.assertEqual(today, now, msg='nepalidate today is not equals to now.')

    def test_nepalidate_comparision(self):
        nepalidate_obj1 = nepalidate(year=2051, month=4, day=28)

        # test equal date
        nepalidate_obj2 = nepalidate(year=2051, month=4, day=28)
        self.assertEqual(nepalidate_obj1, nepalidate_obj2, 'Same nepali date are not checked equals.')

        # test different date
        nepalidate_obj3 = nepalidate(year=2051, month=4, day=29)
        self.assertNotEqual(nepalidate_obj1, nepalidate_obj3, 'Different nepali date are checked as equal.')

        # TODO: check other comparisions (later)

    def test_nepalidate_year_month_day(self):
        nepalidate_obj = nepalidate(year=2051, month=4, day=28)
        self.assertEqual(nepalidate_obj.year, 2051)
        self.assertEqual(nepalidate_obj.month, 4)
        self.assertEqual(nepalidate_obj.day, 28)
        self.assertEqual(nepalidate_obj.weekday(), 4)

    def test_nepalidate_from_date(self):
        python_date_obj = datetime.date(year=1994, month=8, day=12)
        nepalidate_obj = nepalidate.from_date(python_date_obj)
        self.assertEqual(python_date_obj, nepalidate_obj.to_date(), 'nepalidate from_date and to_date are not equal.')

    def test_nepalidate_from_datetime(self):
        python_datetime_obj = datetime.datetime(year=1994, month=8, day=12, hour=4, minute=8, second=12)
        nepalidate_obj = nepalidate.from_datetime(python_datetime_obj)
        self.assertEqual(python_datetime_obj.date(), nepalidate_obj.to_date(), 'nepalidate from_datetime and to_datetime are not equal.')

    def test_nepalidate_strftime(self):
        nepalidate_obj = nepalidate(year=2051, month=4, day=28)
        self.assertEqual(nepalidate_obj.strftime('%Y-%m-%d'), '२०५१-०४-२८')
        self.assertEqual(nepalidate_obj.strftime_en('%Y-%m-%d'), '2051-04-28')

