"""
To run only this unit test use the command below.

    python -m unittest nepali/tests/test_nepalimonth.py -v
"""
import unittest

from nepali.datetime import nepalimonth


class TestNepaliMonth(unittest.TestCase):
    # parse
    def test_nepalimonth_parses_int(self):
        self.assertEqual(nepalimonth(1).value, 1)
        self.assertEqual(nepalimonth(12).value, 12)

    def test_nepalimonth_fails_for_int_less_than_1(self):
        with self.assertRaises(ValueError) as ex:
            nepalimonth(0)
        self.assertEqual(str(ex.exception), "Invalid month: 0")
        with self.assertRaises(ValueError):
            nepalimonth(-100)

    def test_nepalimonth_fails_for_int_more_than_12(self):
        with self.assertRaises(ValueError) as ex:
            nepalimonth(13)
        self.assertEqual(str(ex.exception), "Invalid month: 13")
        with self.assertRaises(ValueError):
            nepalimonth(100)

    def test_nepalimonth_parses_str_int_number(self):
        month = nepalimonth("1")
        self.assertEqual(month.value, 1)

    def test_nepalimonth_fails_for_str_int_out_of_range(self):
        with self.assertRaises(ValueError):
            nepalimonth("0")
        with self.assertRaises(ValueError):
            nepalimonth("-100")
        with self.assertRaises(ValueError):
            nepalimonth("13")
        with self.assertRaises(ValueError):
            nepalimonth("100")

    def test_nepalimonth_fails_for_invalid_str(self):
        with self.assertRaises(ValueError):
            nepalimonth("hello")
        with self.assertRaises(ValueError):
            nepalimonth("1.0")

    def test_nepalimonth_parse_valid_month_in_english(self):
        self.assertEqual(nepalimonth("Baishakh").value, 1)
        self.assertEqual(nepalimonth("Jestha").value, 2)
        self.assertEqual(nepalimonth("Ashad").value, 3)
        self.assertEqual(nepalimonth("Sharwan").value, 4)
        self.assertEqual(nepalimonth("Bhadra").value, 5)
        self.assertEqual(nepalimonth("Ashwin").value, 6)
        self.assertEqual(nepalimonth("Kartik").value, 7)
        self.assertEqual(nepalimonth("Mangsir").value, 8)
        self.assertEqual(nepalimonth("Poush").value, 9)
        self.assertEqual(nepalimonth("Magh").value, 10)
        self.assertEqual(nepalimonth("Falgun").value, 11)
        self.assertEqual(nepalimonth("Chaitra").value, 12)

    def test_nepalimonth_parse_valid_month_in_english_lower_case(self):
        self.assertEqual(nepalimonth("baishakh").value, 1)
        self.assertEqual(nepalimonth("jestha").value, 2)
        self.assertEqual(nepalimonth("ashad").value, 3)
        self.assertEqual(nepalimonth("sharwan").value, 4)
        self.assertEqual(nepalimonth("bhadra").value, 5)
        self.assertEqual(nepalimonth("ashwin").value, 6)
        self.assertEqual(nepalimonth("kartik").value, 7)
        self.assertEqual(nepalimonth("mangsir").value, 8)
        self.assertEqual(nepalimonth("poush").value, 9)
        self.assertEqual(nepalimonth("magh").value, 10)
        self.assertEqual(nepalimonth("falgun").value, 11)
        self.assertEqual(nepalimonth("chaitra").value, 12)

    def test_nepalimonth_parse_valid_month_in_english_case_insensitive(self):
        self.assertEqual(nepalimonth("bAisHakh").value, 1)
        self.assertEqual(nepalimonth("jEsTha").value, 2)
        self.assertEqual(nepalimonth("aShaD").value, 3)
        self.assertEqual(nepalimonth("shaRwaN").value, 4)
        self.assertEqual(nepalimonth("BhadRa").value, 5)
        self.assertEqual(nepalimonth("ashWIn").value, 6)
        self.assertEqual(nepalimonth("KArtIk").value, 7)
        self.assertEqual(nepalimonth("MaNGsir").value, 8)
        self.assertEqual(nepalimonth("POush").value, 9)
        self.assertEqual(nepalimonth("maGh").value, 10)
        self.assertEqual(nepalimonth("faLgUn").value, 11)
        self.assertEqual(nepalimonth("ChaItRa").value, 12)

    def test_nepalimonth_parse_valid_month_in_nepali(self):
        self.assertEqual(nepalimonth("बैशाख").value, 1)
        self.assertEqual(nepalimonth("जेठ").value, 2)
        self.assertEqual(nepalimonth("असार").value, 3)
        self.assertEqual(nepalimonth("साउन").value, 4)
        self.assertEqual(nepalimonth("भदौ").value, 5)
        self.assertEqual(nepalimonth("असोज").value, 6)
        self.assertEqual(nepalimonth("कात्तिक").value, 7)
        self.assertEqual(nepalimonth("मंसिर").value, 8)
        self.assertEqual(nepalimonth("पुस").value, 9)
        self.assertEqual(nepalimonth("माघ").value, 10)
        self.assertEqual(nepalimonth("फागुन").value, 11)
        self.assertEqual(nepalimonth("चैत").value, 12)

    def test_nepalimonth_fails_for_invalid_data_type(self):
        with self.assertRaises(ValueError):
            nepalimonth(1.0)  # type: ignore
        with self.assertRaises(ValueError):
            nepalimonth(2j + 1)  # type: ignore
        with self.assertRaises(ValueError):
            nepalimonth([])  # type: ignore

    def test_nepalimonth_str(self):
        self.assertEqual(str(nepalimonth(1)), nepalimonth(1).name)

    def test_nepalimonth_repr(self):
        self.assertEqual(repr(nepalimonth(1)), "<nepalimonth: 1>")

    def test_nepalimonth_name(self):
        self.assertEqual(nepalimonth(1).name, "Baishakh")
        self.assertEqual(nepalimonth(12).name, "Chaitra")

    def test_nepalimonth_name_ne(self):
        self.assertEqual(nepalimonth(1).name_ne, "बैशाख")
        self.assertEqual(nepalimonth(12).name_ne, "चैत")

    def test_nepalimonth_variable_cache(self):
        self.assertEqual(id(nepalimonth(1)), id(nepalimonth(1)))
        self.assertEqual(id(nepalimonth(12)), id(nepalimonth(12)))

    def test_nepalimonth_int(self):
        self.assertEqual(int(nepalimonth(1)), 1)
        self.assertEqual(int(nepalimonth(12)), 12)

    def test_nepalimonth_equal_with_nepalimonth(self):
        self.assertEqual(nepalimonth(1), nepalimonth(1))
        self.assertEqual(nepalimonth(12), nepalimonth(12))

    def test_nepalimonth_not_equal(self):
        self.assertNotEqual(nepalimonth(1), nepalimonth(2))
        self.assertNotEqual(nepalimonth(1), 2)

    def test_nepalimonth_equal_with_int(self):
        self.assertEqual(nepalimonth(1), 1)
        self.assertEqual(nepalimonth(12), 12)
        self.assertEqual(1, nepalimonth(1))
        self.assertEqual(12, nepalimonth(12))

    def test_nepalimonth_not_equal_with_invalid_object(self):
        self.assertNotEqual(nepalimonth(1), "invalid")
