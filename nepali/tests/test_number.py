"""
To run only this unit test use the command below.

    python -m unittest nepali/tests/test_number.py -v
"""
import unittest

from nepali import number
from nepali.number import nepalinumber


NepaliNumber = number.NepaliNumber


class TestNumber(unittest.TestCase):
    def test_number_english_to_nepali(self):
        self.assertEqual(
            number.english_to_nepali("0123456789०१२३४५६७८९hello"),
            "०१२३४५६७८९०१२३४५६७८९hello",
        )
        self.assertEqual(
            NepaliNumber.convert("0123456789०१२३४५६७८९"), "०१२३४५६७८९०१२३४५६७८९"
        )

    def test_number_nepali_to_english(self):
        self.assertEqual(
            number.nepali_to_english("0123456789०१२३४५६७८९hello"),
            "01234567890123456789hello",
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


class TestNepaliNumberParse(unittest.TestCase):
    def test_nepalinumber_parse_int(self):
        num = nepalinumber(13)
        self.assertEqual(num.value, 13)
        self.assertEqual(type(num.value), int)

    def test_nepalinumber_parse_int_negative(self):
        num = nepalinumber(-13)
        self.assertEqual(num.value, -13)
        self.assertEqual(type(num.value), int)

    def test_nepalinumber_parse_float(self):
        num = nepalinumber(13.07)
        self.assertEqual(num.value, 13.07)
        self.assertEqual(type(num.value), float)

    def test_nepalinumber_parse_float_negative(self):
        num = nepalinumber(-13.07)
        self.assertEqual(num.value, -13.07)
        self.assertEqual(type(num.value), float)

    def test_nepalinumber_parse_str_int(self):
        num = nepalinumber("13")
        self.assertEqual(num.value, 13)
        self.assertEqual(type(num.value), int)

    def test_nepalinumber_parse_str_int_negative(self):
        num = nepalinumber("-13")
        self.assertEqual(num.value, -13)
        self.assertEqual(type(num.value), int)

    def test_nepalinumber_parse_str_float(self):
        num = nepalinumber("13.07")
        self.assertEqual(num.value, 13.07)
        self.assertEqual(type(num.value), float)

    def test_nepalinumber_parse_str_float_negative(self):
        num = nepalinumber("-13.07")
        self.assertEqual(num.value, -13.07)
        self.assertEqual(type(num.value), float)

    def test_nepalinumber_parse_str_float_starting_dot(self):
        num = nepalinumber(".07")
        self.assertEqual(num.value, 0.07)
        self.assertEqual(type(num.value), float)

    def test_nepalinumber_parse_str_float_starting_dot_and_negative(self):
        num = nepalinumber("-.07")
        self.assertEqual(num.value, -0.07)
        self.assertEqual(type(num.value), float)

    def test_nepalinumber_parse_str_nepali_int(self):
        num = nepalinumber("१३")
        self.assertEqual(num.value, 13)
        self.assertEqual(type(num.value), int)

    def test_nepalinumber_parse_str_nepali_int_negative(self):
        num = nepalinumber("-१३")
        self.assertEqual(num.value, -13)
        self.assertEqual(type(num.value), int)

    def test_nepalinumber_parse_str_nepali_float(self):
        num = nepalinumber("१३.०७")
        self.assertEqual(num.value, 13.07)
        self.assertEqual(type(num.value), float)

    def test_nepalinumber_parse_str_nepali_float_negative(self):
        num = nepalinumber("-१३.०७")
        self.assertEqual(num.value, -13.07)
        self.assertEqual(type(num.value), float)

    def test_nepalinumber_raises_exception_for_chars_english(self):
        with self.assertRaises(ValueError) as ex:
            nepalinumber("invalid")
        self.assertEqual(
            str(ex.exception), "could not convert str to nepalinumber: 'invalid'"
        )

    def test_nepalinumber_raises_exception_for_chars_nepali(self):
        with self.assertRaises(ValueError) as ex:
            nepalinumber("आइतबार")

    def test_nepalinumber_raises_exception_for_two_dots(self):
        with self.assertRaises(ValueError) as ex:
            nepalinumber("10..5")

    def test_nepalinumber_raises_exception_for_nepali_aplha(self):
        with self.assertRaises(ValueError) as ex:
            nepalinumber("10..5")

    def test_nepalinumber_raises_exception_for_special_chars(self):
        with self.assertRaises(ValueError) as ex:
            nepalinumber("!@#$%^&*()-+")

    def test_nepalinumber_raise_exception_for_number_with_spaces(self):
        with self.assertRaises(ValueError) as ex:
            nepalinumber("10 20")

    def test_nepalinumber_raises_exception_on_complex_number(self):
        with self.assertRaises(TypeError) as ex:
            nepalinumber(3 + 2j)
        self.assertEqual(
            str(ex.exception), "could not convert complex to nepalinumber: '(3+2j)'"
        )

    # Object parsing
    def test_nepalinumber_parse_object_with_int(self):
        class _test:
            def __int__(self):
                return 13

        num = nepalinumber(_test())
        self.assertEqual(num.value, int(_test()))
        self.assertEqual(type(num.value), int)

    def test_nepalinumber_parse_object_with_float(self):
        class _test:
            def __float__(self):
                return 13.07

        num = nepalinumber(_test())
        self.assertEqual(num.value, float(_test()))
        self.assertEqual(type(num.value), float)

    def test_nepalinumber_parse_object_with_float_and_int(self):
        class _test:
            def __int__(self):
                return 13

            def __float__(self):
                return 13.07

        num = nepalinumber(_test())
        self.assertNotEqual(num.value, int(_test()))
        self.assertEqual(num.value, float(_test()))
        self.assertEqual(type(num.value), float)

    def test_nepalinumber_parse_object_with_valid_number_str_int(self):
        class _test:
            def __str__(self):
                return "13"

        num = nepalinumber(_test())
        self.assertEqual(num.value, int(str(_test())))
        self.assertEqual(type(num.value), int)

    def test_nepalinumber_parse_object_with_valid_number_str_float(self):
        class _test:
            def __str__(self):
                return "13.07"

        num = nepalinumber(_test())
        self.assertEqual(num.value, float(str(_test())))
        self.assertEqual(type(num.value), float)

    def test_nepalinumber_raises_exception_for_invalid_object(self):
        class _test:
            def __str__(self):
                return "13-03"

        with self.assertRaises(TypeError) as ex:
            nepalinumber(_test())
        self.assertEqual(
            str(ex.exception), "could not convert _test to nepalinumber: '13-03'"
        )

    # parsing inheritance with float and int
    def test_nepalinumber_parses_inherited_int(self):
        class _test(int):
            pass

        num = nepalinumber(_test(13))
        self.assertEqual(num.value, 13)
        self.assertEqual(type(num.value), int)

    def test_nepalinumber_parses_inherited_float(self):
        class _test(float):
            pass

        num = nepalinumber(_test(13.07))
        self.assertEqual(num.value, 13.07)
        self.assertEqual(type(num.value), float)
