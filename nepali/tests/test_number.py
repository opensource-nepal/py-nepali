"""
To run only this unit test use the command below.

    python -m unittest nepali/tests/test_number.py -v
"""
import sys
import unittest

from nepali import number
from nepali.number import nepalinumber, NepaliNumber


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


# to run this test suite exclusively
# python -m unittest nepali.tests.test_number.TestNepaliNumber -v
class TestNepaliNumberArithmeticOperations(unittest.TestCase):
    """
    Contains test cases related to nepalinumber
    arithmetic operations
    """

    @classmethod
    def setUpClass(cls):
        """
        Test fixtures
        """
        # positive integers
        cls.nepalinumber_integer_20 = number.nepalinumber(20)
        cls.nepalinumber_integer_15 = number.nepalinumber(15)
        cls.nepalinumber_integer_11 = number.nepalinumber(11)
        cls.nepalinumber_integer_10 = number.nepalinumber(10)
        cls.nepalinumber_integer_5 = number.nepalinumber(5)
        cls.nepalinumber_integer_4 = number.nepalinumber(4)
        cls.nepalinumber_integer_3 = number.nepalinumber(3)
        cls.nepalinumber_integer_2 = number.nepalinumber(2)
        cls.nepalinumber_integer_1 = number.nepalinumber(1)
        # positive floats
        cls.nepalinumber_float_21_21 = number.nepalinumber(21.21)
        cls.nepalinumber_float_20_2 = number.nepalinumber(20.2)
        cls.nepalinumber_float_20_1 = number.nepalinumber(20.1)
        cls.nepalinumber_float_15_6 = number.nepalinumber(15.6)
        cls.nepalinumber_float_15_5 = number.nepalinumber(15.5)
        cls.nepalinumber_float_10_9 = number.nepalinumber(10.9)
        cls.nepalinumber_float_10_0_cont = number.nepalinumber(
            20.1 - 10.1
        )  # 10.000...2
        cls.nepalinumber_float_10_1 = number.nepalinumber(10.1)
        cls.nepalinumber_float_9_9 = number.nepalinumber(9.9)
        cls.nepalinumber_float_5_5 = number.nepalinumber(5.5)
        cls.nepalinumber_float_5_25 = number.nepalinumber(5.25)
        cls.nepalinumber_float_4_6 = number.nepalinumber(4.6)
        cls.nepalinumber_float_4_5 = number.nepalinumber(4.5)
        cls.nepalinumber_float_3_5 = number.nepalinumber(3.5)
        cls.nepalinumber_float_2_5 = number.nepalinumber(2.5)
        cls.nepalinumber_float_2_25 = number.nepalinumber(2.25)
        cls.nepalinumber_float_1_5 = number.nepalinumber(1.5)
        cls.nepalinumber_float_1_25 = number.nepalinumber(1.25)
        cls.nepalinumber_float_0_5 = number.nepalinumber(0.5)
        cls.nepalinumber_float_0_1 = number.nepalinumber(0.1)
        cls.nepalinumber_float_0_0_9 = number.nepalinumber(
            10.1 - 10
        )  # to lazy to type 0.099...
        # negative numbers
        cls.nepalinumber_negative_integer_20 = number.nepalinumber(-20)
        cls.nepalinumber_negative_integer_15 = number.nepalinumber(-15)
        cls.nepalinumber_negative_integer_11 = number.nepalinumber(-11)
        cls.nepalinumber_negative_integer_10 = number.nepalinumber(-10)
        cls.nepalinumber_negative_integer_5 = number.nepalinumber(-5)
        cls.nepalinumber_negative_integer_4 = number.nepalinumber(-4)
        cls.nepalinumber_negative_integer_3 = number.nepalinumber(-3)
        cls.nepalinumber_negative_integer_2 = number.nepalinumber(-2)
        cls.nepalinumber_negative_integer_1 = number.nepalinumber(-1)
        # negative floats
        cls.nepalinumber_negative_float_21_21 = number.nepalinumber(-21.21)
        cls.nepalinumber_negative_float_20_2 = number.nepalinumber(-20.2)
        cls.nepalinumber_negative_float_20_1 = number.nepalinumber(-20.1)
        cls.nepalinumber_negative_float_20_0 = number.nepalinumber(-20.0)
        cls.nepalinumber_negative_float_15_6 = number.nepalinumber(-15.6)
        cls.nepalinumber_negative_float_15_5 = number.nepalinumber(-15.5)
        cls.nepalinumber_negative_float_10_1 = number.nepalinumber(-10.1)
        cls.nepalinumber_negative_float_9_9 = number.nepalinumber(-9.9)
        cls.nepalinumber_negative_float_5_5 = number.nepalinumber(-5.5)
        cls.nepalinumber_negative_float_5_4 = number.nepalinumber(-5.4)
        cls.nepalinumber_negative_float_4_5 = number.nepalinumber(-4.5)
        cls.nepalinumber_negative_float_2_5 = number.nepalinumber(-2.5)
        cls.nepalinumber_negative_float_2_25 = number.nepalinumber(-2.25)
        cls.nepalinumber_negative_float_1_5 = number.nepalinumber(-1.5)
        cls.nepalinumber_negative_float_1_25 = number.nepalinumber(-1.25)
        cls.nepalinumber_negative_float_0_5 = number.nepalinumber(-0.5)
        cls.nepalinumber_negative_float_0_0_9 = number.nepalinumber(
            10 - 10.1
        )  # to lazy to type -0.099...
        # zero
        cls.nepalinumber_zero = number.nepalinumber(0)
        # objects
        cls.random_object = object
        # string
        cls.random_string = "test"

    # addition
    # nepalinumber positive integer addition tests
    def test_nepalinumber_integer_is_addable_to_positive_integer(self):
        self.assertEqual(
            self.nepalinumber_integer_10 + 10, self.nepalinumber_integer_20
        )

    def test_nepalinumber_integer_is_addable_to_positive_float(self):
        self.assertEqual(
            self.nepalinumber_integer_10 + 10.1, self.nepalinumber_float_20_1
        )

    def test_nepalinumber_integer_is_addable_to_negative_integer(self):
        self.assertEqual(self.nepalinumber_integer_10 + (-10), self.nepalinumber_zero)

    def test_nepalinumber_integer_is_addable_to_negative_integer_to_give_negative_nepali_integer(
        self,
    ):
        self.assertEqual(
            self.nepalinumber_integer_10 + (-20), self.nepalinumber_negative_integer_10
        )

    def test_nepalinumber_integer_is_addable_to_negative_float(self):
        self.assertEqual(
            self.nepalinumber_integer_10 + (-5.5), self.nepalinumber_float_4_5
        )

    def test_nepalinumber_integer_is_addable_to_negative_float_to_give_negative_nepali_float(
        self,
    ):
        self.assertEqual(
            self.nepalinumber_integer_10 + (-15.5), self.nepalinumber_negative_float_5_5
        )

    def test_nepalinumber_integer_is_addable_to_postive_nepali_number_integer(self):
        self.assertEqual(
            self.nepalinumber_integer_10 + self.nepalinumber_integer_10,
            self.nepalinumber_integer_20,
        )

    def test_nepalinumber_integer_is_addable_to_positive_nepali_number_float(self):
        self.assertEqual(
            self.nepalinumber_integer_10 + self.nepalinumber_float_10_1,
            self.nepalinumber_float_20_1,
        )

    def test_nepalinumber_integer_is_addable_to_negative_nepali_number_integer(self):
        self.assertEqual(
            self.nepalinumber_integer_10 + self.nepalinumber_negative_integer_10,
            self.nepalinumber_zero,
        )

    def test_nepalinumber_integer_is_addable_to_negative_nepali_number_integer_to_give_negative_nepali_number(
        self,
    ):
        self.assertEqual(
            self.nepalinumber_integer_10 + self.nepalinumber_negative_integer_20,
            self.nepalinumber_negative_integer_10,
        )

    def test_nepalinumber_integer_is_addable_to_negative_nepali_number_float(self):
        self.assertEqual(
            self.nepalinumber_integer_10 + self.nepalinumber_negative_float_5_5,
            self.nepalinumber_float_4_5,
        )

    def test_nepalinumber_integer_is_addable_to_negative_nepali_number_float_to_give_negative_nepali_number(
        self,
    ):
        self.assertEqual(
            self.nepalinumber_integer_10 + self.nepalinumber_negative_float_15_5,
            self.nepalinumber_negative_float_5_5,
        )

    # adding the nepali number to other numbers tests
    def test_positive_integer_is_addable_to_nepalinumber_integer(self):
        self.assertEqual(
            10 + self.nepalinumber_integer_10, self.nepalinumber_integer_20
        )

    def test_positive_float_is_addable_to_nepalinumber_integer(self):
        self.assertEqual(
            10.1 + self.nepalinumber_integer_10, self.nepalinumber_float_20_1
        )

    def test_negative_integer_is_addable_to_nepalinumber_integer(self):
        self.assertEqual(-10 + self.nepalinumber_integer_10, self.nepalinumber_zero)

    def test_negative_integer_is_addable_to_nepalinumber_integer_to_give_negative_nepali_integer(
        self,
    ):
        self.assertEqual(
            (-20) + self.nepalinumber_integer_10, self.nepalinumber_negative_integer_10
        )

    def test_negative_float_is_addable_to_nepalinumber_integer(self):
        self.assertEqual(
            (-5.5) + self.nepalinumber_integer_10, self.nepalinumber_float_4_5
        )

    def test_negative_float_is_addable_to_nepalinumber_integer_to_give_negative_nepali_float(
        self,
    ):
        self.assertEqual(
            (-15.5) + self.nepalinumber_integer_10, self.nepalinumber_negative_float_5_5
        )

    # nepalinumber negative integer addition tests
    def test_negative_nepalinumber_integer_is_addable_to_positive_integer(self):
        self.assertEqual(
            self.nepalinumber_negative_integer_10 + 10, self.nepalinumber_zero
        )

    def test_negative_nepalinumber_integer_is_addable_to_positive_float(self):
        self.assertEqual(
            self.nepalinumber_negative_integer_10 + 10.1, self.nepalinumber_float_0_0_9
        )

    def test_negative_nepalinumber_integer_is_addable_to_positive_integer_to_give_positive_nepali_integer(
        self,
    ):
        self.assertEqual(
            self.nepalinumber_negative_integer_10 + 20, self.nepalinumber_integer_10
        )

    def test_negative_nepalinumber_integer_is_addable_to_negative_integer(self):
        self.assertEqual(
            self.nepalinumber_negative_integer_10 + (-10),
            self.nepalinumber_negative_float_20_0,
        )

    def test_negative_nepalinumber_integer_is_addable_to_negative_float(self):
        self.assertEqual(
            self.nepalinumber_negative_integer_10 + (-5.5),
            self.nepalinumber_negative_float_15_5,
        )

    def test_negative_nepalinumber_integer_is_addable_to_positive_float_to_give_positive_nepali_float(
        self,
    ):
        self.assertEqual(
            self.nepalinumber_negative_integer_10 + 15.5, self.nepalinumber_float_5_5
        )

    def test_negative_nepalinumber_integer_is_addable_to_postive_nepali_number_integer(
        self,
    ):
        self.assertEqual(
            self.nepalinumber_negative_integer_10 + self.nepalinumber_integer_10,
            self.nepalinumber_zero,
        )

    def test_negative_nepalinumber_integer_is_addable_to_positive_nepali_number_float(
        self,
    ):
        self.assertEqual(
            self.nepalinumber_negative_integer_10 + self.nepalinumber_float_10_1,
            self.nepalinumber_float_0_0_9,
        )

    def test_negative_nepalinumber_integer_is_addable_to_negative_nepali_number_integer(
        self,
    ):
        self.assertEqual(
            self.nepalinumber_negative_integer_10
            + self.nepalinumber_negative_integer_10,
            self.nepalinumber_negative_integer_20,
        )

    def test_negative_nepalinumber_integer_is_addable_to_positive_nepali_number_integer_to_give_positive_nepali_number(
        self,
    ):
        self.assertEqual(
            self.nepalinumber_negative_integer_10 + self.nepalinumber_integer_20,
            self.nepalinumber_integer_10,
        )

    def test_negative_nepalinumber_integer_is_addable_to_negative_nepali_number_float(
        self,
    ):
        self.assertEqual(
            self.nepalinumber_negative_integer_10
            + self.nepalinumber_negative_float_5_5,
            self.nepalinumber_negative_float_15_5,
        )

    def test_nepalinumber_integer_is_addable_to_positive_nepali_number_float_to_give_positive_nepali_number(
        self,
    ):
        self.assertEqual(
            self.nepalinumber_negative_float_10_1 + self.nepalinumber_float_20_1,
            self.nepalinumber_float_10_0_cont,
        )

    # nepalinumber positive float addition tests
    def test_nepalinumber_float_is_addable_to_positive_integer(self):
        self.assertEqual(
            self.nepalinumber_float_10_1 + 10, self.nepalinumber_float_20_1
        )

    def test_nepalinumber_float_is_addable_to_positive_float(self):
        self.assertEqual(
            self.nepalinumber_float_10_1 + 10.1, self.nepalinumber_float_20_2
        )

    def test_nepalinumber_float_is_addable_to_negative_integer(self):
        self.assertEqual(
            self.nepalinumber_float_10_1 + (-10), self.nepalinumber_float_0_0_9
        )

    def test_nepalinumber_float_is_addable_to_negative_integer_to_give_negative_nepali_integer(
        self,
    ):
        self.assertEqual(
            self.nepalinumber_float_10_9 + (-21), self.nepalinumber_negative_float_10_1
        )

    def test_nepalinumber_float_is_addable_to_negative_float(self):
        self.assertEqual(
            self.nepalinumber_float_10_1 + (-5.6), self.nepalinumber_float_4_5
        )

    def test_nepalinumber_float_is_addable_to_negative_float_to_give_negative_nepali_float(
        self,
    ):
        self.assertEqual(
            self.nepalinumber_float_10_1 + (-15.6), self.nepalinumber_negative_float_5_5
        )

    def test_nepalinumber_float_is_addable_to_postive_nepali_number_integer(self):
        self.assertEqual(
            self.nepalinumber_float_10_1 + self.nepalinumber_integer_10,
            self.nepalinumber_float_20_1,
        )

    def test_nepalinumber_float_is_addable_to_positive_nepali_number_float(self):
        self.assertEqual(
            self.nepalinumber_float_10_1 + self.nepalinumber_float_10_1,
            self.nepalinumber_float_20_2,
        )

    def test_nepalinumber_float_is_addable_to_negative_nepali_number_integer(self):
        self.assertEqual(
            self.nepalinumber_float_10_1 + self.nepalinumber_negative_integer_10,
            self.nepalinumber_float_0_0_9,
        )

    def test_nepalinumber_float_is_addable_to_negative_nepali_number_integer_to_give_negative_nepali_number(
        self,
    ):
        self.assertEqual(
            self.nepalinumber_float_10_1 + self.nepalinumber_negative_integer_20,
            self.nepalinumber_negative_float_9_9,
        )

    def test_nepalinumber_float_is_addable_to_negative_nepali_number_float(self):
        self.assertEqual(
            self.nepalinumber_float_10_1 + self.nepalinumber_negative_float_5_5,
            self.nepalinumber_float_4_6,
        )

    def test_nepalinumber_float_is_addable_to_negative_nepali_number_float_to_give_negative_nepali_number(
        self,
    ):
        self.assertEqual(
            self.nepalinumber_float_10_1 + self.nepalinumber_negative_float_15_5,
            self.nepalinumber_negative_float_5_4,
        )

    # nepalinumber negative float addition tests
    def test_negative_nepalinumber_float_is_addable_to_positive_integer(self):
        self.assertEqual(
            self.nepalinumber_negative_float_10_1 + 10,
            self.nepalinumber_negative_float_0_0_9,
        )

    def test_negative_nepalinumber_float_is_addable_to_positive_float(self):
        self.assertEqual(
            self.nepalinumber_negative_float_10_1 + 10.1, self.nepalinumber_zero
        )

    def test_negative_nepalinumber_float_is_addable_to_positive_integer_to_give_positive_nepali_float(
        self,
    ):
        self.assertEqual(
            self.nepalinumber_negative_float_10_1 + 20, self.nepalinumber_float_9_9
        )

    def test_negative_nepalinumber_float_is_addable_to_negative_integer(self):
        self.assertEqual(
            self.nepalinumber_negative_float_10_1 + (-10),
            self.nepalinumber_negative_float_20_1,
        )

    def test_negative_nepalinumber_float_is_addable_to_negative_float(self):
        self.assertEqual(
            self.nepalinumber_negative_float_10_1 + (-5.4),
            self.nepalinumber_negative_float_15_5,
        )

    def test_negative_nepalinumber_float_is_addable_to_positive_float_to_give_positive_nepali_float(
        self,
    ):
        self.assertEqual(
            self.nepalinumber_negative_float_10_1 + 15.6, self.nepalinumber_float_5_5
        )

    def test_negative_nepalinumber_float_is_addable_to_postive_nepali_number_integer(
        self,
    ):
        self.assertEqual(
            self.nepalinumber_negative_float_10_1 + self.nepalinumber_integer_10,
            self.nepalinumber_negative_float_0_0_9,
        )

    def test_negative_nepalinumber_float_is_addable_to_positive_nepali_number_float(
        self,
    ):
        self.assertEqual(
            self.nepalinumber_negative_float_10_1 + self.nepalinumber_float_10_1,
            self.nepalinumber_zero,
        )

    def test_negative_nepalinumber_float_is_addable_to_negative_nepali_number_integer(
        self,
    ):
        self.assertEqual(
            self.nepalinumber_negative_float_10_1
            + self.nepalinumber_negative_integer_10,
            self.nepalinumber_negative_float_20_1,
        )

    def test_negative_nepalinumber_float_is_addable_to_positive_nepali_number_integer_to_give_positive_nepali_number(
        self,
    ):
        self.assertEqual(
            self.nepalinumber_negative_float_10_1 + self.nepalinumber_integer_20,
            self.nepalinumber_float_9_9,
        )

    def test_negative_nepalinumber_float_is_addable_to_negative_nepali_number_float(
        self,
    ):
        self.assertEqual(
            self.nepalinumber_negative_float_10_1
            + self.nepalinumber_negative_float_5_5,
            self.nepalinumber_negative_float_15_6,
        )

    def test_nepalinumber_float_is_addable_to_positive_nepali_number_float_to_give_positive_nepali_number(
        self,
    ):
        self.assertEqual(
            self.nepalinumber_negative_float_10_1 + self.nepalinumber_float_20_1,
            self.nepalinumber_float_10_0_cont,
        )

    # addition negative testing
    def test_nepalinumber_throws_error_when_objects_are_added_other_than_int_or_float(
        self,
    ):
        self.assertNotIsInstance(self.random_object, int)
        self.assertNotIsInstance(self.random_object, float)

        with self.assertRaises(TypeError) as te:
            _ = self.nepalinumber_integer_10 + self.random_object

        self.assertEqual(
            str(te.exception),
            "unsupported operand type(s) for +: 'nepalinumber' and 'type'",
        )

    def test_nepalinumber_throws_error_when_added_with_objects_other_than_int_or_float(
        self,
    ):
        self.assertNotIsInstance(self.random_object, int)
        self.assertNotIsInstance(self.random_object, float)

        with self.assertRaises(TypeError) as te:
            _ = self.random_object + self.nepalinumber_integer_10

        self.assertEqual(
            str(te.exception),
            "unsupported operand type(s) for +: 'type' and 'nepalinumber'",
        )

    # subtraction
    # nepalinumber positive integer subtraction tests
    def test_nepalinumber_integer_is_subtractable_by_positive_integer(self):
        self.assertEqual(self.nepalinumber_integer_10 - 10, self.nepalinumber_zero)

    def test_nepalinumber_integer_is_subtractable_by_positive_float(self):
        self.assertEqual(
            self.nepalinumber_integer_10 - 5.5, self.nepalinumber_float_4_5
        )

    def test_nepalinumber_integer_is_subtractable_by_negative_integer(self):
        self.assertEqual(
            self.nepalinumber_integer_10 - (-10), self.nepalinumber_integer_20
        )

    def test_nepalinumber_integer_is_subtractable_by_negative_float(self):
        self.assertEqual(
            self.nepalinumber_integer_10 - (-5.5), self.nepalinumber_float_15_5
        )

    def test_nepalinumber_integer_is_subtractable_by_postive_nepali_number_integer(
        self,
    ):
        self.assertEqual(
            self.nepalinumber_integer_10 - self.nepalinumber_integer_10,
            self.nepalinumber_zero,
        )

    def test_nepalinumber_integer_is_subtractable_by_positive_nepali_number_float(self):
        self.assertEqual(
            self.nepalinumber_integer_10 - self.nepalinumber_float_5_5,
            self.nepalinumber_float_4_5,
        )

    def test_nepalinumber_integer_is_subtractable_by_negative_nepali_number_integer(
        self,
    ):
        self.assertEqual(
            self.nepalinumber_integer_10 - self.nepalinumber_negative_integer_10,
            self.nepalinumber_integer_20,
        )

    def test_nepalinumber_integer_is_subtractable_by_negative_nepali_number_float(self):
        self.assertEqual(
            self.nepalinumber_integer_10 - self.nepalinumber_negative_float_5_5,
            self.nepalinumber_float_15_5,
        )

    # subtracting the nepali number to other numbers tests
    def test_positive_integer_is_subtractable_by_nepalinumber_integer(self):
        self.assertEqual(10 - self.nepalinumber_integer_10, self.nepalinumber_zero)

    def test_positive_float_is_subtractable_by_nepalinumber_integer(self):
        self.assertEqual(
            10.1 - self.nepalinumber_integer_10, self.nepalinumber_float_0_0_9
        )

    def test_negative_integer_is_subtractable_by_nepalinumber_integer(self):
        self.assertEqual(
            (-10) - self.nepalinumber_integer_10, self.nepalinumber_negative_integer_20
        )

    def test_negative_float_is_subtractable_by_nepalinumber_integer(self):
        self.assertEqual(
            (-5.5) - self.nepalinumber_integer_10, self.nepalinumber_negative_float_15_5
        )

    def test_negative_float_is_subtractable_by_nepalinumber_integer_to_give_negative_nepali_float(
        self,
    ):
        self.assertEqual(
            (-5.5) - self.nepalinumber_integer_10, self.nepalinumber_negative_float_15_5
        )

    # nepalinumber negative integer subtraction tests
    def test_negative_nepalinumber_integer_is_subtractable_by_positive_integer(self):
        self.assertEqual(
            self.nepalinumber_negative_integer_10 - 10,
            self.nepalinumber_negative_integer_20,
        )

    def test_negative_nepalinumber_integer_is_subtractable_by_positive_float(self):
        self.assertEqual(
            self.nepalinumber_negative_integer_10 - 10.1,
            self.nepalinumber_negative_float_20_1,
        )

    def test_negative_nepalinumber_integer_is_subtractable_by_negative_integer_to_give_positive_nepali_integer(
        self,
    ):
        self.assertEqual(
            self.nepalinumber_negative_integer_10 - (-20), self.nepalinumber_integer_10
        )

    def test_negative_nepalinumber_integer_is_subtractable_by_negative_float(self):
        self.assertEqual(
            self.nepalinumber_negative_integer_10 - (-5.5),
            self.nepalinumber_negative_float_4_5,
        )

    def test_negative_nepalinumber_integer_is_subtractable_by_negative_float_to_give_positive_nepali_float(
        self,
    ):
        self.assertEqual(
            self.nepalinumber_negative_integer_10 - (-15.5), self.nepalinumber_float_5_5
        )

    def test_negative_nepalinumber_integer_is_subtractable_by_postive_nepali_number_integer(
        self,
    ):
        self.assertEqual(
            self.nepalinumber_negative_integer_10 - self.nepalinumber_integer_10,
            self.nepalinumber_negative_float_20_0,
        )

    def test_negative_nepalinumber_integer_is_subtractable_by_positive_nepali_number_float(
        self,
    ):
        self.assertEqual(
            self.nepalinumber_negative_integer_10 - self.nepalinumber_float_10_1,
            self.nepalinumber_negative_float_20_1,
        )

    def test_negative_nepalinumber_integer_is_subtractable_by_negative_nepali_number_integer(
        self,
    ):
        self.assertEqual(
            self.nepalinumber_negative_integer_10
            - self.nepalinumber_negative_integer_10,
            self.nepalinumber_zero,
        )

    def test_negative_nepalinumber_integer_is_subtractable_by_negative_nepali_number_integer_to_give_positive_nepali_number(
        self,
    ):
        self.assertEqual(
            self.nepalinumber_negative_integer_10
            - self.nepalinumber_negative_integer_20,
            self.nepalinumber_integer_10,
        )

    def test_negative_nepalinumber_integer_is_subtractable_by_negative_nepali_number_float(
        self,
    ):
        self.assertEqual(
            self.nepalinumber_negative_integer_10
            - self.nepalinumber_negative_float_5_5,
            self.nepalinumber_negative_float_4_5,
        )

    def test_nepalinumber_integer_is_subtractable_by_negative_nepali_number_float_to_give_positive_nepali_number(
        self,
    ):
        self.assertEqual(
            self.nepalinumber_negative_float_10_1
            - self.nepalinumber_negative_float_20_1,
            self.nepalinumber_float_10_0_cont,
        )

    # nepalinumber positive float subtraction tests
    def test_nepalinumber_float_is_subtractable_by_positive_integer(self):
        self.assertEqual(
            self.nepalinumber_float_10_1 - 10, self.nepalinumber_float_0_0_9
        )

    def test_nepalinumber_float_is_subtractable_by_positive_float(self):
        self.assertEqual(self.nepalinumber_float_10_1 - 10.1, self.nepalinumber_zero)

    def test_nepalinumber_float_is_subtractable_by_negative_integer(self):
        self.assertEqual(
            self.nepalinumber_float_10_1 - (-10), self.nepalinumber_float_20_1
        )

    def test_nepalinumber_float_is_subtractable_by_negative_float(self):
        self.assertEqual(
            self.nepalinumber_float_10_1 - (-5.4), self.nepalinumber_float_15_5
        )

    def test_nepalinumber_float_is_subtractable_by_postive_nepali_number_integer(self):
        self.assertEqual(
            self.nepalinumber_float_10_1 - self.nepalinumber_integer_10,
            self.nepalinumber_float_0_0_9,
        )

    def test_nepalinumber_float_is_subtractable_by_positive_nepali_number_float(self):
        self.assertEqual(
            self.nepalinumber_float_10_1 - self.nepalinumber_float_10_1,
            self.nepalinumber_zero,
        )

    def test_nepalinumber_float_is_subtractable_by_negative_nepali_number_integer(self):
        self.assertEqual(
            self.nepalinumber_float_10_1 - self.nepalinumber_negative_integer_10,
            self.nepalinumber_float_20_1,
        )

    def test_nepalinumber_float_is_subtractable_by_positive_nepali_number_integer_to_give_negative_nepali_number(
        self,
    ):
        self.assertEqual(
            self.nepalinumber_float_10_1 - self.nepalinumber_integer_20,
            self.nepalinumber_negative_float_9_9,
        )

    def test_nepalinumber_float_is_subtractable_by_negative_nepali_number_float(self):
        self.assertEqual(
            self.nepalinumber_float_10_1 - self.nepalinumber_negative_float_5_5,
            self.nepalinumber_float_15_6,
        )

    # nepalinumber negative float subtraction tests
    def test_negative_nepalinumber_float_is_subtractable_by_positive_integer(self):
        self.assertEqual(
            self.nepalinumber_negative_float_10_1 - 10,
            self.nepalinumber_negative_float_20_1,
        )

    def test_negative_nepalinumber_float_is_subtractable_by_positive_float(self):
        self.assertEqual(
            self.nepalinumber_negative_float_10_1 - 5.4,
            self.nepalinumber_negative_float_15_5,
        )

    def test_negative_nepalinumber_float_is_subtractable_by_negative_integer_to_give_positive_nepali_float(
        self,
    ):
        self.assertEqual(
            self.nepalinumber_negative_float_10_1 - (-20), self.nepalinumber_float_9_9
        )

    def test_negative_nepalinumber_float_is_subtractable_by_negative_integer(self):
        self.assertEqual(
            self.nepalinumber_negative_float_10_1 - (-10),
            self.nepalinumber_negative_float_0_0_9,
        )

    def test_negative_nepalinumber_float_is_subtractable_by_negative_float(self):
        self.assertEqual(
            self.nepalinumber_negative_float_10_1 - (-5.6),
            self.nepalinumber_negative_float_4_5,
        )

    def test_negative_nepalinumber_float_is_subtractable_by_negative_float_to_give_positive_nepali_float(
        self,
    ):
        self.assertEqual(
            self.nepalinumber_negative_float_10_1 - (-15.6), self.nepalinumber_float_5_5
        )

    def test_negative_nepalinumber_float_is_subtractable_by_postive_nepali_number_integer(
        self,
    ):
        self.assertEqual(
            self.nepalinumber_negative_float_10_1 - self.nepalinumber_integer_10,
            self.nepalinumber_negative_float_20_1,
        )

    def test_negative_nepalinumber_float_is_subtractable_by_positive_nepali_number_float(
        self,
    ):
        self.assertEqual(
            self.nepalinumber_negative_float_10_1 - self.nepalinumber_float_5_5,
            self.nepalinumber_negative_float_15_6,
        )

    def test_negative_nepalinumber_float_is_subtractable_by_negative_nepali_number_integer(
        self,
    ):
        self.assertEqual(
            self.nepalinumber_negative_float_10_1
            - self.nepalinumber_negative_integer_10,
            self.nepalinumber_negative_float_0_0_9,
        )

    def test_negative_nepalinumber_float_is_subtractable_by_negative_nepali_number_integer_to_give_positive_nepali_number(
        self,
    ):
        self.assertEqual(
            self.nepalinumber_negative_float_10_1
            - self.nepalinumber_negative_integer_20,
            self.nepalinumber_float_9_9,
        )

    def test_negative_nepalinumber_float_is_subtractable_by_negative_nepali_number_float(
        self,
    ):
        self.assertEqual(
            self.nepalinumber_negative_float_10_1
            - self.nepalinumber_negative_float_10_1,
            self.nepalinumber_zero,
        )

    def test_nepalinumber_float_is_subtractable_by_negative_nepali_number_float_to_give_positive_nepali_number(
        self,
    ):
        self.assertEqual(
            self.nepalinumber_negative_float_10_1
            - self.nepalinumber_negative_float_20_1,
            self.nepalinumber_float_10_0_cont,
        )

    # subtraction negative testing
    def test_nepalinumber_throws_error_when_subtracted_by_object_other_than_int_or_float(
        self,
    ):
        self.assertNotIsInstance(self.random_object, int)
        self.assertNotIsInstance(self.random_object, float)

        with self.assertRaises(TypeError) as te:
            _ = self.nepalinumber_integer_10 - self.random_object

        self.assertEqual(
            str(te.exception),
            "unsupported operand type(s) for -: 'nepalinumber' and 'type'",
        )

    def test_nepalinumber_throws_error_when_subtracted_to_objects_other_than_int_or_float(
        self,
    ):
        self.assertNotIsInstance(self.random_object, int)
        self.assertNotIsInstance(self.random_object, float)

        with self.assertRaises(TypeError) as te:
            _ = self.random_object - self.nepalinumber_integer_10

        self.assertEqual(
            str(te.exception),
            "unsupported operand type(s) for -: 'type' and 'nepalinumber'",
        )

    # multiplication
    # nepalinumber positive integer multiplication tests
    def test_nepalinumber_integer_is_multiplicable_to_positive_integer(self):
        self.assertEqual(self.nepalinumber_integer_10 * 2, self.nepalinumber_integer_20)

    def test_nepalinumber_integer_is_multiplicable_to_positive_float(self):
        self.assertEqual(
            self.nepalinumber_integer_10 * 1.5, self.nepalinumber_integer_15
        )

    def test_nepalinumber_integer_is_multiplicable_to_negative_integer(self):
        self.assertEqual(
            self.nepalinumber_integer_10 * (-2), self.nepalinumber_negative_integer_20
        )

    def test_nepalinumber_integer_is_multiplicable_to_negative_float(self):
        self.assertEqual(
            self.nepalinumber_integer_10 * (-1.5), self.nepalinumber_negative_integer_15
        )

    def test_nepalinumber_integer_is_multiplicable_to_postive_nepali_number_integer(
        self,
    ):
        self.assertEqual(
            self.nepalinumber_integer_10 * self.nepalinumber_integer_2,
            self.nepalinumber_integer_20,
        )

    def test_nepalinumber_integer_is_multiplicable_to_positive_nepali_number_float(
        self,
    ):
        self.assertEqual(
            self.nepalinumber_integer_10 * self.nepalinumber_float_1_5,
            self.nepalinumber_integer_15,
        )

    def test_nepalinumber_integer_is_multiplicable_to_negative_nepali_number_integer(
        self,
    ):
        self.assertEqual(
            self.nepalinumber_integer_10 * self.nepalinumber_negative_integer_2,
            self.nepalinumber_negative_integer_20,
        )

    def test_nepalinumber_integer_is_multiplicable_to_negative_nepali_number_float(
        self,
    ):
        self.assertEqual(
            self.nepalinumber_integer_10 * self.nepalinumber_negative_float_1_5,
            self.nepalinumber_negative_integer_15,
        )

    # multiplying the nepali number to other numbers tests
    def test_positive_integer_is_multiplicable_to_nepalinumber_integer(self):
        self.assertEqual(2 * self.nepalinumber_integer_10, self.nepalinumber_integer_20)

    def test_positive_float_is_multiplicable_to_nepalinumber_integer(self):
        self.assertEqual(
            1.5 * self.nepalinumber_integer_10, self.nepalinumber_integer_15
        )

    def test_negative_integer_is_multiplicable_to_nepalinumber_integer(self):
        self.assertEqual(
            -2 * self.nepalinumber_integer_10, self.nepalinumber_negative_integer_20
        )

    def test_negative_integer_is_multiplicable_to_nepalinumber_integer_to_give_negative_nepali_integer(
        self,
    ):
        self.assertEqual(
            -2 * self.nepalinumber_integer_10, self.nepalinumber_negative_integer_20
        )

    def test_negative_float_is_multiplicable_to_nepalinumber_integer(self):
        self.assertEqual(
            (-1.5) * self.nepalinumber_integer_10, self.nepalinumber_negative_integer_15
        )

    # nepalinumber negative integer multiplication tests
    def test_negative_nepalinumber_integer_is_multiplicable_to_positive_integer(self):
        self.assertEqual(
            self.nepalinumber_negative_integer_10 * 2,
            self.nepalinumber_negative_integer_20,
        )

    def test_negative_nepalinumber_integer_is_multiplicable_to_positive_float(self):
        self.assertEqual(
            self.nepalinumber_negative_integer_10 * 1.5,
            self.nepalinumber_negative_integer_15,
        )

    def test_negative_nepalinumber_integer_is_multiplicable_to_negative_integer(self):
        self.assertEqual(
            self.nepalinumber_negative_integer_10 * (-2),
            self.nepalinumber_integer_20,
        )

    def test_negative_nepalinumber_integer_is_multiplicable_to_negative_float(self):
        self.assertEqual(
            self.nepalinumber_negative_integer_10 * (-1.5),
            self.nepalinumber_integer_15,
        )

    def test_negative_nepalinumber_integer_is_multiplicable_to_postive_nepali_number_integer(
        self,
    ):
        self.assertEqual(
            self.nepalinumber_negative_integer_10 * self.nepalinumber_integer_2,
            self.nepalinumber_negative_integer_20,
        )

    def test_negative_nepalinumber_integer_is_multiplicable_to_positive_nepali_number_float(
        self,
    ):
        self.assertEqual(
            self.nepalinumber_negative_integer_10 * self.nepalinumber_float_1_5,
            self.nepalinumber_negative_integer_15,
        )

    def test_negative_nepalinumber_integer_is_multiplicable_to_negative_nepali_number_integer(
        self,
    ):
        self.assertEqual(
            self.nepalinumber_negative_integer_10
            * self.nepalinumber_negative_integer_2,
            self.nepalinumber_integer_20,
        )

    def test_negative_nepalinumber_integer_is_multiplicable_to_negative_nepali_number_float(
        self,
    ):
        self.assertEqual(
            self.nepalinumber_negative_integer_10
            * self.nepalinumber_negative_float_1_5,
            self.nepalinumber_integer_15,
        )

    # nepalinumber positive float multiplication tests
    def test_nepalinumber_float_is_multiplicable_to_positive_integer(self):
        self.assertEqual(self.nepalinumber_float_1_5 * 10, self.nepalinumber_integer_15)

    def test_nepalinumber_float_is_multiplicable_to_positive_float(self):
        self.assertEqual(
            self.nepalinumber_float_10_1 * 2.1, self.nepalinumber_float_21_21
        )

    def test_nepalinumber_float_is_multiplicable_to_negative_integer(self):
        self.assertEqual(
            self.nepalinumber_float_1_5 * (-3), self.nepalinumber_negative_float_4_5
        )

    def test_nepalinumber_float_is_multiplicable_to_negative_float(self):
        self.assertEqual(
            self.nepalinumber_float_4_5 * (-2.2), self.nepalinumber_negative_float_9_9
        )

    def test_nepalinumber_float_is_multiplicable_to_postive_nepali_number_integer(self):
        self.assertEqual(
            self.nepalinumber_float_10_1 * self.nepalinumber_integer_2,
            self.nepalinumber_float_20_2,
        )

    def test_nepalinumber_float_is_multiplicable_to_positive_nepali_number_float(self):
        self.assertEqual(
            self.nepalinumber_float_1_5 * self.nepalinumber_float_3_5,
            self.nepalinumber_float_5_25,
        )

    def test_nepalinumber_float_is_multiplicable_to_negative_nepali_number_integer(
        self,
    ):
        self.assertEqual(
            self.nepalinumber_float_10_1 * self.nepalinumber_negative_integer_2,
            self.nepalinumber_negative_float_20_2,
        )

    def test_nepalinumber_float_is_multiplicable_to_negative_nepali_number_float(self):
        self.assertEqual(
            self.nepalinumber_float_1_5 * self.nepalinumber_negative_float_1_5,
            self.nepalinumber_negative_float_2_25,
        )

    # nepalinumber negative float addition tests
    def test_negative_nepalinumber_float_is_multiplicable_to_positive_integer(self):
        self.assertEqual(
            self.nepalinumber_negative_float_10_1 * 2,
            self.nepalinumber_negative_float_20_2,
        )

    def test_negative_nepalinumber_float_is_multiplicable_to_positive_float(self):
        self.assertEqual(
            self.nepalinumber_negative_float_1_5 * 1.5,
            self.nepalinumber_negative_float_2_25,
        )

    def test_negative_nepalinumber_float_is_multiplicable_to_negative_integer(self):
        self.assertEqual(
            self.nepalinumber_negative_float_10_1 * (-2),
            self.nepalinumber_float_20_2,
        )

    def test_negative_nepalinumber_float_is_multiplicable_to_negative_float(self):
        self.assertEqual(
            self.nepalinumber_negative_float_1_5 * (-3.5),
            self.nepalinumber_float_5_25,
        )

    def test_negative_nepalinumber_float_is_multiplicable_to_postive_nepali_number_integer(
        self,
    ):
        self.assertEqual(
            self.nepalinumber_negative_float_10_1 * self.nepalinumber_integer_2,
            self.nepalinumber_negative_float_20_2,
        )

    def test_negative_nepalinumber_float_is_multiplicable_to_positive_nepali_number_float(
        self,
    ):
        self.assertEqual(
            self.nepalinumber_negative_float_1_5 * self.nepalinumber_float_1_5,
            self.nepalinumber_negative_float_2_25,
        )

    def test_negative_nepalinumber_float_is_mutliplicable_to_negative_nepali_number_integer(
        self,
    ):
        self.assertEqual(
            self.nepalinumber_negative_float_10_1
            * self.nepalinumber_negative_integer_2,
            self.nepalinumber_float_20_2,
        )

    def test_negative_nepalinumber_float_is_multiplicable_to_negative_nepali_number_float(
        self,
    ):
        self.assertEqual(
            self.nepalinumber_negative_float_1_5 * self.nepalinumber_negative_float_1_5,
            self.nepalinumber_float_2_25,
        )

    # string tests
    def test_nepalinumber_integer_can_be_multiplied_with_string(self):
        self.assertEqual(
            self.nepalinumber_integer_2 * self.random_string, 2 * self.random_string
        )

    def test_string_can_be_multiplied_by_nepalinumber_integer(self):
        self.assertEqual(
            self.random_string * self.nepalinumber_integer_2, self.random_string * 2
        )

    def test_nepalinumber_negative_integer_on_multiplication_with_string_gives_empty_string(
        self,
    ):
        self.assertEqual(self.nepalinumber_negative_integer_2 * self.random_string, "")

    def test_string_can_be_multiplied_by_negative_nepalinumber_integer_to_give_empty_string(
        self,
    ):
        self.assertEqual(self.random_string * self.nepalinumber_negative_integer_2, "")

    def test_nepalinumber_float_throws_error_when_multiplied_with_string(self):
        with self.assertRaises(TypeError) as te:
            _ = self.nepalinumber_float_0_1 * self.random_string

        self.assertEqual(
            str(te.exception),
            "can't multiply sequence by non-int of type 'nepalinumber'",
        )

    def test_nepalinumber_float_throws_error_when_multiplied_to_string(self):
        with self.assertRaises(TypeError) as te:
            _ = self.random_string * self.nepalinumber_float_0_0_9

        self.assertEqual(
            str(te.exception),
            "can't multiply sequence by non-int of type 'nepalinumber'",
        )

    # multiplication negative testing
    def test_nepalinumber_throws_error_when_objects_are_multiplied_other_than_int_or_float(
        self,
    ):
        self.assertNotIsInstance(self.random_object, int)
        self.assertNotIsInstance(self.random_object, float)

        with self.assertRaises(TypeError) as te:
            _ = self.nepalinumber_integer_10 * self.random_object

        self.assertEqual(
            str(te.exception),
            "unsupported operand type(s) for *: 'nepalinumber' and 'type'",
        )

    def test_nepalinumber_throws_error_when_multiplied_with_objects_other_than_int_or_float(
        self,
    ):
        self.assertNotIsInstance(self.random_object, int)
        self.assertNotIsInstance(self.random_object, float)

        with self.assertRaises(TypeError) as te:
            _ = self.random_object + self.nepalinumber_integer_10

        self.assertEqual(
            str(te.exception),
            "unsupported operand type(s) for +: 'type' and 'nepalinumber'",
        )

    # division
    # nepalinumber positive integer division tests
    def test_nepalinumber_integer_is_divisible_by_positive_integer(self):
        self.assertEqual(self.nepalinumber_integer_20 / 2, self.nepalinumber_integer_10)

    def test_nepalinumber_integer_is_divisible_by_positive_float(self):
        self.assertEqual(
            self.nepalinumber_integer_10 / 2.5, self.nepalinumber_integer_4
        )

    def test_nepalinumber_integer_is_divisible_by_negative_integer(self):
        self.assertEqual(
            self.nepalinumber_integer_20 / (-2), self.nepalinumber_negative_integer_10
        )

    def test_nepalinumber_integer_is_divisible_by_negative_float(self):
        self.assertEqual(
            self.nepalinumber_integer_10 / (-2.5), self.nepalinumber_negative_integer_4
        )

    def test_nepalinumber_integer_is_divisible_by_postive_nepali_number_integer(self):
        self.assertEqual(
            self.nepalinumber_integer_20 / self.nepalinumber_integer_10,
            self.nepalinumber_integer_2,
        )

    def test_nepalinumber_integer_is_divisible_by_positive_nepali_number_float(self):
        self.assertEqual(
            self.nepalinumber_integer_10 / self.nepalinumber_float_2_5,
            self.nepalinumber_integer_4,
        )

    def test_nepalinumber_integer_is_divisible_by_negative_nepali_number_integer(self):
        self.assertEqual(
            self.nepalinumber_integer_20 / self.nepalinumber_negative_integer_10,
            self.nepalinumber_negative_integer_2,
        )

    def test_nepalinumber_integer_is_divisible_by_negative_nepali_number_float(self):
        self.assertEqual(
            self.nepalinumber_integer_10 / self.nepalinumber_negative_float_2_5,
            self.nepalinumber_negative_integer_4,
        )

    # dividing other numbers by nepali number tests
    def test_positive_integer_is_divisible_by_nepalinumber_integer(self):
        self.assertEqual(20 / self.nepalinumber_integer_2, self.nepalinumber_integer_10)

    def test_positive_float_is_divisible_by_nepalinumber_integer(self):
        self.assertEqual(
            20.2 / self.nepalinumber_integer_2, self.nepalinumber_float_10_1
        )

    def test_negative_integer_is_divisible_by_nepalinumber_integer(self):
        self.assertEqual(
            -20 / self.nepalinumber_integer_10, self.nepalinumber_negative_integer_2
        )

    def test_negative_integer_is_divisible_by_negative_nepalinumber_integer_to_give_positive_nepali_integer(
        self,
    ):
        self.assertEqual(
            (-20) / self.nepalinumber_negative_integer_10, self.nepalinumber_integer_2
        )

    def test_negative_float_is_divisible_by_nepalinumber_integer(self):
        self.assertEqual(
            (-20.2) / self.nepalinumber_integer_2, self.nepalinumber_negative_float_10_1
        )

    def test_negative_float_is_divisible_by_negative_nepalinumber_integer_to_give_positive_nepali_float(
        self,
    ):
        self.assertEqual(
            (-20.2) / self.nepalinumber_negative_integer_2, self.nepalinumber_float_10_1
        )

    # nepalinumber negative integer division tests
    def test_negative_nepalinumber_integer_is_divisible_by_positive_integer(self):
        self.assertEqual(
            self.nepalinumber_negative_integer_10 / 5,
            self.nepalinumber_negative_integer_2,
        )

    def test_negative_nepalinumber_integer_is_divisible_by_positive_float(self):
        self.assertEqual(
            self.nepalinumber_negative_integer_10 / 2.5,
            self.nepalinumber_negative_integer_4,
        )

    def test_negative_nepalinumber_integer_is_divisible_by_negative_integer_to_give_positive_nepali_integer(
        self,
    ):
        self.assertEqual(
            self.nepalinumber_negative_integer_10 / -5, self.nepalinumber_integer_2
        )

    def test_negative_nepalinumber_integer_is_divisible_by_negative_integer(self):
        self.assertEqual(
            self.nepalinumber_negative_integer_10 / (-5),
            self.nepalinumber_integer_2,
        )

    def test_negative_nepalinumber_integer_is_divisible_by_negative_float(self):
        self.assertEqual(
            self.nepalinumber_negative_integer_10 / (-2.5),
            self.nepalinumber_integer_4,
        )

    def test_negative_nepalinumber_integer_is_divisible_by_negative_float_to_give_positive_nepali_integer(
        self,
    ):
        self.assertEqual(
            self.nepalinumber_negative_integer_10 / -2.5, self.nepalinumber_integer_4
        )

    def test_negative_nepalinumber_integer_is_divisible_by_postive_nepali_number_integer(
        self,
    ):
        self.assertEqual(
            self.nepalinumber_negative_integer_20 / self.nepalinumber_integer_10,
            self.nepalinumber_negative_integer_2,
        )

    def test_negative_nepalinumber_integer_is_divisible_by_positive_nepali_number_float(
        self,
    ):
        self.assertEqual(
            self.nepalinumber_negative_integer_10 / self.nepalinumber_float_2_5,
            self.nepalinumber_negative_integer_4,
        )

    def test_negative_nepalinumber_integer_is_divisible_by_negative_nepali_number_integer(
        self,
    ):
        self.assertEqual(
            self.nepalinumber_negative_integer_20
            / self.nepalinumber_negative_integer_10,
            self.nepalinumber_integer_2,
        )

    def test_negative_nepalinumber_integer_is_divisible_by_negative_nepali_number_integer_to_give_positive_nepali_number(
        self,
    ):
        self.assertEqual(
            self.nepalinumber_negative_integer_20
            / self.nepalinumber_negative_integer_2,
            self.nepalinumber_integer_10,
        )

    def test_negative_nepalinumber_integer_is_divisible_by_negative_nepali_number_float(
        self,
    ):
        self.assertEqual(
            self.nepalinumber_negative_integer_10
            / self.nepalinumber_negative_float_2_5,
            self.nepalinumber_integer_4,
        )

    # nepalinumber positive float division tests
    def test_nepalinumber_float_is_divisible_by_positive_integer(self):
        self.assertEqual(self.nepalinumber_float_20_2 / 2, self.nepalinumber_float_10_1)

    def test_nepalinumber_float_is_divisible_by_positive_float(self):
        self.assertEqual(
            self.nepalinumber_float_20_2 / 10.1, self.nepalinumber_integer_2
        )

    def test_nepalinumber_float_is_divisible_by_negative_integer(self):
        self.assertEqual(
            self.nepalinumber_float_20_2 / (-2), self.nepalinumber_negative_float_10_1
        )

    def test_nepalinumber_float_is_divisible_by_negative_float(self):
        self.assertEqual(
            self.nepalinumber_float_20_2 / (-10.1), self.nepalinumber_negative_integer_2
        )

    def test_nepalinumber_float_is_divisible_by_postive_nepali_number_integer(self):
        self.assertEqual(
            self.nepalinumber_float_20_2 / self.nepalinumber_integer_2,
            self.nepalinumber_float_10_1,
        )

    def test_nepalinumber_float_is_divisible_by_positive_nepali_number_float(self):
        self.assertEqual(
            self.nepalinumber_float_20_2 / self.nepalinumber_float_10_1,
            self.nepalinumber_integer_2,
        )

    def test_nepalinumber_float_is_divisible_by_negative_nepali_number_integer(self):
        self.assertEqual(
            self.nepalinumber_float_20_2 / self.nepalinumber_negative_integer_2,
            self.nepalinumber_negative_float_10_1,
        )

    def test_nepalinumber_float_is_divisible_by_negative_nepali_number_float(self):
        self.assertEqual(
            self.nepalinumber_float_20_2 / self.nepalinumber_negative_float_10_1,
            self.nepalinumber_negative_integer_2,
        )

    # nepalinumber negative float division tests
    def test_negative_nepalinumber_float_is_divisible_by_positive_integer(self):
        self.assertEqual(
            self.nepalinumber_negative_float_20_2 / 2,
            self.nepalinumber_negative_float_10_1,
        )

    def test_negative_nepalinumber_float_is_divisible_by_positive_float(self):
        self.assertEqual(
            self.nepalinumber_negative_float_20_2 / 10.1,
            self.nepalinumber_negative_integer_2,
        )

    def test_negative_nepalinumber_float_is_divisible_by_negative_integer(self):
        self.assertEqual(
            self.nepalinumber_negative_float_20_2 / (-2),
            self.nepalinumber_float_10_1,
        )

    def test_negative_nepalinumber_float_is_divisible_by_negative_float(self):
        self.assertEqual(
            self.nepalinumber_negative_float_20_2 / (-10.1),
            self.nepalinumber_integer_2,
        )

    def test_negative_nepalinumber_float_is_divisible_by_postive_nepali_number_integer(
        self,
    ):
        self.assertEqual(
            self.nepalinumber_negative_float_20_2 / self.nepalinumber_integer_2,
            self.nepalinumber_negative_float_10_1,
        )

    def test_negative_nepalinumber_float_is_divisible_by_positive_nepali_number_float(
        self,
    ):
        self.assertEqual(
            self.nepalinumber_negative_float_20_2 / self.nepalinumber_float_10_1,
            self.nepalinumber_negative_integer_2,
        )

    def test_negative_nepalinumber_float_is_divisible_by_negative_nepali_number_integer_to_give_positive_nepali_number(
        self,
    ):
        self.assertEqual(
            self.nepalinumber_negative_float_20_2
            / self.nepalinumber_negative_integer_2,
            self.nepalinumber_float_10_1,
        )

    def test_negative_nepalinumber_float_is_divisible_by_negative_nepali_number_float(
        self,
    ):
        self.assertEqual(
            self.nepalinumber_negative_float_20_2
            / self.nepalinumber_negative_float_10_1,
            self.nepalinumber_integer_2,
        )

    # division negative testing
    def test_nepalinumber_throws_error_when_divided_by_objects_other_than_int_or_float(
        self,
    ):
        self.assertNotIsInstance(self.random_object, int)
        self.assertNotIsInstance(self.random_object, float)

        with self.assertRaises(TypeError) as te:
            _ = self.nepalinumber_integer_10 / self.random_object

        self.assertEqual(
            str(te.exception),
            "unsupported operand type(s) for /: 'nepalinumber' and 'type'",
        )

    def test_nepalinumber_throws_error_when_divided_to_objects_other_than_int_or_float(
        self,
    ):
        self.assertNotIsInstance(self.random_object, int)
        self.assertNotIsInstance(self.random_object, float)

        with self.assertRaises(TypeError) as te:
            _ = self.random_object / self.nepalinumber_integer_10

        self.assertEqual(
            str(te.exception),
            "unsupported operand type(s) for /: 'type' and 'nepalinumber'",
        )

    def test_nepalinumber_throws_error_when_divided_by_zero(self):
        with self.assertRaises(ZeroDivisionError) as ze:
            _ = self.nepalinumber_integer_2 / 0

        self.assertEqual(str(ze.exception), "division by zero")

    def test_nepalinumber_throws_error_when_zero_nepalinumber_divides_other_numbers(
        self,
    ):
        with self.assertRaises(ZeroDivisionError) as ze:
            _ = 12 / self.nepalinumber_zero

        self.assertEqual(str(ze.exception), "division by zero")

    def test_nepalinumber_throws_error_when_divided_by_zero_nepalinumber(self):
        with self.assertRaises(ZeroDivisionError) as ze:
            _ = self.nepalinumber_integer_2 / self.nepalinumber_zero

        self.assertEqual(str(ze.exception), "division by zero")

    # floor divison
    # nepalinumber positive integer division tests
    def test_nepalinumber_integer_is_floor_divisible_by_positive_integer(self):
        self.assertEqual(
            self.nepalinumber_integer_20 // 2, self.nepalinumber_integer_10
        )

    def test_nepalinumber_integer_is_floor_divisible_by_positive_float(self):
        self.assertEqual(
            self.nepalinumber_integer_10 // 2.5, self.nepalinumber_integer_4
        )

    def test_nepalinumber_integer_is_floor_divisible_by_negative_integer(self):
        self.assertEqual(
            self.nepalinumber_integer_20 // (-2), self.nepalinumber_negative_integer_10
        )

    def test_nepalinumber_integer_is_floor_divisible_by_negative_float(self):
        self.assertEqual(
            self.nepalinumber_integer_10 // (-2.5), self.nepalinumber_negative_integer_4
        )

    def test_nepalinumber_integer_is_floor_divisible_by_postive_nepali_number_integer(
        self,
    ):
        self.assertEqual(
            self.nepalinumber_integer_20 // self.nepalinumber_integer_10,
            self.nepalinumber_integer_2,
        )

    def test_nepalinumber_integer_is_floor_divisible_by_positive_nepali_number_float(
        self,
    ):
        self.assertEqual(
            self.nepalinumber_integer_10 / self.nepalinumber_float_2_5,
            self.nepalinumber_integer_4,
        )

    def test_nepalinumber_integer_is_floor_divisible_by_negative_nepali_number_integer(
        self,
    ):
        self.assertEqual(
            self.nepalinumber_integer_20 // self.nepalinumber_negative_integer_10,
            self.nepalinumber_negative_integer_2,
        )

    def test_nepalinumber_integer_is_floor_divisible_by_negative_nepali_number_float(
        self,
    ):
        self.assertEqual(
            self.nepalinumber_integer_10 // self.nepalinumber_negative_float_2_5,
            self.nepalinumber_negative_integer_4,
        )

    # dividing other numbers by nepali number tests
    def test_positive_integer_is_floor_divisible_by_nepalinumber_integer(self):
        self.assertEqual(
            20 // self.nepalinumber_integer_2, self.nepalinumber_integer_10
        )

    def test_positive_float_is_floor_divisible_by_nepalinumber_integer(self):
        self.assertEqual(
            20.2 // self.nepalinumber_integer_2, self.nepalinumber_integer_10
        )

    def test_negative_integer_is_floor_divisible_by_nepalinumber_integer(self):
        self.assertEqual(
            -20 // self.nepalinumber_integer_10, self.nepalinumber_negative_integer_2
        )

    def test_negative_integer_is_floor_divisible_by_negative_nepalinumber_integer_to_give_positive_nepali_integer(
        self,
    ):
        self.assertEqual(
            (-20) // self.nepalinumber_negative_integer_10, self.nepalinumber_integer_2
        )

    def test_negative_float_is_floor_divisible_by_nepalinumber_integer(self):
        self.assertEqual(
            (-19.2) // self.nepalinumber_integer_2,
            self.nepalinumber_negative_integer_10,
        )

    def test_negative_float_is_floor_divisible_by_negative_nepalinumber_integer_to_give_positive_nepali_integer(
        self,
    ):
        self.assertEqual(
            (-20.2) // self.nepalinumber_negative_integer_2,
            self.nepalinumber_integer_10,
        )

    # nepalinumber negative integer division tests
    def test_negative_nepalinumber_integer_is_floor_divisible_by_positive_integer(self):
        self.assertEqual(
            self.nepalinumber_negative_integer_10 // 5,
            self.nepalinumber_negative_integer_2,
        )

    def test_negative_nepalinumber_integer_is_floor_divisible_by_positive_float(self):
        self.assertEqual(
            self.nepalinumber_negative_integer_10 // 2.5,
            self.nepalinumber_negative_integer_4,
        )

    def test_negative_nepalinumber_integer_is_floor_divisible_by_negative_integer_to_give_positive_nepali_integer(
        self,
    ):
        self.assertEqual(
            self.nepalinumber_negative_integer_10 // -5, self.nepalinumber_integer_2
        )

    def test_negative_nepalinumber_integer_is_floor_divisible_by_negative_integer(self):
        self.assertEqual(
            self.nepalinumber_negative_integer_10 // (-5),
            self.nepalinumber_integer_2,
        )

    def test_negative_nepalinumber_integer_is_floor_divisible_by_negative_float(self):
        self.assertEqual(
            self.nepalinumber_negative_integer_10 // (-2.5),
            self.nepalinumber_integer_4,
        )

    def test_negative_nepalinumber_integer_is_floor_divisible_by_negative_float_to_give_positive_nepali_integer(
        self,
    ):
        self.assertEqual(
            self.nepalinumber_negative_integer_10 // -2.5, self.nepalinumber_integer_4
        )

    def test_negative_nepalinumber_integer_is_floor_divisible_by_postive_nepali_number_integer(
        self,
    ):
        self.assertEqual(
            self.nepalinumber_negative_integer_20 // self.nepalinumber_integer_10,
            self.nepalinumber_negative_integer_2,
        )

    def test_negative_nepalinumber_integer_is_floor_divisible_by_positive_nepali_number_float(
        self,
    ):
        self.assertEqual(
            self.nepalinumber_negative_integer_10 // self.nepalinumber_float_2_5,
            self.nepalinumber_negative_integer_4,
        )

    def test_negative_nepalinumber_integer_is_floor_divisible_by_negative_nepali_number_integer(
        self,
    ):
        self.assertEqual(
            self.nepalinumber_negative_integer_20
            // self.nepalinumber_negative_integer_10,
            self.nepalinumber_integer_2,
        )

    def test_negative_nepalinumber_integer_is_floor_divisible_by_negative_nepali_number_integer_to_give_positive_nepali_number(
        self,
    ):
        self.assertEqual(
            self.nepalinumber_negative_integer_20
            // self.nepalinumber_negative_integer_2,
            self.nepalinumber_integer_10,
        )

    def test_negative_nepalinumber_integer_is_floor_divisible_by_negative_nepali_number_float(
        self,
    ):
        self.assertEqual(
            self.nepalinumber_negative_integer_10
            // self.nepalinumber_negative_float_2_5,
            self.nepalinumber_integer_4,
        )

    # nepalinumber positive float division tests
    def test_nepalinumber_float_is_floor_divisible_by_positive_integer(self):
        self.assertEqual(
            self.nepalinumber_float_20_2 // 2, self.nepalinumber_integer_10
        )

    def test_nepalinumber_float_is_floor_divisible_by_positive_float(self):
        self.assertEqual(
            self.nepalinumber_float_20_2 // 10.1, self.nepalinumber_integer_2
        )

    def test_nepalinumber_float_is_floor_divisible_by_negative_integer(self):
        self.assertEqual(
            self.nepalinumber_float_20_2 // (-2), self.nepalinumber_negative_integer_11
        )

    def test_nepalinumber_float_is_floor_divisible_by_negative_float(self):
        self.assertEqual(
            self.nepalinumber_float_20_2 // (-10.1),
            self.nepalinumber_negative_integer_2,
        )

    def test_nepalinumber_float_is_floor_divisible_by_postive_nepali_number_integer(
        self,
    ):
        self.assertEqual(
            self.nepalinumber_float_20_2 // self.nepalinumber_integer_2,
            self.nepalinumber_integer_10,
        )

    def test_nepalinumber_float_is_floor_divisible_by_positive_nepali_number_float(
        self,
    ):
        self.assertEqual(
            self.nepalinumber_float_20_2 // self.nepalinumber_float_10_1,
            self.nepalinumber_integer_2,
        )

    def test_nepalinumber_float_is_floor_divisible_by_negative_nepali_number_integer(
        self,
    ):
        self.assertEqual(
            self.nepalinumber_float_20_2 // self.nepalinumber_negative_integer_2,
            self.nepalinumber_negative_integer_11,
        )

    def test_nepalinumber_float_is_floor_divisible_by_negative_nepali_number_float(
        self,
    ):
        self.assertEqual(
            self.nepalinumber_float_20_2 // self.nepalinumber_negative_float_10_1,
            self.nepalinumber_negative_integer_2,
        )

    # nepalinumber negative float division tests
    def test_negative_nepalinumber_float_is_floor_divisible_by_positive_integer(self):
        self.assertEqual(
            self.nepalinumber_negative_float_20_2 // 2,
            self.nepalinumber_negative_integer_11,
        )

    def test_negative_nepalinumber_float_is_floor_divisible_by_positive_float(self):
        self.assertEqual(
            self.nepalinumber_negative_float_20_2 // 10.1,
            self.nepalinumber_negative_integer_2,
        )

    def test_negative_nepalinumber_float_is_floor_divisible_by_negative_integer(self):
        self.assertEqual(
            self.nepalinumber_negative_float_20_2 // (-2),
            self.nepalinumber_integer_10,
        )

    def test_negative_nepalinumber_float_is_floor_divisible_by_negative_float(self):
        self.assertEqual(
            self.nepalinumber_negative_float_20_2 // (-10.1),
            self.nepalinumber_integer_2,
        )

    def test_negative_nepalinumber_float_is_floor_divisible_by_postive_nepali_number_integer(
        self,
    ):
        self.assertEqual(
            self.nepalinumber_negative_float_20_2 // self.nepalinumber_integer_2,
            self.nepalinumber_negative_integer_11,
        )

    def test_negative_nepalinumber_float_is_floor_divisible_by_positive_nepali_number_float(
        self,
    ):
        self.assertEqual(
            self.nepalinumber_negative_float_20_2 // self.nepalinumber_float_10_1,
            self.nepalinumber_negative_integer_2,
        )

    def test_negative_nepalinumber_float_is_floor_divisible_by_negative_nepali_number_integer_to_give_positive_nepali_number(
        self,
    ):
        self.assertEqual(
            self.nepalinumber_negative_float_20_2
            // self.nepalinumber_negative_integer_2,
            self.nepalinumber_integer_10,
        )

    def test_negative_nepalinumber_float_is_floor_divisible_by_negative_nepali_number_float(
        self,
    ):
        self.assertEqual(
            self.nepalinumber_negative_float_20_2
            // self.nepalinumber_negative_float_10_1,
            self.nepalinumber_integer_2,
        )

    # division negative testing
    def test_nepalinumber_throws_error_when_floor_divided_by_objects_other_than_int_or_float(
        self,
    ):
        self.assertNotIsInstance(self.random_object, int)
        self.assertNotIsInstance(self.random_object, float)

        with self.assertRaises(TypeError) as te:
            _ = self.nepalinumber_integer_10 // self.random_object

        self.assertEqual(
            str(te.exception),
            "unsupported operand type(s) for //: 'nepalinumber' and 'type'",
        )

        with self.assertRaises(TypeError) as te:
            _ = self.nepalinumber_float_10_1 // self.random_object

        self.assertEqual(
            str(te.exception),
            "unsupported operand type(s) for //: 'nepalinumber' and 'type'",
        )

    def test_nepalinumber_throws_error_when_floor_divided_to_objects_other_than_int_or_float(
        self,
    ):
        self.assertNotIsInstance(self.random_object, int)
        self.assertNotIsInstance(self.random_object, float)

        with self.assertRaises(TypeError) as te:
            _ = self.random_object // self.nepalinumber_integer_10

        self.assertEqual(
            str(te.exception),
            "unsupported operand type(s) for //: 'type' and 'nepalinumber'",
        )

        with self.assertRaises(TypeError) as te:
            _ = self.random_object // self.nepalinumber_float_10_1

        self.assertEqual(
            str(te.exception),
            "unsupported operand type(s) for //: 'type' and 'nepalinumber'",
        )

    def test_nepalinumber_throws_error_when_floor_floor_divided_by_zero(self):
        with self.assertRaises(ZeroDivisionError) as ze:
            _ = self.nepalinumber_integer_2 // 0

        self.assertEqual(str(ze.exception), "integer division or modulo by zero")

        with self.assertRaises(ZeroDivisionError) as ze:
            _ = self.nepalinumber_float_10_1 // 0

        python_version = sys.version_info

        if python_version.major >= 3:
            if python_version.minor <= 8:
                self.assertEqual(str(ze.exception), "float divmod()")
            else:
                self.assertEqual(str(ze.exception), "float floor division by zero")

    def test_nepalinumber_throws_error_when_zero_nepalinumber_floor_divides_other_numbers(
        self,
    ):
        with self.assertRaises(ZeroDivisionError) as ze:
            _ = 12 // self.nepalinumber_zero

        self.assertEqual(str(ze.exception), "integer division or modulo by zero")

        with self.assertRaises(ZeroDivisionError) as ze:
            _ = 12.1 // self.nepalinumber_zero

        python_version = sys.version_info

        if python_version.major >= 3:
            if python_version.minor <= 8:
                self.assertEqual(str(ze.exception), "float divmod()")
            else:
                self.assertEqual(str(ze.exception), "float floor division by zero")

    def test_nepalinumber_throws_error_when_floor_divided_by_zero_nepalinumber(self):
        with self.assertRaises(ZeroDivisionError) as ze:
            _ = self.nepalinumber_integer_2 // self.nepalinumber_zero

        self.assertEqual(str(ze.exception), "integer division or modulo by zero")

        with self.assertRaises(ZeroDivisionError) as ze:
            _ = self.nepalinumber_float_10_1 // self.nepalinumber_zero

        python_version = sys.version_info

        if python_version.major >= 3:
            if python_version.minor <= 8:
                self.assertEqual(str(ze.exception), "float divmod()")
            else:
                self.assertEqual(str(ze.exception), "float floor division by zero")

    # mod
    # nepalinumber positive integer modulo tests
    def test_nepalinumber_integer_can_be_modulo_divided_by_positive_integer(self):
        self.assertEqual(self.nepalinumber_integer_10 % 4, self.nepalinumber_integer_2)

    def test_nepalinumber_integer_can_be_modulo_divided_by_positive_float(self):
        self.assertEqual(self.nepalinumber_integer_10 % 2.5, self.nepalinumber_zero)

    def test_nepalinumber_integer_can_be_modulo_divided_by_negative_integer(self):
        self.assertEqual(
            self.nepalinumber_integer_10 % -4, self.nepalinumber_negative_integer_2
        )

    def test_nepalinumber_integer_can_be_modulo_divided_by_negative_float(self):
        self.assertEqual(
            self.nepalinumber_integer_10 % -2.25, self.nepalinumber_negative_float_1_25
        )

    def test_nepalinumber_integer_can_be_modulo_divided_by_positive_nepalinumber_integer(
        self,
    ):
        self.assertEqual(
            self.nepalinumber_integer_10 % self.nepalinumber_integer_2,
            self.nepalinumber_zero,
        )

    def test_nepalinumber_integer_can_be_modulo_divided_by_positive_nepalinumber_float(
        self,
    ):
        self.assertEqual(
            self.nepalinumber_integer_10 % self.nepalinumber_float_2_5,
            self.nepalinumber_zero,
        )

    def test_nepalinumber_integer_can_be_modulo_divided_by_negative_nepalinumber_integer(
        self,
    ):
        self.assertEqual(
            self.nepalinumber_integer_10 % self.nepalinumber_negative_integer_20,
            self.nepalinumber_negative_integer_10,
        )

    def test_nepalinumber_integer_can_be_modulo_divided_by_negative_nepainumber_float(
        self,
    ):
        self.assertEqual(
            self.nepalinumber_integer_10 % self.nepalinumber_negative_float_15_5,
            self.nepalinumber_negative_float_5_5,
        )

    # nepalinumber other numbers modulo divided by positive nepalinumber tests
    def test_positive_integer_can_be_modulo_divided_by_positive_nepalinumber_integer(
        self,
    ):
        self.assertEqual(4 % self.nepalinumber_integer_10, self.nepalinumber_integer_4)

    def test_positive_float_can_be_modulo_divided_by_positive_nepalinumber_integer(
        self,
    ):
        self.assertEqual(
            15.5 % self.nepalinumber_integer_10, self.nepalinumber_float_5_5
        )

    def test_negative_integer_can_be_modulo_divided_by_positive_nepalinumber_integer(
        self,
    ):
        self.assertEqual(-5 % self.nepalinumber_integer_10, self.nepalinumber_integer_5)

    def test_negative_float_can_be_modulo_divided_by_positive_nepalinumber_integer(
        self,
    ):
        self.assertEqual(
            -20.5 % self.nepalinumber_integer_2, self.nepalinumber_float_1_5
        )

    def test_positive_nepalinumber_float_can_be_modulo_divided_by_positive_nepalinumber_integer(
        self,
    ):
        self.assertEqual(
            self.nepalinumber_float_10_1 % self.nepalinumber_integer_5,
            self.nepalinumber_float_0_0_9,
        )

    def test_negative_nepalinumber_integer_can_be_modulo_divided_by_positive_nepalinumber_integer(
        self,
    ):
        self.assertEqual(
            self.nepalinumber_negative_integer_10 % self.nepalinumber_integer_20,
            self.nepalinumber_integer_10,
        )

    def test_negative_nepalinumber_float_can_be_modulo_divided_by_positive_nepainumber_float(
        self,
    ):
        self.assertEqual(
            self.nepalinumber_negative_float_15_5 % self.nepalinumber_integer_10,
            self.nepalinumber_float_4_5,
        )

    # nepalinumber negative integer modulo tests
    def test_negative_nepalinumber_integer_can_be_modulo_divided_by_positive_integer(
        self,
    ):
        self.assertEqual(
            self.nepalinumber_negative_integer_10 % 4, self.nepalinumber_integer_2
        )

    def test_negative_nepalinumber_integer_can_be_modulo_divided_by_positive_float(
        self,
    ):
        self.assertEqual(
            self.nepalinumber_negative_integer_10 % 2.5, self.nepalinumber_zero
        )

    def test_negative_nepalinumber_integer_can_be_modulo_divided_by_negative_integer(
        self,
    ):
        self.assertEqual(
            self.nepalinumber_negative_integer_10 % -4,
            self.nepalinumber_negative_integer_2,
        )

    def test_negative_nepalinumber_integer_can_be_modulo_divided_by_negative_float(
        self,
    ):
        self.assertEqual(
            self.nepalinumber_negative_integer_10 % -2.5, self.nepalinumber_zero
        )

    def test_negative_nepalinumber_integer_can_be_modulo_divided_by_positive_nepalinumber_float(
        self,
    ):
        self.assertEqual(
            self.nepalinumber_negative_integer_10 % self.nepalinumber_float_2_5,
            self.nepalinumber_zero,
        )

    def test_negative_nepalinumber_integer_can_be_modulo_divided_by_negative_nepalinumber_integer(
        self,
    ):
        self.assertEqual(
            self.nepalinumber_negative_integer_10
            % self.nepalinumber_negative_integer_20,
            self.nepalinumber_negative_integer_10,
        )

    def test_negative_nepalinumber_integer_can_be_modulo_divided_by_negative_nepainumber_float(
        self,
    ):
        self.assertEqual(
            self.nepalinumber_negative_integer_10
            % self.nepalinumber_negative_float_15_5,
            self.nepalinumber_negative_integer_10,
        )

    # nepalinumber other numbers modulo divided by negative nepalinumber tests
    def test_positive_integer_can_be_modulo_divided_by_negative_nepalinumber_integer(
        self,
    ):
        self.assertEqual(
            5 % self.nepalinumber_negative_integer_10,
            self.nepalinumber_negative_integer_5,
        )

    def test_positive_float_can_be_modulo_divided_by_negative_nepalinumber_integer(
        self,
    ):
        self.assertEqual(
            15.5 % self.nepalinumber_negative_integer_10,
            self.nepalinumber_negative_float_4_5,
        )

    def test_negative_integer_can_be_modulo_divided_negative_nepalinumber_integer(self):
        self.assertEqual(
            -5 % self.nepalinumber_negative_integer_10,
            self.nepalinumber_negative_integer_5,
        )

    def test_negative_float_can_be_modulo_divided_by_negative_nepalinumber_integer(
        self,
    ):
        self.assertEqual(
            -5.5 % self.nepalinumber_negative_integer_2,
            self.nepalinumber_negative_float_1_5,
        )

    def test_positive_nepalinumber_float_can_be_modulo_divided_by_negative_nepalinumber_integer(
        self,
    ):
        self.assertEqual(
            self.nepalinumber_float_4_5 % self.nepalinumber_negative_integer_10,
            self.nepalinumber_negative_float_5_5,
        )

    def test_negative_nepalinumber_float_can_be_modulo_divided_by_negative_nepainumber_integer(
        self,
    ):
        self.assertEqual(
            self.nepalinumber_negative_float_15_5
            % self.nepalinumber_negative_integer_10,
            self.nepalinumber_negative_float_5_5,
        )

    # nepalinumber positive float modulo tests
    def test_nepalinumber_float_can_be_modulo_divided_by_positive_integer(self):
        self.assertEqual(self.nepalinumber_float_4_5 % 2, self.nepalinumber_float_0_5)

    def test_nepalinumber_float_can_be_modulo_divided_by_positive_float(self):
        self.assertEqual(self.nepalinumber_float_4_5 % 2.5, self.nepalinumber_integer_2)

    def test_nepalinumber_float_can_be_modulo_divided_by_negative_integer(self):
        self.assertEqual(
            self.nepalinumber_float_4_5 % -2, self.nepalinumber_negative_float_1_5
        )

    def test_nepalinumber_float_can_be_modulo_divided_by_negative_float(self):
        self.assertEqual(self.nepalinumber_float_4_5 % -2.25, self.nepalinumber_zero)

    def test_nepalinumber_float_can_be_modulo_divided_by_positive_nepalinumber_integer(
        self,
    ):
        self.assertEqual(
            self.nepalinumber_float_4_5 % self.nepalinumber_integer_2,
            self.nepalinumber_float_0_5,
        )

    def test_nepalinumber_float_can_be_modulo_divided_by_positive_nepalinumber_float(
        self,
    ):
        self.assertEqual(
            self.nepalinumber_float_4_5 % self.nepalinumber_float_2_25,
            self.nepalinumber_zero,
        )

    def test_nepalinumber_float_can_be_modulo_divided_by_negative_nepalinumber_integer(
        self,
    ):
        self.assertEqual(
            self.nepalinumber_float_4_5 % self.nepalinumber_negative_integer_20,
            self.nepalinumber_negative_float_15_5,
        )

    def test_nepalinumber_float_can_be_modulo_divided_by_negative_nepainumber_float(
        self,
    ):
        self.assertEqual(
            self.nepalinumber_float_4_5 % self.nepalinumber_negative_float_15_5,
            self.nepalinumber_negative_integer_11,
        )

    # nepalinumber other numbers modulo divided by positive nepalinumber float tests
    def test_positive_nepalinumber_float_can_be_modulo_divided_by_positive_nepalinumber_float(
        self,
    ):
        self.assertEqual(
            self.nepalinumber_float_10_1 % self.nepalinumber_integer_5,
            self.nepalinumber_float_0_0_9,
        )

    # nepalinumber negative float modulo tests
    def test_negative_nepalinumber_float_can_be_modulo_divided_by_positive_integer(
        self,
    ):
        self.assertEqual(
            self.nepalinumber_negative_float_15_5 % 4, self.nepalinumber_float_0_5
        )

    def test_negative_nepalinumber_float_can_be_modulo_divided_by_positive_float(self):
        self.assertEqual(
            self.nepalinumber_negative_float_15_5 % 2.5, self.nepalinumber_integer_2
        )

    def test_negative_nepalinumber_float_can_be_modulo_divided_by_negative_integer(
        self,
    ):
        self.assertEqual(
            self.nepalinumber_negative_float_4_5 % -20,
            self.nepalinumber_negative_float_4_5,
        )

    def test_negative_nepalinumber_float_can_be_modulo_divided_by_negative_float(self):
        self.assertEqual(
            self.nepalinumber_negative_float_4_5 % -2.5,
            self.nepalinumber_negative_integer_2,
        )

    def test_negative_nepalinumber_float_can_be_modulo_divided_by_positive_nepalinumber_float(
        self,
    ):
        self.assertEqual(
            self.nepalinumber_negative_float_15_5 % self.nepalinumber_float_2_5,
            self.nepalinumber_integer_2,
        )

    def test_negative_nepalinumber_float_can_be_modulo_divided_by_negative_nepalinumber_integer(
        self,
    ):
        self.assertEqual(
            self.nepalinumber_negative_float_4_5
            % self.nepalinumber_negative_integer_20,
            self.nepalinumber_negative_float_4_5,
        )

    # nepalinumber other integers modulo divided by negative nepalinumber float tests
    def test_positive_integer_can_be_modulo_divided_by_negative_nepalinumber_float(
        self,
    ):
        self.assertEqual(
            5 % self.nepalinumber_negative_float_2_5, self.nepalinumber_zero
        )

    def test_positive_float_can_be_modulo_divided_by_negative_nepalinumber_float(self):
        self.assertEqual(
            15.5 % self.nepalinumber_negative_float_15_5, self.nepalinumber_zero
        )

    def test_negative_integer_can_be_modulo_divided_by_negative_nepalinumber_float(
        self,
    ):
        self.assertEqual(
            -5 % self.nepalinumber_negative_float_2_5, self.nepalinumber_zero
        )

    def test_negative_float_can_be_modulo_divided_by_negative_nepalinumber_float(self):
        self.assertEqual(
            -5.5 % self.nepalinumber_negative_float_15_5,
            self.nepalinumber_negative_float_5_5,
        )

    def test_positive_nepalinumber_float_can_be_modulo_divided_by_negative_nepalinumber_float(
        self,
    ):
        self.assertEqual(
            self.nepalinumber_float_4_5 % self.nepalinumber_negative_float_15_5,
            self.nepalinumber_negative_integer_11,
        )

    # modulo negative_testing
    def test_nepalinumber_throws_error_when_object_other_than_int_or_float_modulo_divide(
        self,
    ):
        self.assertNotIsInstance(self.random_object, int)
        self.assertNotIsInstance(self.random_object, float)

        with self.assertRaises(TypeError) as te:
            _ = self.nepalinumber_integer_10 % self.random_object

        self.assertEqual(
            str(te.exception),
            "unsupported operand type(s) for %: 'nepalinumber' and 'type'",
        )

    def test_nepalinumber_throws_error_when_modulo_divided_with_objects_other_than_int_or_float(
        self,
    ):
        self.assertNotIsInstance(self.random_object, int)
        self.assertNotIsInstance(self.random_object, float)

        with self.assertRaises(TypeError) as te:
            _ = self.random_object % self.nepalinumber_integer_10

        self.assertEqual(
            str(te.exception),
            "unsupported operand type(s) for %: 'type' and 'nepalinumber'",
        )

    # divmod
    # divmod positive nepalinumber integer as dividend tests
    def test_positive_nepalinumber_integer_can_be_divmod_with_positive_integer(self):
        self.assertEqual(
            divmod(self.nepalinumber_integer_10, 2),
            (self.nepalinumber_integer_5, self.nepalinumber_zero),
        )

    def test_positive_nepalinumber_integer_can_be_divmod_with_positive_float(self):
        self.assertEqual(
            divmod(self.nepalinumber_integer_10, 2.5),
            (self.nepalinumber_integer_4, self.nepalinumber_zero),
        )

    def test_positive_nepalinumber_integer_can_be_divmod_with_negative_integer(self):
        self.assertEqual(
            divmod(self.nepalinumber_integer_10, -4),
            (
                self.nepalinumber_negative_integer_3,
                self.nepalinumber_negative_integer_2,
            ),
        )

    def test_positive_nepalinumber_integer_can_be_divmod_with_negative_float(self):
        self.assertEqual(
            divmod(self.nepalinumber_integer_10, -5.5),
            (
                self.nepalinumber_negative_integer_2,
                self.nepalinumber_negative_integer_1,
            ),
        )

    def test_positive_nepalinumber_integer_can_be_divmod_with_positive_nepalinumber_integer(
        self,
    ):
        self.assertEqual(
            divmod(self.nepalinumber_integer_10, self.nepalinumber_integer_2),
            (self.nepalinumber_integer_5, self.nepalinumber_zero),
        )

    def test_positive_nepalinumber_integer_can_be_divmod_with_positive_nepalinumber_float(
        self,
    ):
        self.assertEqual(
            divmod(self.nepalinumber_integer_10, self.nepalinumber_float_2_5),
            (self.nepalinumber_integer_4, self.nepalinumber_zero),
        )

    def test_positive_nepalinumber_integer_can_be_divmod_with_negative_nepalinumber_integer(
        self,
    ):
        self.assertEqual(
            divmod(self.nepalinumber_integer_10, self.nepalinumber_negative_integer_4),
            (
                self.nepalinumber_negative_integer_3,
                self.nepalinumber_negative_integer_2,
            ),
        )

    def test_positive_nepalinumber_integer_can_be_divmod_with_negative_nepalinumber_float(
        self,
    ):
        self.assertEqual(
            divmod(self.nepalinumber_integer_10, self.nepalinumber_negative_float_5_5),
            (
                self.nepalinumber_negative_integer_2,
                self.nepalinumber_negative_integer_1,
            ),
        )

    # divmod positive nepalinumber integer as divisior tests
    def test_positive_integer_can_be_divmod_with_positive_nepalinumber_integer(self):
        self.assertEqual(
            divmod(10, self.nepalinumber_integer_2),
            (self.nepalinumber_integer_5, self.nepalinumber_zero),
        )

    def test_positive_float_can_be_divmod_with_positive_nepalinumber_integer(self):
        self.assertEqual(
            divmod(15.5, self.nepalinumber_integer_10),
            (self.nepalinumber_integer_1, self.nepalinumber_float_5_5),
        )

    def test_negative_integer_can_be_divmod_with_positive_nepalinumber_integer(self):
        self.assertEqual(
            divmod(-10, self.nepalinumber_integer_10),
            (self.nepalinumber_negative_integer_1, self.nepalinumber_zero),
        )

    def test_negative_float_can_be_divmod_with_positive_nepalinumber_integer(self):
        self.assertEqual(
            divmod(-15.5, self.nepalinumber_integer_5),
            (self.nepalinumber_negative_integer_4, self.nepalinumber_float_4_5),
        )

    def test_positive_nepalinumber_float_can_be_divmod_with_positive_nepalinumber_integer(
        self,
    ):
        self.assertEqual(
            divmod(self.nepalinumber_float_15_5, self.nepalinumber_integer_10),
            (self.nepalinumber_integer_1, self.nepalinumber_float_5_5),
        )

    def test_negative_nepalinumber_integer_can_be_divmod_with_positive_nepalinumber_integer(
        self,
    ):
        self.assertEqual(
            divmod(self.nepalinumber_negative_integer_10, self.nepalinumber_integer_10),
            (self.nepalinumber_negative_integer_1, self.nepalinumber_zero),
        )

    def test_negative_nepalinumber_float_can_be_divmod_with_positive_nepalinumber_integer(
        self,
    ):
        self.assertEqual(
            divmod(self.nepalinumber_negative_float_15_5, self.nepalinumber_integer_5),
            (self.nepalinumber_negative_integer_4, self.nepalinumber_float_4_5),
        )

    # divmod positive nepalinumber float as dividend tests
    def test_positive_nepalinumber_float_can_be_divmod_with_positive_integer(self):
        self.assertEqual(
            divmod(self.nepalinumber_float_4_5, 2),
            (self.nepalinumber_integer_2, self.nepalinumber_float_0_5),
        )

    def test_positive_nepalinumber_float_can_be_divmod_with_positive_float(self):
        self.assertEqual(
            divmod(self.nepalinumber_float_4_5, 2.5),
            (self.nepalinumber_integer_1, self.nepalinumber_integer_2),
        )

    def test_positive_nepalinumber_float_can_be_divmod_with_negative_integer(self):
        self.assertEqual(
            divmod(self.nepalinumber_float_4_5, -3),
            (
                self.nepalinumber_negative_integer_2,
                self.nepalinumber_negative_float_1_5,
            ),
        )

    def test_positive_nepalinumber_float_can_be_divmod_with_negative_float(self):
        self.assertEqual(
            divmod(self.nepalinumber_float_4_5, -2.25),
            (self.nepalinumber_negative_integer_2, self.nepalinumber_zero),
        )

    def test_positive_nepalinumber_float_can_be_divmod_with_positive_nepalinumber_float(
        self,
    ):
        self.assertEqual(
            divmod(self.nepalinumber_float_4_5, self.nepalinumber_float_4_5),
            (self.nepalinumber_integer_1, self.nepalinumber_zero),
        )

    def test_positive_nepalinumber_float_can_be_divmod_with_negative_nepalinumber_integer(
        self,
    ):
        self.assertEqual(
            divmod(self.nepalinumber_float_4_5, -2),
            (
                self.nepalinumber_negative_integer_3,
                self.nepalinumber_negative_float_1_5,
            ),
        )

    def test_positive_nepalinumber_float_can_be_divmod_with_negative_nepalinumber_float(
        self,
    ):
        self.assertEqual(
            divmod(self.nepalinumber_float_4_5, -2.5),
            (
                self.nepalinumber_negative_integer_2,
                self.nepalinumber_negative_float_0_5,
            ),
        )

    # divmod positive nepalinumber float as divisior tests
    def test_positive_integer_can_be_divmod_with_positive_nepalinumber_float(self):
        self.assertEqual(
            divmod(10, self.nepalinumber_float_2_5),
            (self.nepalinumber_integer_4, self.nepalinumber_zero),
        )

    def test_positive_float_can_be_divmod_with_positive_nepalinumber_float(self):
        self.assertEqual(
            divmod(4.5, self.nepalinumber_float_2_25),
            (self.nepalinumber_integer_2, self.nepalinumber_zero),
        )

    def test_negative_integer_can_be_divmod_with_positive_nepalinumber_float(self):
        self.assertEqual(
            divmod(-10, self.nepalinumber_float_2_25),
            (self.nepalinumber_negative_integer_5, self.nepalinumber_float_1_25),
        )

    def test_negative_float_can_be_divmod_with_positive_nepalinumber_float(self):
        self.assertEqual(
            divmod(-15.5, self.nepalinumber_float_1_5),
            (self.nepalinumber_negative_integer_11, self.nepalinumber_integer_1),
        )

    def test_negative_nepalinumber_integer_can_be_divmod_with_positive_nepalinumber_float(
        self,
    ):
        self.assertEqual(
            divmod(self.nepalinumber_negative_integer_10, self.nepalinumber_float_2_5),
            (self.nepalinumber_negative_integer_4, self.nepalinumber_zero),
        )

    def test_negative_nepalinumber_float_can_be_divmod_with_positive_nepalinumber_float(
        self,
    ):
        self.assertEqual(
            divmod(self.nepalinumber_negative_float_20_2, self.nepalinumber_float_10_1),
            (self.nepalinumber_negative_integer_2, self.nepalinumber_zero),
        )

    # divmod negative nepalinumber integer as dividend tests
    def test_negative_nepalinumber_integer_can_be_divmod_with_positive_integer(self):
        self.assertEqual(
            divmod(self.nepalinumber_negative_integer_10, 2),
            (self.nepalinumber_negative_integer_5, self.nepalinumber_zero),
        )

    def test_negative_nepalinumber_integer_can_be_divmod_with_positive_float(self):
        self.assertEqual(
            divmod(self.nepalinumber_negative_integer_10, 2.5),
            (self.nepalinumber_negative_integer_4, self.nepalinumber_zero),
        )

    def test_negative_nepalinumber_integer_can_be_divmod_with_negative_integer(self):
        self.assertEqual(
            divmod(self.nepalinumber_negative_integer_10, -4),
            (self.nepalinumber_integer_2, self.nepalinumber_negative_integer_2),
        )

    def test_negative_nepalinumber_integer_can_be_divmod_with_negative_float(self):
        self.assertEqual(
            divmod(self.nepalinumber_negative_integer_10, -5.5),
            (self.nepalinumber_integer_1, self.nepalinumber_negative_float_4_5),
        )

    def test_negative_nepalinumber_integer_can_be_divmod_with_negative_nepalinumber_integer(
        self,
    ):
        self.assertEqual(
            divmod(
                self.nepalinumber_negative_integer_10,
                self.nepalinumber_negative_integer_4,
            ),
            (self.nepalinumber_integer_2, self.nepalinumber_negative_integer_2),
        )

    def test_negative_nepalinumber_integer_can_be_divmod_with_negative_nepalinumber_float(
        self,
    ):
        self.assertEqual(
            divmod(
                self.nepalinumber_negative_integer_10,
                self.nepalinumber_negative_float_5_5,
            ),
            (self.nepalinumber_integer_1, self.nepalinumber_negative_float_4_5),
        )

    # divmod negative nepalinumber integer as divisior tests
    def test_positive_integer_can_be_divmod_with_negative_nepalinumber_integer(self):
        self.assertEqual(
            divmod(10, self.nepalinumber_negative_integer_2),
            (self.nepalinumber_negative_integer_5, self.nepalinumber_zero),
        )

    def test_positive_float_can_be_divmod_with_negative_nepalinumber_integer(self):
        self.assertEqual(
            divmod(15.5, self.nepalinumber_negative_integer_10),
            (
                self.nepalinumber_negative_integer_2,
                self.nepalinumber_negative_float_4_5,
            ),
        )

    def test_negative_integer_can_be_divmod_with_negative_nepalinumber_integer(self):
        self.assertEqual(
            divmod(-10, self.nepalinumber_negative_integer_10),
            (self.nepalinumber_integer_1, self.nepalinumber_zero),
        )

    def test_negative_float_can_be_divmod_with_negative_nepalinumber_integer(self):
        self.assertEqual(
            divmod(-4.5, self.nepalinumber_negative_integer_5),
            (self.nepalinumber_zero, self.nepalinumber_negative_float_4_5),
        )

    def test_negative_nepalinumber_float_can_be_divmod_with_negative_nepalinumber_integer(
        self,
    ):
        self.assertEqual(
            divmod(
                self.nepalinumber_negative_float_4_5,
                self.nepalinumber_negative_integer_2,
            ),
            (self.nepalinumber_integer_2, self.nepalinumber_negative_float_0_5),
        )

    # divmod negative nepalinumber float as dividend tests
    def test_negative_nepalinumber_float_can_be_divmod_with_positive_integer(self):
        self.assertEqual(
            divmod(self.nepalinumber_negative_float_4_5, 2),
            (self.nepalinumber_negative_integer_3, self.nepalinumber_float_1_5),
        )

    def test_negative_nepalinumber_float_can_be_divmod_with_positive_float(self):
        self.assertEqual(
            divmod(self.nepalinumber_negative_float_4_5, 2.5),
            (self.nepalinumber_negative_integer_2, self.nepalinumber_float_0_5),
        )

    def test_negative_nepalinumber_float_can_be_divmod_with_negative_integer(self):
        self.assertEqual(
            divmod(self.nepalinumber_negative_float_4_5, -3),
            (self.nepalinumber_integer_1, self.nepalinumber_negative_float_1_5),
        )

    def test_negative_nepalinumber_float_can_be_divmod_with_negative_float(self):
        self.assertEqual(
            divmod(self.nepalinumber_negative_float_4_5, -2.25),
            (self.nepalinumber_integer_2, self.nepalinumber_zero),
        )

    def test_negative_nepalinumber_float_can_be_divmod_with_negative_nepalinumber_float(
        self,
    ):
        self.assertEqual(
            divmod(self.nepalinumber_negative_float_4_5, -2.5),
            (self.nepalinumber_integer_1, self.nepalinumber_negative_integer_2),
        )

    # divmod negative nepalinumber float as divisior tests
    def test_positive_integer_can_be_divmod_with_negative_nepalinumber_float(self):
        self.assertEqual(
            divmod(10, self.nepalinumber_negative_float_2_5),
            (self.nepalinumber_negative_integer_4, self.nepalinumber_zero),
        )

    def test_positive_float_can_be_divmod_with_negative_nepalinumber_float(self):
        self.assertEqual(
            divmod(4.5, self.nepalinumber_negative_float_2_25),
            (self.nepalinumber_negative_integer_2, self.nepalinumber_zero),
        )

    def test_negative_integer_can_be_divmod_with_negative_nepalinumber_float(self):
        self.assertEqual(
            divmod(-10, self.nepalinumber_negative_float_2_25),
            (self.nepalinumber_integer_4, self.nepalinumber_negative_integer_1),
        )

    def test_negative_float_can_be_divmod_with_negative_nepalinumber_float(self):
        self.assertEqual(
            divmod(-15.5, self.nepalinumber_negative_float_1_5),
            (self.nepalinumber_integer_10, self.nepalinumber_negative_float_0_5),
        )

    # pow
    # pow positive nepalinumber integer as base
    def test_positive_nepalinumber_integer_can_be_powered_to_positive_integer(self):
        self.assertEqual(self.nepalinumber_integer_2**2, self.nepalinumber_integer_4)

    def test_positive_nepalinumber_integer_can_be_powered_to_positive_float(self):
        self.assertEqual(
            self.nepalinumber_integer_2**2.5, number.nepalinumber(2**2.5)
        )

    def test_positive_nepalinumber_integer_can_be_powered_to_negative_integer(self):
        self.assertEqual(self.nepalinumber_integer_2**-1, self.nepalinumber_float_0_5)

    def test_positive_nepalinumber_integer_can_be_powered_to_negative_float(self):
        self.assertEqual(
            self.nepalinumber_integer_2**-1.5, number.nepalinumber(2**-1.5)
        )

    def test_positive_nepalinumber_integer_can_be_powered_to_positive_nepalinumber_integer(
        self,
    ):
        self.assertEqual(
            self.nepalinumber_integer_2**self.nepalinumber_integer_2,
            self.nepalinumber_integer_4,
        )

    def test_positive_nepalinumber_integer_can_be_powered_to_positive_nepalinumber_float(
        self,
    ):
        self.assertEqual(
            self.nepalinumber_integer_2**self.nepalinumber_float_2_5,
            number.nepalinumber(2**2.5),
        )

    def test_positive_nepalinumber_integer_can_be_powered_to_negative_nepalinumber_integer(
        self,
    ):
        self.assertEqual(
            self.nepalinumber_integer_2**self.nepalinumber_negative_integer_1,
            self.nepalinumber_float_0_5,
        )

    def test_positive_nepalinumber_integer_can_be_powered_to_negative_nepalinumber_float(
        self,
    ):
        self.assertEqual(
            self.nepalinumber_integer_2**self.nepalinumber_negative_float_1_5,
            number.nepalinumber(2**-1.5),
        )

    # pow positive nepalinumber integer as exponent
    def test_positive_integer_can_be_powered_to_positive_nepalinumber_integer(self):
        self.assertEqual(2**self.nepalinumber_integer_2, self.nepalinumber_integer_4)

    def test_positive_float_can_be_powered_to_positive_nepalinumber_integer(self):
        self.assertEqual(
            2.5**self.nepalinumber_integer_2, number.nepalinumber(2.5**2)
        )

    def test_negative_integer_can_be_powered_to_positive_nepalinumber_integer(self):
        self.assertEqual(
            (-1) ** self.nepalinumber_integer_2, self.nepalinumber_integer_1
        )

    def test_negative_float_can_be_powered_to_positive_nepalinumber_integer(self):
        self.assertEqual(
            (-1.5) ** self.nepalinumber_integer_2, number.nepalinumber((-1.5) ** 2)
        )

    def test_positive_nepalinumber_float_can_be_powered_to_positive_nepalinumber_integer(
        self,
    ):
        self.assertEqual(
            self.nepalinumber_float_2_5**self.nepalinumber_integer_2,
            number.nepalinumber(2.5**2),
        )

    def test_negative_nepalinumber_integer_can_be_powered_to_positive_nepalinumber_integer(
        self,
    ):
        self.assertEqual(
            self.nepalinumber_negative_integer_1**self.nepalinumber_integer_2,
            self.nepalinumber_integer_1,
        )

    def test_negative_nepalinumber_float_can_be_powered_to_positive_nepalinumber_integer(
        self,
    ):
        self.assertEqual(
            self.nepalinumber_negative_float_1_5**self.nepalinumber_integer_2,
            number.nepalinumber((-1.5) ** 2),
        )

    # pow positive nepalinumber float as base
    def test_positive_nepalinumber_float_can_be_powered_to_positive_integer(self):
        self.assertEqual(self.nepalinumber_float_1_5**2, self.nepalinumber_float_2_25)

    def test_positive_nepalinumber_float_can_be_powered_to_positive_float(self):
        self.assertEqual(
            self.nepalinumber_float_1_5**1.5, number.nepalinumber(1.5**1.5)
        )

    def test_positive_nepalinumber_float_can_be_powered_to_negative_integer(self):
        self.assertEqual(
            self.nepalinumber_float_1_5**-2, number.nepalinumber(1.5**-2)
        )

    def test_positive_nepalinumber_float_can_be_powered_to_negative_float(self):
        self.assertEqual(
            self.nepalinumber_float_1_5**-1.5, number.nepalinumber(1.5**-1.5)
        )

    def test_positive_nepalinumber_float_can_be_powered_to_positive_nepalinumber_float(
        self,
    ):
        self.assertEqual(
            self.nepalinumber_float_1_5**self.nepalinumber_float_1_5,
            number.nepalinumber(1.5**1.5),
        )

    def test_positive_nepalinumber_float_can_be_powered_to_negative_nepalinumber_integer(
        self,
    ):
        self.assertEqual(
            self.nepalinumber_float_1_5**self.nepalinumber_negative_integer_2,
            number.nepalinumber(1.5**-2),
        )

    def test_positive_nepalinumber_float_can_be_powered_to_negative_nepalinumber_float(
        self,
    ):
        self.assertEqual(
            self.nepalinumber_float_1_5**self.nepalinumber_negative_float_1_5,
            number.nepalinumber(1.5**-1.5),
        )

    # pow positive nepalinumber float as exponent
    def test_positive_integer_can_be_powered_to_positive_nepalinumber_float(self):
        self.assertEqual(
            2**self.nepalinumber_float_1_5, number.nepalinumber(2**1.5)
        )

    def test_positive_float_can_be_powered_to_positive_nepalinumber_float(self):
        self.assertEqual(
            1.5**self.nepalinumber_float_1_5, number.nepalinumber(1.5**1.5)
        )

    def test_negative_integer_can_be_powered_to_positive_nepalinumber_float(self):
        self.assertEqual((-2) ** self.nepalinumber_float_1_5, (-2) ** 1.5)

    def test_negative_float_can_be_powered_to_positive_nepalinumber_float(self):
        self.assertEqual((-1.5) ** self.nepalinumber_float_1_5, (-1.5) ** 1.5)

    def test_negative_nepalinumber_integer_can_be_powered_to_positive_nepalinumber_float(
        self,
    ):
        self.assertEqual(
            self.nepalinumber_negative_integer_2**self.nepalinumber_float_1_5,
            (-2) ** 1.5,
        )

    def test_negative_nepalinumber_float_can_be_powered_to_positive_nepalinumber_float(
        self,
    ):
        self.assertEqual(
            self.nepalinumber_negative_float_1_5**self.nepalinumber_float_1_5,
            (-1.5) ** 1.5,
        )

    # pow negative nepalinumber integer as base
    def test_negative_nepalinumber_integer_can_be_powered_to_positive_integer(self):
        self.assertEqual(
            self.nepalinumber_negative_integer_2**2, self.nepalinumber_integer_4
        )

    def test_negative_nepalinumber_integer_can_be_powered_to_positive_float(self):
        self.assertEqual(
            self.nepalinumber_negative_integer_2**2.5,
            (-2) ** 2.5,
        )

    def test_negative_nepalinumber_integer_can_be_powered_to_negative_integer(self):
        self.assertEqual(
            self.nepalinumber_negative_integer_2**-1,
            self.nepalinumber_negative_float_0_5,
        )

    def test_negative_nepalinumber_integer_can_be_powered_to_negative_float(self):
        self.assertEqual(
            self.nepalinumber_negative_integer_2**-1.5,
            (-2) ** -1.5,
        )

    def test_negative_nepalinumber_integer_can_be_powered_to_negative_nepalinumber_integer(
        self,
    ):
        self.assertEqual(
            self.nepalinumber_negative_integer_2
            ** self.nepalinumber_negative_integer_1,
            self.nepalinumber_negative_float_0_5,
        )

    def test_negative_nepalinumber_integer_can_be_powered_to_negative_nepalinumber_float(
        self,
    ):
        self.assertEqual(
            self.nepalinumber_negative_integer_2
            ** self.nepalinumber_negative_float_1_5,
            (-2) ** -1.5,
        )

    # pow negative nepalinumber integer as exponent
    def test_positive_integer_can_be_powered_to_negative_nepalinumber_integer(self):
        self.assertEqual(
            2**self.nepalinumber_negative_integer_2, number.nepalinumber(2**-2)
        )

    def test_positive_float_can_be_powered_to_negative_nepalinumber_integer(self):
        self.assertEqual(
            2.5**self.nepalinumber_negative_integer_2, number.nepalinumber(2.5**-2)
        )

    def test_negative_integer_can_be_powered_to_negative_nepalinumber_integer(self):
        self.assertEqual(
            (-1) ** self.nepalinumber_negative_integer_2, self.nepalinumber_integer_1
        )

    def test_negative_float_can_be_powered_to_negative_nepalinumber_integer(self):
        self.assertEqual(
            (-1.5) ** self.nepalinumber_negative_integer_2,
            number.nepalinumber((-1.5) ** (-2)),
        )

    def test_negative_nepalinumber_float_can_be_powered_to_negative_nepalinumber_integer(
        self,
    ):
        self.assertEqual(
            self.nepalinumber_negative_float_1_5
            ** self.nepalinumber_negative_integer_2,
            number.nepalinumber((-1.5) ** (-2)),
        )

    # pow negative nepalinumber float as base
    def test_negative_nepalinumber_float_can_be_powered_to_positive_integer(self):
        self.assertEqual(
            self.nepalinumber_negative_float_1_5**2, self.nepalinumber_float_2_25
        )

    def test_negative_nepalinumber_float_can_be_powered_to_positive_float(self):
        self.assertEqual(
            self.nepalinumber_negative_float_1_5**1.5,
            (-1.5) ** 1.5,
        )

    def test_negative_nepalinumber_float_can_be_powered_to_negative_integer(self):
        self.assertEqual(
            self.nepalinumber_negative_float_1_5**-2,
            number.nepalinumber((-1.5) ** -2),
        )

    def test_negative_nepalinumber_float_can_be_powered_to_negative_float(self):
        self.assertEqual(
            self.nepalinumber_negative_float_1_5**-1.5,
            (-1.5) ** -1.5,
        )

    def test_negative_nepalinumber_float_can_be_powered_to_negative_nepalinumber_float(
        self,
    ):
        self.assertEqual(
            self.nepalinumber_negative_float_1_5
            ** self.nepalinumber_negative_float_1_5,
            (-1.5) ** -1.5,
        )

    # pow negative nepalinumber float as exponent
    def test_positive_integer_can_be_powered_to_negative_nepalinumber_float(self):
        self.assertEqual(
            2**self.nepalinumber_negative_float_1_5, number.nepalinumber(2**-1.5)
        )

    def test_positive_float_can_be_powered_to_negative_nepalinumber_float(self):
        self.assertEqual(
            1.5**self.nepalinumber_negative_float_1_5,
            number.nepalinumber(1.5**-1.5),
        )

    def test_negative_integer_can_be_powered_to_negative_nepalinumber_float(self):
        self.assertEqual(
            (-2) ** self.nepalinumber_negative_float_1_5,
            (-2) ** -1.5,
        )

    def test_negative_float_can_be_powered_to_negative_nepalinumber_float(self):
        self.assertEqual(
            (-1.5) ** self.nepalinumber_negative_float_1_5,
            (-1.5) ** -1.5,
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
        with self.assertRaises(ValueError):
            nepalinumber("आइतबार")

    def test_nepalinumber_raises_exception_for_two_dots(self):
        with self.assertRaises(ValueError):
            nepalinumber("10..5")

    def test_nepalinumber_raises_exception_for_nepali_aplha(self):
        with self.assertRaises(ValueError):
            nepalinumber("10..5")

    def test_nepalinumber_raises_exception_for_special_chars(self):
        with self.assertRaises(ValueError):
            nepalinumber("!@#$%^&*()-+")

    def test_nepalinumber_raise_exception_for_number_with_spaces(self):
        with self.assertRaises(ValueError):
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


class TestNepaliNumberMethods(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # positive integers
        cls.nepalinumber_integer_999999 = number.nepalinumber(999999)
        cls.nepalinumber_integer_1 = number.nepalinumber(1)
        cls.nepalinumber_integer_0 = number.nepalinumber(0)
        # positive floats
        cls.nepalinumber_float_999999_999999 = number.nepalinumber(999999.999999)
        cls.nepalinumber_float_1_25 = number.nepalinumber(1.25)
        cls.nepalinumber_float_0_05 = number.nepalinumber(0.05)
        cls.nepalinumber_float_0_0 = number.nepalinumber(0.0)
        # negative numbers
        cls.nepalinumber_negative_integer_999999 = number.nepalinumber(-999999)
        cls.nepalinumber_negative_integer_1 = number.nepalinumber(-1)
        # negative floats
        cls.nepalinumber_negative_float_999999_999999 = number.nepalinumber(
            -999999.999999
        )
        cls.nepalinumber_negative_float_1_25 = number.nepalinumber(-1.25)
        cls.nepalinumber_negative_float_0_05 = number.nepalinumber(-0.05)

    # tests for str_ne methods
    def test_nepalinumber_str_ne_for_small_positive_integer(self):
        self.assertEqual(self.nepalinumber_integer_1.str_ne(), "१")

    def test_nepalinumber_str_ne_for_large_positive_integer(self):
        self.assertEqual(self.nepalinumber_integer_999999.str_ne(), "९९९९९९")

    def test_nepalinumber_str_ne_for_small_negative_integer(self):
        self.assertEqual(self.nepalinumber_negative_integer_1.str_ne(), "-१")

    def test_nepalinumber_str_ne_for_large_negative_integer(self):
        self.assertEqual(self.nepalinumber_negative_integer_999999.str_ne(), "-९९९९९९")

    def test_nepalinumber_str_ne_for_small_positive_float(self):
        self.assertEqual(self.nepalinumber_float_1_25.str_ne(), "१.२५")
        self.assertEqual(self.nepalinumber_float_0_05.str_ne(), "०.०५")

    def test_nepalinumber_str_ne_for_large_positive_float(self):
        self.assertEqual(
            self.nepalinumber_float_999999_999999.str_ne(), "९९९९९९.९९९९९९"
        )

    def test_nepalinumber_str_ne_for_small_negative_float(self):
        self.assertEqual(self.nepalinumber_negative_float_1_25.str_ne(), "-१.२५")
        self.assertEqual(self.nepalinumber_negative_float_0_05.str_ne(), "-०.०५")

    def test_nepalinumber_str_ne_for_large_negative_float(self):
        self.assertEqual(
            self.nepalinumber_negative_float_999999_999999.str_ne(), "-९९९९९९.९९९९९९"
        )

    def test_nepalinumber_str_ne_for_zero(self):
        self.assertEqual(self.nepalinumber_integer_0.str_ne(), "०")
        self.assertEqual(self.nepalinumber_float_0_0.str_ne(), "०.०")
