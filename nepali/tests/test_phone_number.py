"""
NOTE: To run only this test case use the below command
python setup.py test -s nepali.tests.test_phone_number
"""
import unittest
from unittest import mock

from nepali.phone_number import (_get_operator, _parse_mobile_number, is_mobile_number, is_landline_number,
                                 is_valid, get_exact_number, parse, Operator)


class TestPhoneNumberValidation(unittest.TestCase):
    def test_is_mobile_number(self):
        # True case
        self.assertEqual(is_mobile_number("9842536789"), True)
        self.assertEqual(is_mobile_number("9779842536789"), True)
        self.assertEqual(is_mobile_number("+9779842536789"), True)
        self.assertEqual(is_mobile_number("+977-9842536789"), True)
        self.assertEqual(is_mobile_number("9851088967"), True)
        self.assertEqual(is_mobile_number("9751088967"), True)
        self.assertEqual(is_mobile_number("9651088967"), True)

        # False case
        self.assertEqual(is_mobile_number(None), False)  # type: ignore
        self.assertEqual(is_mobile_number(""), False)
        self.assertEqual(is_mobile_number("test"), False)
        self.assertEqual(is_mobile_number("977test"), False)
        self.assertEqual(is_mobile_number("+977test"), False)
        self.assertEqual(is_mobile_number("+977-test"), False)
        self.assertEqual(is_mobile_number("9551088967"), False)
        self.assertEqual(is_mobile_number("+977-98425367899"), False)
        self.assertEqual(is_mobile_number("+977-984253678"), False)
        self.assertEqual(is_mobile_number("984253678"), False)
        self.assertEqual(is_mobile_number("98425367899"), False)

    def test_is_landline_number(self):
        # True case
        self.assertEqual(is_landline_number("14231481"), True)
        self.assertEqual(is_landline_number("014231481"), True)
        self.assertEqual(is_landline_number("0215154579"), True)
        self.assertEqual(is_landline_number("+977-142314819"), True)
        self.assertEqual(is_landline_number("0154225639"), True)
        self.assertEqual(is_landline_number("9770154225639"), True)
        self.assertEqual(is_landline_number("0565114679"), True)
        self.assertEqual(is_landline_number("+977-0565114679"), True)

        # False case
        self.assertEqual(is_landline_number(None), False)  # type: ignore
        self.assertEqual(is_landline_number(""), False)
        self.assertEqual(is_landline_number("test"), False)
        self.assertEqual(is_landline_number("977test"), False)
        self.assertEqual(is_landline_number("+977test"), False)
        self.assertEqual(is_landline_number("+977-test"), False)

    @mock.patch("nepali.phone_number.is_landline_number", return_value=False)
    @mock.patch("nepali.phone_number.is_mobile_number", return_value=False)
    def test_if__is_valid__returns_false_for_invalid_numbers(self, *_):
        self.assertEqual(is_valid("who_cares"), False)

    @mock.patch("nepali.phone_number.is_landline_number", return_value=True)
    @mock.patch("nepali.phone_number.is_mobile_number", return_value=False)
    def test_if__is_valid__returns_true_for_landline(self, *_):
        self.assertEqual(is_valid("who_cares"), True)

    @mock.patch("nepali.phone_number.is_landline_number", return_value=False)
    @mock.patch("nepali.phone_number.is_mobile_number", return_value=True)
    def test_if__is_valid__returns_true_for_mobile(self, *_):
        self.assertEqual(is_valid("who_cares"), True)

    @mock.patch("nepali.phone_number.is_landline_number", return_value=True)
    @mock.patch("nepali.phone_number.is_mobile_number", return_value=True)
    def test_if__is_valid__returns_true_if_both_mobile_and_landline_returns_true(self, *_):
        self.assertEqual(is_valid("who_cares"), True)


class TestPhoneNumberFunctions(unittest.TestCase):
    def test_get_exact_number(self):
        self.assertEqual(get_exact_number("9842536789"), "9842536789")
        self.assertEqual(get_exact_number("9779842536789"), "9842536789")
        self.assertEqual(get_exact_number("+9779842536789"), "9842536789")
        self.assertEqual(get_exact_number("+977-9842536789"), "9842536789")
        self.assertEqual(get_exact_number(""), "")
        self.assertEqual(get_exact_number("test"), "test")
        self.assertEqual(get_exact_number("977test"), "test")
        self.assertEqual(get_exact_number("+977test"), "test")
        self.assertEqual(get_exact_number("+977-test"), "test")
        self.assertEqual(get_exact_number("+977-142314819"), "142314819")
        self.assertEqual(get_exact_number("0154225639"), "0154225639")
        self.assertEqual(get_exact_number("9770154225639"), "0154225639")
        self.assertEqual(get_exact_number("0565114679"), "0565114679")
        self.assertEqual(get_exact_number("984-2536789"), "9842536789")
        self.assertEqual(get_exact_number("984-2536-789"), "9842536789")
        with self.assertRaises(AttributeError):
            get_exact_number(None)  # type: ignore


class TestPhoneNumberParser(unittest.TestCase):
    def test__get_operator__for_ntc(self):
        self.assertEqual(_get_operator("9842536789"), Operator.NEPAL_TELECOM)
        self.assertEqual(_get_operator("9852536789"), Operator.NEPAL_TELECOM)
        self.assertEqual(_get_operator("9862536789"), Operator.NEPAL_TELECOM)
        # For CDMA (Nepal Telecom)
        self.assertEqual(_get_operator("9742536789"), Operator.NEPAL_TELECOM)
        self.assertEqual(_get_operator("9752536789"), Operator.NEPAL_TELECOM)

    def test__get_operator__for_ncell(self):
        self.assertEqual(_get_operator("9802536789"), Operator.NCELL)
        self.assertEqual(_get_operator("9812536789"), Operator.NCELL)
        self.assertEqual(_get_operator("9822536789"), Operator.NCELL)

    def test__get_operator__for_smart_cell(self):
        self.assertEqual(_get_operator("9612536789"), Operator.SMART_CELL)
        self.assertEqual(_get_operator("9622536789"), Operator.SMART_CELL)
        self.assertEqual(_get_operator("9882536789"), Operator.SMART_CELL)

    def test__get_operator__for_utl(self):
        self.assertEqual(_get_operator("9722536789"), Operator.UTL)

    def test__get_operator__for_hello_mobile(self):
        self.assertEqual(_get_operator("9632536789"), Operator.HELLO_MOBILE)

    @mock.patch("nepali.phone_number._get_operator", return_value='test')
    def test__parse_mobile_number_returns_valid_data(self, *args):
        data = _parse_mobile_number("+977-9842536789")
        self.assertEqual(data["type"], "Mobile")
        self.assertEqual(data["operator"], "test")
        self.assertEqual(data["number"], "9842536789")

    @mock.patch("nepali.phone_number._get_operator", return_value=None)
    def test__parse_mobile_number_on_invalid_operator(self, *args):
        data = _parse_mobile_number("+977-983174499")
        self.assertEqual(data, None)


class TestParseIntegration(unittest.TestCase):
    def test_parse_for_mobile_number(self):
        data = parse("+9779842536789")
        self.assertEqual(data["type"], "Mobile")
        self.assertEqual(data["operator"], Operator.NEPAL_TELECOM)
        self.assertEqual(data["number"], "9842536789")
