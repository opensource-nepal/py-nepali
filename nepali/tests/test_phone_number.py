import unittest
from unittest import mock

from nepali.phone_number import (
    _get_area_code,
    _get_operator,
    _parse_landline_number,
    _parse_mobile_number,
    is_mobile_number,
    is_landline_number,
    is_valid,
    get_exact_number,
    parse,
    Operator,
)


class TestOperator(unittest.TestCase):
    def test_operator_with_invalid_data(self):
        with self.assertRaises(ValueError):
            Operator("Hello")

    def test_operator_with_valid_data(self):
        operator = Operator("Nepal Telecom")
        self.assertEqual(operator, Operator.NEPAL_TELECOM)

    def test_operator_str(self):
        operator = Operator.NEPAL_TELECOM
        self.assertEqual(str(operator), operator.value)

    def test_operator_repr(self):
        operator = Operator.NEPAL_TELECOM
        self.assertEqual(repr(operator), f"<Operator: {operator.value}>")


class TestPhoneNumberValidation(unittest.TestCase):
    def test_is_mobile_number(self):
        # True case
        self.assertEqual(is_mobile_number("9779842536789"), True)
        self.assertEqual(is_mobile_number("+9779842536789"), True)
        self.assertEqual(is_mobile_number("+977-9842536789"), True)
        self.assertEqual(is_mobile_number("9842536789"), True)
        self.assertEqual(is_mobile_number("9852536789"), True)
        self.assertEqual(is_mobile_number("9862536789"), True)
        self.assertEqual(is_mobile_number("9742536789"), True)
        self.assertEqual(is_mobile_number("9752536789"), True)
        self.assertEqual(is_mobile_number("9802536789"), True)
        self.assertEqual(is_mobile_number("9812536789"), True)
        self.assertEqual(is_mobile_number("9822536789"), True)
        self.assertEqual(is_mobile_number("9612536789"), True)
        self.assertEqual(is_mobile_number("9622536789"), True)
        self.assertEqual(is_mobile_number("9882536789"), True)
        self.assertEqual(is_mobile_number("9722536789"), True)
        self.assertEqual(is_mobile_number("9632536789"), True)

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
        self.assertEqual(is_landline_number("021420451"), True)
        self.assertEqual(is_landline_number("21420451"), True)
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
    def test_if__is_valid__returns_true_if_both_mobile_and_landline_returns_true(
        self, *_
    ):
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


class TestMobileNumberParser(unittest.TestCase):
    def test__get_operator__with_invalid_input(self):
        self.assertEqual(_get_operator("Hello there"), None)

    def test__get_operator__with_not_matching_input(self):
        self.assertEqual(_get_operator("9132536789"), None)

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

    @mock.patch("nepali.phone_number._get_operator", return_value="test")
    def test__parse_mobile_number_returns_valid_data(self, *_):
        data = _parse_mobile_number("+977-9842536789")
        self.assertEqual(data and data["type"], "Mobile")
        self.assertEqual(data and data["operator"], "test")
        self.assertEqual(data and data["number"], "9842536789")

    @mock.patch("nepali.phone_number._get_operator", return_value=None)
    def test__parse_mobile_number_on_invalid_operator(self, *_):
        data = _parse_mobile_number("+977-14231481")
        self.assertEqual(data, None)


class TestLandlineNumberParser(unittest.TestCase):
    def test__get_area_code_for_kathmandu(self):
        self.assertEqual(_get_area_code("0142314819"), "01")
        self.assertEqual(_get_area_code("0154225639"), "01")

    def test__get_area_code_for_biratnagar(self):
        self.assertEqual(_get_area_code("021420431"), "021")

    def test__get_area_code_for_chitwan(self):
        self.assertEqual(_get_area_code("056520198"), "056")

    def test__get_area_code_for_jhapa(self):
        self.assertEqual(_get_area_code("023455125"), "023")

    def test__get_area_code_for_rupandehi(self):
        self.assertEqual(_get_area_code("071540029"), "071")

    def test__get_area_code_for_kaski(self):
        self.assertEqual(_get_area_code("061463076"), "061")

    def test__get_area_code_for_dhading(self):
        self.assertEqual(_get_area_code("010520133"), "010")

    def test__get_area_code_for_syangja(self):
        self.assertEqual(_get_area_code("063420211"), "063")

    @mock.patch("nepali.phone_number._get_area_code", return_value="test")
    def test__parse_landline_number_returns_valid_data(self, *_):
        data = _parse_landline_number("0142314819")
        self.assertEqual(data["type"], "Landline")
        self.assertEqual(data["area_code"], "test")
        self.assertEqual(data["number"], "0142314819")

    @mock.patch("nepali.phone_number._get_area_code", return_value="test")
    def test__parse_landline_number_returns_valid_data_for_977(self, *_):
        data = _parse_landline_number("+977142314819")
        self.assertEqual(data["type"], "Landline")
        self.assertEqual(data["area_code"], "test")
        self.assertEqual(data["number"], "0142314819")


class TestParser(unittest.TestCase):
    def test_none_number_returns_none(self):
        self.assertEqual(parse(None), None)  # type: ignore

    def test_empty_number_returns_none(self):
        self.assertEqual(parse(""), None)

    @mock.patch("nepali.phone_number.is_mobile_number", return_value=True)
    @mock.patch("nepali.phone_number._parse_mobile_number", return_value="Mobile")
    def test_mobile_number_parsing(self, *_):
        self.assertEqual(parse("number"), "Mobile")

    @mock.patch("nepali.phone_number.is_mobile_number", return_value=False)
    @mock.patch("nepali.phone_number.is_landline_number", return_value=True)
    @mock.patch("nepali.phone_number._parse_landline_number", return_value="Landline")
    def test_landline_number_parsing(self, *_):
        self.assertEqual(parse("number"), "Landline")

    @mock.patch("nepali.phone_number.is_mobile_number", return_value=False)
    @mock.patch("nepali.phone_number.is_landline_number", return_value=False)
    def test_invalid_number_returns_none(self, *_):
        self.assertEqual(parse("number"), None)


class TestParseIntegration(unittest.TestCase):
    def test_parse_for_mobile_number(self):
        data = parse("+9779842536789")
        self.assertEqual(data and data["type"], "Mobile")
        self.assertEqual(data and data["number"], "9842536789")
        self.assertEqual(data and data["operator"], Operator.NEPAL_TELECOM)

    def test_parse_for_landline_number(self):
        data = parse("+977-142314819")
        self.assertEqual(data and data["type"], "Landline")
        self.assertEqual(data and data["number"], "0142314819")
        self.assertEqual(data and data["area_code"], "01")
