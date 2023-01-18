import unittest
from nepali import phone_number


class TestPhoneNumber(unittest.TestCase):
    def test_parse_invalid_argument(self):
        # string input
        number = phone_number.parse('test')
        self.assertEqual(number, None)

        # None input
        number = phone_number.parse(None)
        self.assertEqual(number, None)

        # invalid number
        number = phone_number.parse('987678')
        self.assertEqual(number, None)

    def test_valid_mobile_number_input(self):
        number = phone_number.parse('9842531781')
        self.assertEqual(type(number), dict)

        number = phone_number.parse('+9779842531781')
        self.assertEqual(type(number), dict)

        number = phone_number.parse('+977-9842531781')
        self.assertEqual(type(number), dict)
        self.assertEqual(number and number['type'], 'Mobile')

    def test_valid_phone_number_input(self):
        number = phone_number.parse('14231481')
        self.assertEqual(type(number), dict)

        number = phone_number.parse('014231481')
        self.assertEqual(type(number), dict)

        number = phone_number.parse('0215154579')
        self.assertEqual(type(number), dict)

        number = phone_number.parse('+977-142314819')
        self.assertEqual(type(number), dict)

        number = phone_number.parse('0154225639')
        self.assertEqual(type(number), dict)

        number = phone_number.parse('9770154225639')
        self.assertEqual(type(number), dict)

        number = phone_number.parse('0565114679')
        self.assertEqual(type(number), dict)

        number = phone_number.parse('+977-0565114679')
        self.assertEqual(type(number), dict)
        self.assertEqual(number and number['type'], 'Mobile')
