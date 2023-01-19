"""
NOTE: To run only this test case use the below command
python setup.py test -s nepali.tests.test_phone_number
"""
import unittest
from unittest import mock

from nepali.phone_number import is_mobile_number, is_landline_number, is_valid, get_exact_number, parse


class TestPhoneNumber(unittest.TestCase):
    def test_is_mobile_number(self):
        # True case
        self.assertEqual(is_mobile_number('9842531781'), True)
        self.assertEqual(is_mobile_number('9779842531781'), True)
        self.assertEqual(is_mobile_number('+9779842531781'), True)
        self.assertEqual(is_mobile_number('+977-9842531781'), True)

        # False case
        self.assertEqual(is_mobile_number(None), False)  # type: ignore
        self.assertEqual(is_mobile_number(''), False)
        self.assertEqual(is_mobile_number('test'), False)
        self.assertEqual(is_mobile_number('977test'), False)
        self.assertEqual(is_mobile_number('+977test'), False)
        self.assertEqual(is_mobile_number('+977-test'), False)

    def test_is_landline_number(self):
        # True case
        self.assertEqual(is_landline_number('14231481'), True)
        self.assertEqual(is_landline_number('014231481'), True)
        self.assertEqual(is_landline_number('0215154579'), True)
        self.assertEqual(is_landline_number('+977-142314819'), True)
        self.assertEqual(is_landline_number('0154225639'), True)
        self.assertEqual(is_landline_number('9770154225639'), True)
        self.assertEqual(is_landline_number('0565114679'), True)
        self.assertEqual(is_landline_number('+977-0565114679'), True)

        # False case
        self.assertEqual(is_landline_number(None), False)  # type: ignore
        self.assertEqual(is_landline_number(''), False)
        self.assertEqual(is_landline_number('test'), False)
        self.assertEqual(is_landline_number('977test'), False)
        self.assertEqual(is_landline_number('+977test'), False)
        self.assertEqual(is_landline_number('+977-test'), False)

    def test_is_valid(self):
        # mock start
        patcher1 = mock.patch('nepali.phone_number.is_mobile_number')
        patcher2 = mock.patch('nepali.phone_number.is_landline_number')
        mock_is_mobile_number = patcher1.start()
        mock_is_landline_number = patcher2.start()

        # both mobile and landline are invalid
        mock_is_mobile_number.return_value = False
        mock_is_landline_number.return_value = False
        self.assertEqual(is_valid('who_cares'), False)

        # mobile is invalid and landline is valid
        mock_is_mobile_number.return_value = True
        mock_is_landline_number.return_value = False
        self.assertEqual(is_valid('who_cares'), True)

        # mobile is invalid and landline is valid
        mock_is_mobile_number.return_value = False
        mock_is_landline_number.return_value = True
        self.assertEqual(is_valid('who_cares'), True)

        # both mobile and landline are valid
        mock_is_mobile_number.return_value = True
        mock_is_landline_number.return_value = True
        self.assertEqual(is_valid('who_cares'), True)

        # mock stop
        patcher1.stop()
        patcher2.stop()

    def test_get_exact_number(self):
        self.assertEqual(get_exact_number('9842531781'), '9842531781')
        self.assertEqual(get_exact_number('9779842531781'), '9842531781')
        self.assertEqual(get_exact_number('+9779842531781'), '9842531781')
        self.assertEqual(get_exact_number('+977-9842531781'), '9842531781')
        with self.assertRaises(AttributeError):
            get_exact_number(None)  # type: ignore
        self.assertEqual(get_exact_number(''), '')
        self.assertEqual(get_exact_number('test'), 'test')
        self.assertEqual(get_exact_number('977test'), 'test')
        self.assertEqual(get_exact_number('+977test'), 'test')
        self.assertEqual(get_exact_number('+977-test'), 'test')
        self.assertEqual(get_exact_number('+977-142314819'), '142314819')
        self.assertEqual(get_exact_number('0154225639'), '0154225639')
        self.assertEqual(get_exact_number('9770154225639'), '0154225639')
        self.assertEqual(get_exact_number('0565114679'), '0565114679')
        self.assertEqual(get_exact_number('984-2531781'), '9842531781')
        self.assertEqual(get_exact_number('984-2531-781'), '9842531781')
