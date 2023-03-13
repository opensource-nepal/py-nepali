import datetime
import unittest

from nepali.datetime import nepalidate, nepalitime, nepalidatetime
from nepali.datetime.utils import to_nepalidatetime, to_nepalidate
from nepali.exceptions import InvalidNepaliDateTimeObjectException
from nepali.timezone import NepaliTimeZone


class TestNepaliDateTime(unittest.TestCase):
    #
    # nepalidate

    def test_nepalidate_now_and_today(self):
        today = nepalidate.today()
        now = nepalidate.now()
        self.assertEqual(today, now, msg="nepalidate today is not equals to now.")

    def test_nepalidate_comparison(self):
        nepalidate_obj1 = nepalidate(year=2051, month=4, day=28)

        # test equal date
        nepalidate_obj2 = nepalidate(year=2051, month=4, day=28)
        self.assertEqual(
            nepalidate_obj1, nepalidate_obj2, "Same nepali date are not checked equals."
        )

        # test different date
        nepalidate_obj3 = nepalidate(year=2051, month=4, day=29)
        self.assertNotEqual(
            nepalidate_obj1,
            nepalidate_obj3,
            "Different nepali date are checked as equal.",
        )

        #
        # test addition

        # test with timedelta
        nt = nepalidate(year=2051, month=4, day=29)
        nt = nt + datetime.timedelta(days=1)
        self.assertEqual((nt.year, nt.month, nt.day), (2051, 4, 30))

        # test without timedelta
        with self.assertRaises(TypeError):
            nt = nt + 1

        #
        # test subtraction

        # test with nepali date
        td = nepalidate(year=2051, month=4, day=30) - nepalidate(
            year=2051, month=4, day=29
        )
        self.assertEqual(td.days, 1)

        # test with python date
        td = nepalidate(year=2051, month=4, day=30) - datetime.date(
            year=1994, month=8, day=13
        )
        self.assertEqual(td.days, 1)

        # test with timedelta
        nt = nepalidate(year=2051, month=4, day=30) - datetime.timedelta(days=1)
        self.assertEqual((nt.year, nt.month, nt.day), (2051, 4, 29))

        # test without timedelta
        with self.assertRaises(TypeError):
            nt = nt - 1

        #
        # test less than
        self.assertEqual(nepalidate(2051, 4, 29) < nepalidate(2051, 4, 30), True)
        self.assertEqual(nepalidate(2051, 4, 29) < nepalidate(2051, 4, 29), False)
        self.assertEqual(nepalidate(2051, 4, 29) < datetime.date(1994, 8, 14), True)
        self.assertEqual(nepalidate(2051, 4, 29) < datetime.date(1994, 8, 13), False)
        with self.assertRaises(TypeError):
            _ = nepalidate(2051, 4, 29) < 0

        #
        # test less than equal
        self.assertEqual(nepalidate(2051, 4, 29) <= nepalidate(2051, 4, 30), True)
        self.assertEqual(nepalidate(2051, 4, 29) <= nepalidate(2051, 4, 29), True)
        self.assertEqual(nepalidate(2051, 4, 30) <= nepalidate(2051, 4, 29), False)
        self.assertEqual(nepalidate(2051, 4, 29) <= datetime.date(1994, 8, 14), True)
        self.assertEqual(nepalidate(2051, 4, 29) <= datetime.date(1994, 8, 13), True)
        self.assertEqual(nepalidate(2051, 4, 30) <= datetime.date(1994, 8, 13), False)
        with self.assertRaises(TypeError):
            _ = nepalidate(2051, 4, 29) <= 0

        #
        # test greater than
        self.assertEqual(nepalidate(2051, 4, 30) > nepalidate(2051, 4, 29), True)
        self.assertEqual(nepalidate(2051, 4, 30) > nepalidate(2051, 4, 30), False)
        self.assertEqual(nepalidate(2051, 4, 30) > datetime.date(1994, 8, 14), False)
        self.assertEqual(nepalidate(2051, 4, 30) > datetime.date(1994, 8, 13), True)
        with self.assertRaises(TypeError):
            _ = nepalidate(2051, 4, 29) > 0

        #
        # test greater than equal
        self.assertEqual(nepalidate(2051, 4, 30) >= nepalidate(2051, 4, 30), True)
        self.assertEqual(nepalidate(2051, 4, 30) >= nepalidate(2051, 4, 29), True)
        self.assertEqual(nepalidate(2051, 4, 29) >= nepalidate(2051, 4, 30), False)
        self.assertEqual(nepalidate(2051, 4, 30) >= datetime.date(1994, 8, 14), True)
        self.assertEqual(nepalidate(2051, 4, 30) >= datetime.date(1994, 8, 13), True)
        self.assertEqual(nepalidate(2051, 4, 29) >= datetime.date(1994, 8, 14), False)
        with self.assertRaises(TypeError):
            _ = nepalidate(2051, 4, 29) >= 0

    def test_nepalidate_year_month_day(self):
        nepalidate_obj = nepalidate(year=2051, month=4, day=28)
        self.assertEqual(nepalidate_obj.year, 2051)
        self.assertEqual(nepalidate_obj.month, 4)
        self.assertEqual(nepalidate_obj.day, 28)
        self.assertEqual(nepalidate_obj.weekday(), 5)

    def test_nepalidate_from_date(self):
        python_date_obj = datetime.date(year=1994, month=8, day=12)
        nepalidate_obj = nepalidate.from_date(python_date_obj)
        self.assertEqual(
            python_date_obj,
            nepalidate_obj.to_date(),
            "nepalidate from_date and to_date are not equal.",
        )

    def test_nepalidate_from_datetime(self):
        python_datetime_obj = datetime.datetime(
            year=1994, month=8, day=12, hour=4, minute=8, second=12
        )
        nepalidate_obj = nepalidate.from_datetime(python_datetime_obj)
        self.assertEqual(
            python_datetime_obj.date(),
            nepalidate_obj.to_date(),
            "nepalidate from_datetime and to_datetime are not equal.",
        )

    def test_nepalidate_strftime(self):
        nepalidate_obj = nepalidate(year=2051, month=4, day=28)
        self.assertEqual(nepalidate_obj.strftime("%Y-%m-%d"), "2051-04-28")
        self.assertEqual(
            nepalidate_obj.strftime("%a %A %w %d %b %B %m %y %Y"),
            "Fri Friday 5 28 Sharwan Sharwan 04 51 2051",
        )
        self.assertEqual(nepalidate_obj.strftime_en("%Y-%m-%d"), "2051-04-28")
        self.assertEqual(
            nepalidate_obj.strftime_en("%a %A %w %d %b %B %m %y %Y"),
            "Fri Friday 5 28 Sharwan Sharwan 04 51 2051",
        )
        self.assertEqual(nepalidate_obj.strftime_ne("%Y-%m-%d"), "२०५१-०४-२८")
        self.assertEqual(
            nepalidate_obj.strftime_ne("%a %A %w %d %b %B %m %y %Y"),
            "शुक्र शुक्रबार ५ २८ साउन साउन ०४ ५१ २०५१",
        )

    def test_nepalidate_strptime(self):
        nepalidatetime_obj = nepalidate.strptime("2078-01-12", format="%Y-%m-%d")
        self.assertEqual(nepalidatetime_obj.year, 2078)
        self.assertEqual(nepalidatetime_obj.month, 1)
        self.assertEqual(nepalidatetime_obj.day, 12)

    #
    # nepalitime

    def test_nepalitime_now(self):
        nepalitime_obj, dt_now = nepalitime.now(), datetime.datetime.now()
        self.assertEqual(nepalitime_obj.hour, dt_now.hour)
        self.assertEqual(nepalitime_obj.minute, dt_now.minute)
        self.assertEqual(nepalitime_obj.second, dt_now.second)

    #
    # nepalidatetime

    def test_nepalidatetime_from_date(self):
        python_datetime_obj = datetime.datetime(
            year=1994, month=8, day=12, hour=5, minute=28, second=23
        )
        nepalidatetime_obj = nepalidatetime.from_date(python_datetime_obj)
        self.assertEqual(python_datetime_obj.date(), nepalidatetime_obj.to_date())

    def test_nepalidatetime_from_datetime(self):
        python_datetime_obj = datetime.datetime(
            year=1994,
            month=8,
            day=12,
            hour=5,
            minute=28,
            second=23,
            tzinfo=NepaliTimeZone(),
        )
        nepalidatetime_obj = nepalidatetime.from_datetime(python_datetime_obj)
        self.assertEqual(
            python_datetime_obj,
            nepalidatetime_obj.to_datetime(),
            msg="{} and {} are not equal.".format(
                python_datetime_obj, nepalidatetime_obj.to_datetime()
            ),
        )

    def test_nepalidatetime_strftime(self):
        nepalidatetime_obj = nepalidatetime(
            year=2051, month=4, day=28, hour=5, minute=28, second=23
        )
        self.assertEqual(
            nepalidatetime_obj.strftime("%Y-%m-%d %H:%M:%S"), "2051-04-28 05:28:23"
        )
        self.assertEqual(
            nepalidatetime_obj.strftime("%a %A %w %d %b %B %m %y %Y %H %I %p %M %S"),
            "Fri Friday 5 28 Sharwan Sharwan 04 51 2051 05 05 AM 28 23",
        )
        self.assertEqual(
            nepalidatetime_obj.strftime_en("%Y-%m-%d %H:%M:%S"), "2051-04-28 05:28:23"
        )
        self.assertEqual(
            nepalidatetime_obj.strftime_en("%a %A %w %d %b %B %m %y %Y %H %I %p %M %S"),
            "Fri Friday 5 28 Sharwan Sharwan 04 51 2051 05 05 AM 28 23",
        )
        self.assertEqual(
            nepalidatetime_obj.strftime_en(
                "%a %A %w %d %-d %b %B %m %-m %y %Y %H %-H %I %-I %p %M %-M %S %-S %%"
            ),
            "Fri Friday 5 28 28 Sharwan Sharwan 04 4 51 2051 05 5 05 5 AM 28 28 23 23 %",
        )
        self.assertEqual(
            nepalidatetime_obj.strftime_ne("%Y-%m-%d %H:%M:%S"), "२०५१-०४-२८ ०५:२८:२३"
        )
        self.assertEqual(
            nepalidatetime_obj.strftime_ne("%a %A %w %d %b %B %m %y %Y %H %I %p %M %S"),
            "शुक्र शुक्रबार ५ २८ साउन साउन ०४ ५१ २०५१ ०५ ०५ शुभप्रभात २८ २३",
        )

    def test_nepalidatetime_strptime(self):
        nepalidatetime_obj = nepalidatetime.strptime(
            "2078-01-12 13:12", format="%Y-%m-%d %H:%M"
        )
        self.assertEqual(nepalidatetime_obj.year, 2078)
        self.assertEqual(nepalidatetime_obj.month, 1)
        self.assertEqual(nepalidatetime_obj.day, 12)
        self.assertEqual(nepalidatetime_obj.hour, 13)
        self.assertEqual(nepalidatetime_obj.minute, 12)

    def test_nepalidatetime_timedelta(self):
        nepalidatetime_obj1 = nepalidatetime(
            year=2051, month=4, day=28, hour=5, minute=28, second=23
        )
        nepalidatetime_obj2 = nepalidatetime(
            year=2051, month=4, day=29, hour=5, minute=28, second=23
        )
        nepalidatetime_obj1 = nepalidatetime_obj1 + datetime.timedelta(days=1)
        self.assertEqual(
            nepalidatetime_obj1,
            nepalidatetime_obj2,
            msg="{} and {} are not equal".format(
                nepalidatetime_obj1, nepalidatetime_obj2
            ),
        )


