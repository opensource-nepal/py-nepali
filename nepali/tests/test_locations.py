import unittest

from nepali import locations


class TestLocations(unittest.TestCase):

    def test_locations_count(self):
        self.assertEqual(len(locations.provinces), 7)
        self.assertEqual(len(locations.districts), 77)
        self.assertEqual(len(locations.municipalities), 753)
