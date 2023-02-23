import datetime
import unittest
from unittest.mock import patch

from nepali.datetime import nepalihumanize, HumanizeDateTime, nepalidate, nepalidatetime
from nepali.exceptions import InvalidNepaliDateTimeObjectException
from nepali.timezone import NepaliTimeZone


REF_TIME = datetime.datetime(2015, 1, 1, 10, 15, tzinfo=NepaliTimeZone())


@patch("nepali.datetime._humanize.now", return_value=REF_TIME)
class TestNepaliHumanizeFunction(unittest.TestCase):
    def test_nepalihumanize_for_just_now(self, *_):
        humanize_str = nepalihumanize(REF_TIME)
        self.assertEqual(humanize_str, "भर्खरै")

    def test_nepalihumanize_for_seconds(self, *_):
        humanize_str = nepalihumanize(REF_TIME - datetime.timedelta(seconds=10))
        self.assertEqual(humanize_str, "१० सेकेन्ड अघि")

    def test_nepalihumanize_for_minutes(self, *_):
        humanize_str = nepalihumanize(REF_TIME - datetime.timedelta(minutes=10))
        self.assertEqual(humanize_str, "१० मिनेट अघि")

    def test_nepalihumanize_for_hours(self, *_):
        humanize_str = nepalihumanize(REF_TIME - datetime.timedelta(hours=10))
        self.assertEqual(humanize_str, "१० घण्टा अघि")

    def test_nepalihumanize_for_days(self, *_):
        humanize_str = nepalihumanize(REF_TIME - datetime.timedelta(days=10))
        self.assertEqual(humanize_str, "१० दिन अघि")

    def test_nepalihumanize_for_months(self, *_):
        humanize_str = nepalihumanize(REF_TIME - datetime.timedelta(days=32))
        self.assertEqual(humanize_str, "१ महिना अघि")

    def test_nepalihumanize_for_years(self, *_):
        humanize_str = nepalihumanize(REF_TIME - datetime.timedelta(days=366))
        self.assertEqual(humanize_str, "१ वर्ष अघि")

    def test_nepalihumanize_for_future(self, *_):
        humanize_str = nepalihumanize(REF_TIME + datetime.timedelta(days=10))
        self.assertEqual(humanize_str, "१० दिन पछि")

    def test_nepalihumanize_returns_date_after_threshold(self, *_):
        humanize_str = nepalihumanize(
            REF_TIME - datetime.timedelta(seconds=10), threshold=10
        )
        self.assertEqual(humanize_str, "पुस १७, २०७१")


class TestHumanizeDateTimeClass(unittest.TestCase):
    def test_nepali_humanize_raise_exception_on_invalid_input(self, *_):
        with self.assertRaises(InvalidNepaliDateTimeObjectException):
            HumanizeDateTime("test")

        with self.assertRaises(InvalidNepaliDateTimeObjectException):
            HumanizeDateTime(None)

        with self.assertRaises(InvalidNepaliDateTimeObjectException):
            HumanizeDateTime("2017-12-04")

    def test_nepali_humanize_supports_python_date(self, *_):
        humanize_obj = HumanizeDateTime(datetime.date.today())
        self.assertEqual(type(humanize_obj.to_str()), str)

    def test_nepali_humanize_supports_python_datetime(self, *_):
        humanize_obj = HumanizeDateTime(datetime.datetime.now())
        self.assertEqual(type(humanize_obj.to_str()), str)

    def test_nepali_humanize_supports_nepalidate(self, *_):
        humanize_obj = HumanizeDateTime(nepalidate.today())
        self.assertEqual(type(humanize_obj.to_str()), str)

    def test_nepali_humanize_supports_nepalidatetime(self, *_):
        humanize_obj = HumanizeDateTime(nepalidatetime.now())
        self.assertEqual(type(humanize_obj.to_str()), str)

    @patch("nepali.datetime._humanize.now", return_value=REF_TIME)
    def test_test_nepali_humanize_str_and_repr(self, *_):
        humanize_obj = HumanizeDateTime(REF_TIME + datetime.timedelta(days=10))
        self.assertEqual(str(humanize_obj), "१० दिन पछि")
        self.assertEqual(repr(humanize_obj), "१० दिन पछि")
