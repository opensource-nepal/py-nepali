"""
To run only this unit test use the command below.

    python -m unittest nepali/tests/test_timezone.py -v
"""
import datetime
import unittest
from unittest.mock import patch

from nepali.timezone import (
    NepaliTimeZone,
    to_nepali_timezone,
    to_utc_timezone,
    utc_now,
    now,
    get_timezone,
)


class TestNepaliTimeZone(unittest.TestCase):
    def setUp(self):
        self.nepali_timezone = NepaliTimeZone()
        return super().setUp()

    def test_nepali_timezone_dst(self):
        self.assertEqual(self.nepali_timezone.dst(None), datetime.timedelta(0))

    def test_nepali_timezone_utcoffset(self):
        self.assertEqual(
            self.nepali_timezone.utcoffset(None),
            datetime.timedelta(hours=5, minutes=45),
        )

    def test_nepali_timezone_tzname(self):
        self.assertEqual(self.nepali_timezone.tzname(None), "Asia/Kathmandu")

    def test_nepali_timezone_str(self):
        self.assertEqual(str(self.nepali_timezone), "Asia/Kathmandu")

    def test_nepali_timezone_repr(self):
        self.assertEqual(repr(self.nepali_timezone), "Asia/Kathmandu")

    def test_datetime_with_nepali_timezone(self):
        dt = datetime.datetime(2015, 10, 14, tzinfo=self.nepali_timezone)
        self.assertEqual(dt.tzinfo, self.nepali_timezone)
        self.assertEqual(dt.tzname(), self.nepali_timezone.tzname(dt))
        self.assertEqual(dt.utcoffset(), self.nepali_timezone.utcoffset(dt))


class TestTimezoneUtils(unittest.TestCase):
    def test_get_timezone(self):
        tz = get_timezone()
        self.assertIsNotNone(tz)

    @patch("nepali.timezone.get_timezone")
    @patch("nepali.timezone.datetime")
    def test_timezone_now(self, mock_datetime, mock_get_timezone):
        # mocking data
        mock_get_timezone.return_value = (
            datetime.timezone.utc
        )  # mocking get_timezone => UTC
        datetime_now = mock_datetime.datetime.now
        datetime_now.return_value = datetime.datetime(
            2015, 1, 1
        )  # mocking datetime.now => 2015/1/1

        # calling now
        current_dt = now()

        # checking
        self.assertEqual(current_dt, datetime.datetime(2015, 1, 1))
        self.assertSequenceEqual(datetime_now.call_args[0], [datetime.timezone.utc])

    @patch("nepali.timezone.datetime")
    def test_timezone_utc_now(self, mock_datetime):
        # mocking data
        mock_datetime.timezone.utc = (
            datetime.timezone.utc
        )  # reverting the utc timezone mock
        datetime_now = mock_datetime.datetime.now
        datetime_now.return_value = datetime.datetime(
            2015, 1, 1
        )  # mocking datetime.now => 2015/1/1

        # calling utc_now
        utc_dt = utc_now()

        # checking
        self.assertEqual(utc_dt, datetime.datetime(2015, 1, 1))
        self.assertSequenceEqual(datetime_now.call_args[0], [datetime.timezone.utc])

    # to_utc_timezone
    def test_to_utc_timezone_invalid_input_returns_as_it_is(self):
        self.assertEqual(to_utc_timezone("test"), "test")  # type: ignore

    @patch("nepali.timezone.get_timezone")
    def test_to_utc_timezone_without_timezone(self, mock_get_timezone):
        mock_get_timezone.return_value = datetime.timezone(
            offset=datetime.timedelta(hours=5, minutes=30)
        )  # Indian timezone
        dt = datetime.datetime(2014, 11, 14, 10, 15, 11)
        utc_dt = to_utc_timezone(dt)
        self.assertEqual(utc_dt.tzinfo, datetime.timezone.utc)
        self.assertSequenceEqual(
            (
                utc_dt.year,
                utc_dt.month,
                utc_dt.day,
                utc_dt.hour,
                utc_dt.minute,
                utc_dt.second,
            ),
            (2014, 11, 14, 4, 45, 11),
        )

    def test_to_utc_timezone_with_utc_timezone(self):
        dt = datetime.datetime(2014, 11, 14, 10, 15, 11, tzinfo=datetime.timezone.utc)
        utc_dt = to_utc_timezone(dt)
        self.assertEqual(utc_dt.tzinfo, datetime.timezone.utc)
        self.assertSequenceEqual(
            (
                utc_dt.year,
                utc_dt.month,
                utc_dt.day,
                utc_dt.hour,
                utc_dt.minute,
                utc_dt.second,
            ),
            (2014, 11, 14, 10, 15, 11),
        )

    def test_to_utc_timezone_with_nepali_timezone(self):
        dt = datetime.datetime(2014, 11, 14, 10, 15, 11, tzinfo=NepaliTimeZone())
        utc_dt = to_utc_timezone(dt)
        self.assertEqual(utc_dt.tzinfo, datetime.timezone.utc)
        self.assertSequenceEqual(
            (
                utc_dt.year,
                utc_dt.month,
                utc_dt.day,
                utc_dt.hour,
                utc_dt.minute,
                utc_dt.second,
            ),
            (2014, 11, 14, 4, 30, 11),
        )

    # to_nepali_timezone
    def test_to_nepali_timezone_invalid_input_returns_as_it_is(self):
        self.assertEqual(to_nepali_timezone("test"), "test")  # type: ignore

    def test_to_nepali_timezone_without_timezone(self):
        dt = datetime.datetime(2014, 11, 14, 10, 15, 11)
        nepali_dt = to_nepali_timezone(dt)
        self.assertEqual(nepali_dt.tzinfo, NepaliTimeZone())
        self.assertSequenceEqual(
            (dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second),
            (2014, 11, 14, 10, 15, 11),
        )

    def test_to_nepali_timezone_with_utc_timezone(self):
        dt = datetime.datetime(2014, 11, 14, 4, 30, 11, tzinfo=datetime.timezone.utc)
        nepali_dt = to_nepali_timezone(dt)
        self.assertEqual(nepali_dt.tzinfo, NepaliTimeZone())
        self.assertSequenceEqual(
            (
                nepali_dt.year,
                nepali_dt.month,
                nepali_dt.day,
                nepali_dt.hour,
                nepali_dt.minute,
                nepali_dt.second,
            ),
            (2014, 11, 14, 10, 15, 11),
        )

    def test_to_nepali_timezone_with_nepali_timezone(self):
        dt = datetime.datetime(2014, 11, 14, 10, 15, 11, tzinfo=NepaliTimeZone())
        nepali_dt = to_nepali_timezone(dt)
        self.assertEqual(nepali_dt.tzinfo, NepaliTimeZone())
        self.assertSequenceEqual(
            (
                nepali_dt.year,
                nepali_dt.month,
                nepali_dt.day,
                nepali_dt.hour,
                nepali_dt.minute,
                nepali_dt.second,
            ),
            (2014, 11, 14, 10, 15, 11),
        )
