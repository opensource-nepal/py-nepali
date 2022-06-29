import unittest

from nepali.char import nepali_to_english_text
from nepali.datetime import nepalidatetime
from nepali.datetime import parser as nepalidatetime_parser
from nepali.datetime.parser.validators import NepaliTimeRE, extract, transform, validate
from nepali.exceptions import FormatNotMatchException, InvalidDateTimeFormatException


class TestNepaliDateTimeParserValidators(unittest.TestCase):
    '''
    Tests nepali date
    '''

    def setUp(self) -> None:
        self.nepali_time_re = NepaliTimeRE()
        return super().setUp()

    # test extract

    def test_simple_extract(self):
        extracted_data = extract("2078-01-12", format="%Y-%m-%d")
        self.assertEqual(extracted_data.get('Y'), '2078')
        self.assertEqual(extracted_data.get('m'), '01')
        self.assertEqual(extracted_data.get('d'), '12')

    def test_complex_extract(self):
        extracted_data = extract("Wed Wednesday 3 28 Sharwan Sharwan 04 51 2051 05 05 AM 28 23", format="%a %A %w %d %b %B %m %y %Y %H %I %p %M %S")
        self.assertEqual(extracted_data.get('a'), 'Wed')
        self.assertEqual(extracted_data.get('A'), 'Wednesday')
        self.assertEqual(extracted_data.get('w'), '3')
        self.assertEqual(extracted_data.get('d'), '28')
        self.assertEqual(extracted_data.get('b'), 'Sharwan')
        self.assertEqual(extracted_data.get('B'), 'Sharwan')
        self.assertEqual(extracted_data.get('m'), '04')
        self.assertEqual(extracted_data.get('y'), '51')
        self.assertEqual(extracted_data.get('Y'), '2051')
        self.assertEqual(extracted_data.get('H'), '05')
        self.assertEqual(extracted_data.get('I'), '05')
        self.assertEqual(extracted_data.get('p'), 'AM')
        self.assertEqual(extracted_data.get('M'), '28')
        self.assertEqual(extracted_data.get('S'), '23')

    def test_nepali_to_english_text_conversion(self):
        self.assertEqual(
            nepali_to_english_text('बुध बुधबार ३ २८ साउन साउन ०४ ५१ २०५१ ०५ ०५ शुभप्रभात २८ २३'),
            'Wed Wednesday 3 28 Sharwan Sharwan 04 51 2051 05 05 AM 28 23'
        )

    def test_complex_extract_in_nepali(self):
        extracted_data = extract("बुध बुधबार ३ २८ साउन साउन ०४ ५१ २०५१ ०५ ०५ शुभप्रभात २८ २३", format="%a %A %w %d %b %B %m %y %Y %H %I %p %M %S")
        self.assertEqual(extracted_data.get('a'), 'Wed')
        self.assertEqual(extracted_data.get('A'), 'Wednesday')
        self.assertEqual(extracted_data.get('w'), '3')
        self.assertEqual(extracted_data.get('d'), '28')
        self.assertEqual(extracted_data.get('b'), 'Sharwan')
        self.assertEqual(extracted_data.get('B'), 'Sharwan')
        self.assertEqual(extracted_data.get('m'), '04')
        self.assertEqual(extracted_data.get('y'), '51')
        self.assertEqual(extracted_data.get('Y'), '2051')
        self.assertEqual(extracted_data.get('H'), '05')
        self.assertEqual(extracted_data.get('I'), '05')
        self.assertEqual(extracted_data.get('p'), 'AM')
        self.assertEqual(extracted_data.get('M'), '28')
        self.assertEqual(extracted_data.get('S'), '23')


    # test transform
    def test_transform(self):
        data = transform({
            'Y': '2078',
            'b': 'MAngsir',
            'd': '12',
            'p': 'pm',
            'I': '05',
            'M': '25',
            'S': '31',
            'f': '455',
            'a': 'Wed',
        })
        self.assertEqual(data.get('year'), 2078)
        self.assertEqual(data.get('month'), 8)
        self.assertEqual(data.get('day'), 12)
        self.assertEqual(data.get('hour'), 17)
        self.assertEqual(data.get('minute'), 25)
        self.assertEqual(data.get('second'), 31)
        self.assertEqual(data.get('microsecond'), 455000)
        self.assertEqual(data.get('weekday'), 4)

    #
    # test validate

    def test_validate(self):
        nepalidatetime_obj = validate('2078-01-12', format='%Y-%m-%d')
        self.assertEqual(nepalidatetime_obj.year, 2078)
        self.assertEqual(nepalidatetime_obj.month, 1)
        self.assertEqual(nepalidatetime_obj.day, 12)

        nepalidatetime_obj = validate('2079-03-32', format='%Y-%m-%d')
        self.assertEqual(nepalidatetime_obj.year, 2079)
        self.assertEqual(nepalidatetime_obj.month, 3)
        self.assertEqual(nepalidatetime_obj.day, 32)

    def test_test_validate(self):
        nepalidatetime_obj = validate('29 Jestha, 2078, 1:30 PM', format='%d %B, %Y, %I:%M %p')
        self.assertEqual(nepalidatetime_obj.year, 2078)
        self.assertEqual(nepalidatetime_obj.month, 2)
        self.assertEqual(nepalidatetime_obj.day, 29)
        self.assertEqual(nepalidatetime_obj.hour, 13)
        self.assertEqual(nepalidatetime_obj.minute, 30)
        self.assertEqual(nepalidatetime_obj.second, 0)

    def test_validate_with_invalid_data(self):
        self.assertEqual(validate('2078-01-12', format='%k-%m-%d'), None)
        self.assertEqual(validate('2078-01-12', format='%m-%M-%Y'), None)


class TestNepaliDateTimeParser(unittest.TestCase):
    '''
    Tests nepali datetime parser.
    '''

    # test strptime
    def test_strptime(self):
        nepalidatetime_obj = nepalidatetime_parser.strptime('2078-01-12', format='%Y-%m-%d')
        self.assertEqual(nepalidatetime_obj.year, 2078)
        self.assertEqual(nepalidatetime_obj.month, 1)
        self.assertEqual(nepalidatetime_obj.day, 12)

    def test_strptime_fail(self):
        with self.assertRaises(FormatNotMatchException):
            nepalidatetime_parser.strptime('2078-01-12', format='%Y %d')

    # test parser

    def test_normal_string_parse(self):
        parsed_datetime = nepalidatetime_parser.parse('2071-01-24')
        test_datetime = nepalidatetime(2071, 1, 24)
        self.assertEqual(parsed_datetime, test_datetime)

    def test_complex_string_parse(self):
        nepalidatetime_obj = nepalidatetime_parser.parse('29 Jestha, 2078, 1:30 PM')
        self.assertEqual(nepalidatetime_obj.year, 2078)
        self.assertEqual(nepalidatetime_obj.month, 2)
        self.assertEqual(nepalidatetime_obj.day, 29)
        self.assertEqual(nepalidatetime_obj.hour, 13)
        self.assertEqual(nepalidatetime_obj.minute, 30)

    def test_parse_failed(self):
        with self.assertRaises(InvalidDateTimeFormatException):
            nepalidatetime_parser.parse('')
