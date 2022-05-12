import datetime
import unittest

from nepali.datetime import nepalihumanize

class TestNepaliDateTime(unittest.TestCase):

    def test_nepalihumanize_basic(self):
        humanize_str = nepalihumanize(datetime.datetime(2022, 2, 15), threshold=0)
        self.assertNotEqual(humanize_str, None, msg='Invalid nepali humanize str.')

        humanize_str = nepalihumanize(datetime.datetime(2022, 2, 15), threshold=600000000)
        self.assertNotEqual(humanize_str, None, msg='Invalid nepali humanize str with threshold.')
