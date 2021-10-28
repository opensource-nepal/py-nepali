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

    def test_all_format_to_regex(self):
        format_to_regex = self.nepali_time_re.pattern('%a %A %w %d %b %B %m %y %Y %H %I %p %M %S')
        expected_output = r'(?P<a>Sun|Mon|Tue|Wed|Thu|Fri|Sat)\s+(?P<A>Wednesday|Thursday|Saturday|Tuesday|Sunday|Monday|Friday)\s+(?P<w>[0-6])\s+(?P<d>3[0-1]|[1-2]\d|0[1-9]|[1-9]| [1-9])\s+(?P<b>Baishakh|Sharwan|Mangsir|Chaitra|Jestha|Bhadra|Ashwin|Kartik|Falgun|Ashad|Poush|Magh)\s+(?P<B>Baishakh|Sharwan|Mangsir|Chaitra|Jestha|Bhadra|Ashwin|Kartik|Falgun|Ashad|Poush|Magh)\s+(?P<m>1[0-2]|0[1-9]|[1-9])\s+(?P<y>\d\d)\s+(?P<Y>\d\d\d\d)\s+(?P<H>2[0-3]|[0-1]\d|\d)\s+(?P<I>1[0-2]|0[1-9]|[1-9])\s+(?P<p>AM|PM)\s+(?P<M>[0-5]\d|\d)\s+(?P<S>6[0-1]|[0-5]\d|\d)'
        self.assertEqual(format_to_regex, expected_output)


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
