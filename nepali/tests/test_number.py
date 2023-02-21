"""
To run only this unit test use the command below.

    python -m unittest nepali/tests/test_number.py -v
"""
import unittest

from nepali import number

NepaliNumber = number.NepaliNumber


class TestNumber(unittest.TestCase):
    def test_number_english_to_nepali(self):
        self.assertEqual(
            number.english_to_nepali("0123456789०१२३४५६७८९"), "०१२३४५६७८९०१२३४५६७८९"
        )
        self.assertEqual(
            NepaliNumber.convert("0123456789०१२३४५६७८९"), "०१२३४५६७८९०१२३४५६७८९"
        )

    def test_number_nepali_to_english(self):
        self.assertEqual(
            number.nepali_to_english("0123456789०१२३४५६७८९"), "01234567890123456789"
        )
        self.assertEqual(
            NepaliNumber.revert("0123456789०१२३४५६७८९"), "01234567890123456789"
        )

    def test_number_add_comma(self):
        self.assertEqual(number.add_comma("123456789"), "12,34,56,789")
        self.assertEqual(NepaliNumber.add_comma("123456789"), "12,34,56,789")

    def test_number_add_comma_english(self):
        self.assertEqual(number.add_comma_english("123456789"), "123,456,789")
        self.assertEqual(NepaliNumber.add_comma_english("123456789"), "123,456,789")

    def test_number_add_comma_with_convert_True(self):
        self.assertEqual(number.add_comma("123456789", convert=True), "१२,३४,५६,७८९")

    def test_number_add_comma_with_convert_False(self):
        self.assertEqual(number.add_comma("123456789", convert=False), "12,34,56,789")

    def test_number_convert_and_add_comma(self):
        self.assertEqual(number.convert_and_add_comma("123456789"), "१२,३४,५६,७८९")
        self.assertEqual(
            NepaliNumber.convert_and_add_comma("123456789"), "१२,३४,५६,७८९"
        )
