"""
To run only this unit test use the command below.

    python -m unittest nepali/tests/test_date_converter.py -v
"""
import unittest

from nepali.date_converter import converter


class TestNepaliDateConverter(unittest.TestCase):
    # test date range
    def test_english_date_range(self):
        self.assertEqual(converter.en_min_year(), 1944)
        self.assertEqual(converter.en_max_year(), 2042)

    def test_nepali_date_range(self):
        self.assertEqual(converter.np_min_year(), 2000)
        self.assertEqual(converter.np_max_year(), 2099)

    # english_to_nepali
    def test_converter_english_to_nepali_raise_exception_on_max_year_range(self):
        with self.assertRaises(Exception):
            converter.english_to_nepali(2060, 1, 4)

    def test_converter_english_to_nepali_raise_exception_on_min_year_range(self):
        with self.assertRaises(Exception):
            converter.english_to_nepali(1920, 1, 4)

    def test_converter_english_to_nepali_raise_exception_on_min_month_range(self):
        with self.assertRaises(Exception):
            converter.english_to_nepali(2023, 0, 4)

    def test_converter_english_to_nepali_raise_exception_on_max_month_range(self):
        with self.assertRaises(Exception):
            converter.english_to_nepali(2023, 13, 4)

    def test_converter_english_to_nepali_raise_exception_on_min_day_range(self):
        with self.assertRaises(Exception):
            converter.english_to_nepali(2023, 1, 0)

    def test_converter_english_to_nepali_raise_exception_on_max_day_range(self):
        with self.assertRaises(Exception):
            converter.english_to_nepali(2023, 1, 40)

    def test_converter_english_to_nepali_returns_valid_past_nepali_date(self):
        y, m, d = converter.english_to_nepali(1994, 8, 13)
        self.assertEqual(y, 2051)
        self.assertEqual(m, 4)
        self.assertEqual(d, 29)

    def test_converter_english_to_nepali_returns_valid_recent_nepali_date(self):
        y, m, d = converter.english_to_nepali(2023, 1, 28)
        self.assertEqual(y, 2079)
        self.assertEqual(m, 10)
        self.assertEqual(d, 14)

    def test_converter_english_to_nepali_returns_valid_future_nepali_date(self):
        y, m, d = converter.english_to_nepali(2030, 11, 26)
        self.assertEqual(y, 2087)
        self.assertEqual(m, 8)
        self.assertEqual(d, 10)

    def test_converter_english_to_nepali_for_min_edge_date(self):
        y, m, d = converter.english_to_nepali(1944, 1, 1)
        self.assertEqual(y, 2000)
        self.assertEqual(m, 9)
        self.assertEqual(d, 17)

    def test_converter_english_to_nepali_for_max_edge_date(self):
        y, m, d = converter.english_to_nepali(2042, 12, 31)
        self.assertEqual(y, 2099)
        self.assertEqual(m, 9)
        self.assertEqual(d, 16)

    # nepali_to_english
    def test_converter_nepali_to_englishReturnErrorOnMaxYearRange(self):
        with self.assertRaises(Exception):
            converter.nepali_to_english(3000, 1, 4)

    def test_converter_nepali_to_english_raise_exception_on_min_year_range(self):
        with self.assertRaises(Exception):
            converter.nepali_to_english(1920, 1, 4)

    def test_converter_nepali_to_english_raise_exception_on_min_month_range(self):
        with self.assertRaises(Exception):
            converter.nepali_to_english(2079, 0, 4)

    def test_converter_nepali_to_english_raise_exception_on_max_month_range(self):
        with self.assertRaises(Exception):
            converter.nepali_to_english(2079, 13, 4)

    def test_converter_nepali_to_english_raise_exception_on_min_day_range(self):
        with self.assertRaises(Exception):
            converter.nepali_to_english(2079, 1, 0)

    def test_converter_nepali_to_english_raise_exception_on_max_day_range(self):
        with self.assertRaises(Exception):
            converter.nepali_to_english(2079, 1, 40)

    def test_converter_nepali_to_englishReturnsValidPastEnglishDate(self):
        y, m, d = converter.nepali_to_english(2051, 4, 29)
        self.assertEqual(y, 1994)
        self.assertEqual(m, 8)
        self.assertEqual(d, 13)

    def test_converter_nepali_to_englishReturnsValidRecentEnglishDate(self):
        y, m, d = converter.nepali_to_english(2079, 10, 14)
        self.assertEqual(y, 2023)
        self.assertEqual(m, 1)
        self.assertEqual(d, 28)

    def test_converter_nepali_to_englishReturnsValidFutureEnglishDate(self):
        y, m, d = converter.nepali_to_english(2087, 8, 10)
        self.assertEqual(y, 2030)
        self.assertEqual(m, 11)
        self.assertEqual(d, 26)

    def test_converter_nepali_to_englishReturnsValidEnglishLeapYearDate(self):
        y, m, d = converter.nepali_to_english(2080, 12, 15)
        self.assertEqual(y, 2024)
        self.assertEqual(m, 3)
        self.assertEqual(d, 28)

    def test_converter_nepali_to_english_for_min_edge_date(self):
        y, m, d = converter.nepali_to_english(2000, 1, 1)
        self.assertEqual(y, 1943)
        self.assertEqual(m, 4)
        self.assertEqual(d, 14)

    def test_converter_nepali_to_english_for_max_edge_date(self):
        y, m, d = converter.nepali_to_english(2099, 12, 30)
        self.assertEqual(y, 2043)
        self.assertEqual(m, 4)
        self.assertEqual(d, 13)
