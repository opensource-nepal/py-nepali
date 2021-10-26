import unittest

from nepali.datetime import nepalidatetime
from nepali.datetime import parser as nepalidatetime_parser
from nepali.datetime.parser.validators import NepaliTimeRE
from nepali.exceptions import InvalidDateTimeFormatException


class TestNepaliDateTimeParserValidators(unittest.TestCase):
    '''
    Tests nepali date
    '''

    def setUp(self) -> None:
        self.nepali_time_re = NepaliTimeRE()
        return super().setUp()

    def test_format_to_regex(self):
        format_to_regex = self.nepali_time_re.pattern('%Y $ \d %-d *')
        self.assertEqual(format_to_regex, r'(?P<Y>\d\d\d\d)\s+\$\s+\\d\s+(?P<d>3[0-1]|[1-2]\d|0[1-9]|[1-9]| [1-9])\s+\*')


class TestNepaliDateTimeParser(unittest.TestCase):
    '''
    Tests nepali datetime parser.
    '''

    def test_normal_string_parse(self):
        parsed_datetime = nepalidatetime_parser.parse('2071-01-24')
        test_datetime = nepalidatetime(2071, 1, 24)
        self.assertEqual(parsed_datetime, test_datetime)

    def test_parse_failed(self):
        with self.assertRaises(InvalidDateTimeFormatException):
            parsed_datetime = nepalidatetime_parser.parse('')
