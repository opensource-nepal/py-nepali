import unittest

from nepali import locations
from nepali.locations.utils import _filter_location, get_province, get_district, get_municipality


class TestLocations(unittest.TestCase):

    def test_locations_count(self):
        self.assertEqual(len(locations.provinces), 7)
        self.assertEqual(len(locations.districts), 77)
        self.assertEqual(len(locations.municipalities), 753)

    def test_utils_filter_location(self):
        # checking if no argument is passed
        with self.assertRaises(ValueError):
            _filter_location(locations=locations.provinces)

        # checking pattern match
        province = _filter_location(locations=locations.provinces, name="Bagmati")
        self.assertEqual(province.name, "Bagmati Province")

        # checking ignore-case match
        province = _filter_location(locations=locations.provinces, name="bagmati")
        self.assertEqual(province.name, "Bagmati Province")

        # checking with invalid name
        province = _filter_location(locations=locations.provinces, name="invalid")
        self.assertEqual(province, None)

        # checking using exact True with invalid match
        province = _filter_location(locations=locations.provinces, name="Bagmati", exact=True)
        self.assertEqual(province, None)

        # checking using exact True with a valid match
        province = _filter_location(locations=locations.provinces, name="Bagmati Province", exact=True)
        self.assertEqual(province.name, "Bagmati Province")

        # checking assertion if exact and multiple is passes together
        with self.assertRaises(ValueError):
            _filter_location(locations=locations.provinces, name="Bagmati Province", exact=True, multiple=True)

        # checking multiple value match
        provinces = _filter_location(locations=locations.provinces, name="Province", multiple=True)
        self.assertEqual(type(provinces), list)
        self.assertEqual(len(provinces), 7)

        # checking multiple value with invalid match
        provinces = _filter_location(locations=locations.provinces, name="invalid", multiple=True)
        self.assertEqual(len(provinces), 0)

        # checking pattern match with nepali name
        province = _filter_location(locations=locations.provinces, name_nepali="बागमती")
        self.assertEqual(province.name_nepali, "बागमती प्रदेश")

        # checking using exact True with a valid nepali match
        province = _filter_location(locations=locations.provinces, name_nepali="बागमती प्रदेश", exact=True)
        self.assertEqual(province.name_nepali, "बागमती प्रदेश")

    def test_utils_get_province(self):
        province = get_province(locations=locations.provinces, name="Bagmati")
        self.assertEqual(province.name, "Bagmati Province")

    def test_utils_get_district(self):
        district = get_district(locations=locations.districts, name="Kathmandu")
        self.assertEqual(district.name, "Kathmandu")

    def test_utils_get_municipality(self):
        municipality = get_municipality(locations=locations.municipalities, name="Kathmandu")
        self.assertEqual(municipality.name, "Kathmandu Metropolitan City")
