"""
To run only this unit test use the command below.

    python -m unittest nepali/tests/test_number.py -v
"""
import unittest

from nepali import number


class TestNumber(unittest.TestCase):
    def test_number_convert(self):
        self.assertEqual(number.convert("0123456789०१२३४५६७८९"), "०१२३४५६७८९०१२३४५६७८९")

    def test_number_revert(self):
        self.assertEqual(number.revert("0123456789०१२३४५६७८९"), "01234567890123456789")

    def test_number_add_comma(self):
        self.assertEqual(number.add_comma("123456789"), "12,34,56,789")

    def test_number_add_comma_english(self):
        self.assertEqual(number.add_comma_english("123456789"), "123,456,789")

    def test_number_convert_and_add_comma(self):
        self.assertEqual(number.convert_and_add_comma("123456789"), "१२,३४,५६,७८९")
