import unittest

from nepali.datetime import nepalidatetime
from nepali.datetime import parser as nepalidatetime_parser
from nepali.exceptions import InvalidDateTimeFormatException

class TestNepaliDateTimeParser(unittest.TestCase):
    '''
    tests nepali datetime parser
    '''

    def test_normal_string_parse(self):
        parsed_datetime = nepalidatetime_parser.parse('2071-01-24')
        test_datetime = nepalidatetime(2071, 1, 24)
        self.assertEqual(parsed_datetime, test_datetime)

    def test_parse_failed(self):
        with self.assertRaises(InvalidDateTimeFormatException):
            parsed_datetime = nepalidatetime_parser.parse('')
