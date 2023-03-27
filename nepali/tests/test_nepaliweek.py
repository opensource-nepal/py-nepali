"""
To run only this unit test use the command below.

    python -m unittest nepali/tests/test_nepaliweek.py -v
"""
import unittest

from nepali.datetime import nepaliweek


class TestNepaliWeek(unittest.TestCase):
    # parse
    def test_nepaliweek_parses_int(self):
        self.assertEqual(nepaliweek(1).value, 1)
        self.assertEqual(nepaliweek(7).value, 7)

    def test_nepaliweek_fails_for_int_less_than_1(self):
        with self.assertRaises(ValueError) as ex:
            nepaliweek(0)
        self.assertEqual(str(ex.exception), "Invalid week: 0")
        with self.assertRaises(ValueError):
            nepaliweek(-100)

    def test_nepaliweek_fails_for_int_more_than_7(self):
        with self.assertRaises(ValueError) as ex:
            nepaliweek(8)
        self.assertEqual(str(ex.exception), "Invalid week: 8")
        with self.assertRaises(ValueError):
            nepaliweek(100)

    def test_nepaliweek_parses_str_int_number(self):
        week = nepaliweek("1")
        self.assertEqual(week.value, 1)

    def test_nepaliweek_fails_for_str_int_out_of_range(self):
        with self.assertRaises(ValueError):
            nepaliweek("0")
        with self.assertRaises(ValueError):
            nepaliweek("-100")
        with self.assertRaises(ValueError):
            nepaliweek("8")
        with self.assertRaises(ValueError):
            nepaliweek("100")

    def test_nepaliweek_fails_for_invalid_str(self):
        with self.assertRaises(ValueError):
            nepaliweek("hello")
        with self.assertRaises(ValueError):
            nepaliweek("1.0")

    def test_nepaliweek_parse_valid_week_in_english(self):
        self.assertEqual(nepaliweek("Sunday").value, 1)
        self.assertEqual(nepaliweek("Monday").value, 2)
        self.assertEqual(nepaliweek("Tuesday").value, 3)
        self.assertEqual(nepaliweek("Wednesday").value, 4)
        self.assertEqual(nepaliweek("Thursday").value, 5)
        self.assertEqual(nepaliweek("Friday").value, 6)
        self.assertEqual(nepaliweek("Saturday").value, 7)

    def test_nepaliweek_parse_valid_week_in_english_lower_case(self):
        self.assertEqual(nepaliweek("sunday").value, 1)
        self.assertEqual(nepaliweek("monday").value, 2)
        self.assertEqual(nepaliweek("tuesday").value, 3)
        self.assertEqual(nepaliweek("wednesday").value, 4)
        self.assertEqual(nepaliweek("thursday").value, 5)
        self.assertEqual(nepaliweek("friday").value, 6)
        self.assertEqual(nepaliweek("saturday").value, 7)

    def test_nepaliweek_parse_valid_week_in_english_case_insensitive(self):
        self.assertEqual(nepaliweek("sUnday").value, 1)
        self.assertEqual(nepaliweek("moNday").value, 2)
        self.assertEqual(nepaliweek("tueSday").value, 3)
        self.assertEqual(nepaliweek("wednEsday").value, 4)
        self.assertEqual(nepaliweek("thursDay").value, 5)
        self.assertEqual(nepaliweek("fridaY").value, 6)
        self.assertEqual(nepaliweek("saTurday").value, 7)

    def test_nepaliweek_parse_valid_week_in_english_abbreviated_name(self):
        self.assertEqual(nepaliweek("Sun").value, 1)
        self.assertEqual(nepaliweek("Mon").value, 2)
        self.assertEqual(nepaliweek("Tue").value, 3)
        self.assertEqual(nepaliweek("Wed").value, 4)
        self.assertEqual(nepaliweek("Thu").value, 5)
        self.assertEqual(nepaliweek("Fri").value, 6)
        self.assertEqual(nepaliweek("Sat").value, 7)

    def test_nepaliweek_parse_valid_week_in_nepali(self):
        self.assertEqual(nepaliweek("आइतबार").value, 1)
        self.assertEqual(nepaliweek("सोमबार").value, 2)
        self.assertEqual(nepaliweek("मंगलबार").value, 3)
        self.assertEqual(nepaliweek("बुधबार").value, 4)
        self.assertEqual(nepaliweek("बिहीबार").value, 5)
        self.assertEqual(nepaliweek("शुक्रबार").value, 6)
        self.assertEqual(nepaliweek("शनिबार").value, 7)

    def test_nepaliweek_parse_valid_week_in_nepali_abbreviated_name(self):
        self.assertEqual(nepaliweek("आइत").value, 1)
        self.assertEqual(nepaliweek("सोम").value, 2)
        self.assertEqual(nepaliweek("मंगल").value, 3)
        self.assertEqual(nepaliweek("बुध").value, 4)
        self.assertEqual(nepaliweek("बिही").value, 5)
        self.assertEqual(nepaliweek("शुक्र").value, 6)
        self.assertEqual(nepaliweek("शनि").value, 7)

    def test_nepaliweek_fails_for_invalid_data_type(self):
        with self.assertRaises(ValueError):
            nepaliweek(1.0)  # type: ignore
        with self.assertRaises(ValueError):
            nepaliweek(2j + 1)  # type: ignore
        with self.assertRaises(ValueError):
            nepaliweek([])  # type: ignore

    def test_nepaliweek_str(self):
        self.assertEqual(str(nepaliweek(1)), nepaliweek(1).name)

    def test_nepaliweek_repr(self):
        self.assertEqual(repr(nepaliweek(1)), "<nepaliweek: 1>")

    def test_nepaliweek_name(self):
        self.assertEqual(nepaliweek(1).name, "Sunday")
        self.assertEqual(nepaliweek(7).name, "Saturday")

    def test_nepaliweek_abbr(self):
        self.assertEqual(nepaliweek(1).abbr, "Sun")
        self.assertEqual(nepaliweek(7).abbr, "Sat")

    def test_nepaliweek_name_ne(self):
        self.assertEqual(nepaliweek(1).name_ne, "आइतबार")
        self.assertEqual(nepaliweek(7).name_ne, "शनिबार")

    def test_nepaliweek_abbr_ne(self):
        self.assertEqual(nepaliweek(1).abbr_ne, "आइत")
        self.assertEqual(nepaliweek(7).abbr_ne, "शनि")

    def test_nepaliweek_variable_cache(self):
        self.assertEqual(id(nepaliweek(1)), id(nepaliweek(1)))
        self.assertEqual(id(nepaliweek(7)), id(nepaliweek(7)))

    def test_nepaliweek_int(self):
        self.assertEqual(int(nepaliweek(1)), 1)
        self.assertEqual(int(nepaliweek(7)), 7)

    def test_nepaliweek_equal_with_nepaliweek(self):
        self.assertEqual(nepaliweek(1), nepaliweek(1))
        self.assertEqual(nepaliweek(7), nepaliweek(7))

    def test_nepaliweek_not_equal(self):
        self.assertNotEqual(nepaliweek(1), nepaliweek(2))
        self.assertNotEqual(nepaliweek(1), 2)

    def test_nepaliweek_equal_with_int(self):
        self.assertEqual(nepaliweek(1), 1)
        self.assertEqual(nepaliweek(7), 7)
        self.assertEqual(1, nepaliweek(1))
        self.assertEqual(7, nepaliweek(7))

    def test_nepaliweek_not_equal_with_invalid_object(self):
        self.assertNotEqual(nepaliweek(1), "invalid")