class TestDatetimeUtils(unittest.TestCase):
    # to_nepalidate
    def test_to_nepalidate_raises_exception_on_invalid_input(self):
        with self.assertRaises(InvalidNepaliDateTimeObjectException):
            to_nepalidate("Invalid input")

    def test_to_nepalidate_from_python_date(self):
        np_date = to_nepalidate(datetime.date(2023, 2, 26))
        self.assertSequenceEqual(
            (np_date.year, np_date.month, np_date.day), (2079, 11, 14)
        )

    def test_to_nepalidate_from_python_datetime(self):
        np_date = to_nepalidate(datetime.datetime(2023, 2, 26, 1, 12, 13))
        self.assertSequenceEqual(
            (np_date.year, np_date.month, np_date.day), (2079, 11, 14)
        )

    def test_to_nepalidate_from_nepalidate(self):
        np_date = to_nepalidate(nepalidate(2079, 11, 14))
        self.assertSequenceEqual(
            (np_date.year, np_date.month, np_date.day), (2079, 11, 14)
        )

    def test_to_nepalidate_from_nepalidatetime(self):
        np_date = to_nepalidate(nepalidatetime(2079, 11, 14, 1, 12, 13))
        self.assertSequenceEqual(
            (np_date.year, np_date.month, np_date.day), (2079, 11, 14)
        )

    # to_nepalidatetime
    def test_to_nepalidatetime_raises_exception_on_invalid_input(self):
        with self.assertRaises(InvalidNepaliDateTimeObjectException):
            to_nepalidatetime("Invalid input")

    def test_to_nepalidatetime_from_python_date(self):
        np_date = to_nepalidatetime(datetime.date(2023, 2, 26))
        self.assertSequenceEqual(
            (
                np_date.year,
                np_date.month,
                np_date.day,
                np_date.hour,
                np_date.minute,
                np_date.second,
            ),
            (2079, 11, 14, 0, 0, 0),
        )

    def test_to_nepalidatetime_from_python_datetime(self):
        np_date = to_nepalidatetime(
            datetime.datetime(2023, 2, 26, 4, 30, 13, tzinfo=datetime.timezone.utc)
        )
        self.assertSequenceEqual(
            (
                np_date.year,
                np_date.month,
                np_date.day,
                np_date.hour,
                np_date.minute,
                np_date.second,
            ),
            (2079, 11, 14, 10, 15, 13),
        )

    def test_to_nepalidatetime_from_nepalidate(self):
        np_date = to_nepalidatetime(nepalidate(2079, 11, 14))
        self.assertSequenceEqual(
            (
                np_date.year,
                np_date.month,
                np_date.day,
                np_date.hour,
                np_date.minute,
                np_date.second,
            ),
            (2079, 11, 14, 0, 0, 0),
        )

    def test_to_nepalidatetime_from_nepalidatetime(self):
        np_date = to_nepalidatetime(nepalidatetime(2079, 11, 14, 1, 12, 13))
        self.assertSequenceEqual(
            (
                np_date.year,
                np_date.month,
                np_date.day,
                np_date.hour,
                np_date.minute,
                np_date.second,
            ),
            (2079, 11, 14, 1, 12, 13),
        )
