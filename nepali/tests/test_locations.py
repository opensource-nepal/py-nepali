import unittest

from nepali import locations
from nepali.locations.models import (
    Location,
    MunicipalityType,
    Province,
    District,
    Municipality,
)
from nepali.locations.utils import (
    _filter_location,
    get_province,
    get_district,
    get_municipality,
)


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
        province = _filter_location(
            locations=locations.provinces, name="Bagmati", exact=True
        )
        self.assertEqual(province, None)

        # checking using exact True with a valid match
        province = _filter_location(
            locations=locations.provinces, name="Bagmati Province", exact=True
        )
        self.assertEqual(province.name, "Bagmati Province")

        # checking assertion if exact and multiple is passes together
        with self.assertRaises(ValueError):
            _filter_location(
                locations=locations.provinces,
                name="Bagmati Province",
                exact=True,
                multiple=True,
            )

        # checking multiple value match
        provinces = _filter_location(
            locations=locations.provinces, name="Province", multiple=True
        )
        self.assertEqual(type(provinces), list)
        self.assertEqual(len(provinces), 7)

        # checking multiple value with invalid match
        provinces = _filter_location(
            locations=locations.provinces, name="invalid", multiple=True
        )
        self.assertEqual(len(provinces), 0)

        # checking pattern match with nepali name
        province = _filter_location(locations=locations.provinces, name_nepali="बागमती")
        self.assertEqual(province.name_nepali, "बागमती प्रदेश")

        # checking using exact True with a valid nepali match
        province = _filter_location(
            locations=locations.provinces, name_nepali="बागमती प्रदेश", exact=True
        )
        self.assertEqual(province.name_nepali, "बागमती प्रदेश")


class TestLocationsUtils(unittest.TestCase):
    def test_utils_get_province(self):
        province = get_province(name="Bagmati")
        self.assertEqual(province.name, "Bagmati Province")

    def test_utils_get_district(self):
        district = get_district(name="Kathmandu")
        self.assertEqual(district.name, "Kathmandu")

    def test_utils_get_municipality(self):
        municipality = get_municipality(name="Kathmandu")
        self.assertEqual(municipality.name, "Kathmandu Metropolitan City")


class TestLocationsModels(unittest.TestCase):
    def test_location_data(self):
        location = Location("test_en", "test_ne")
        self.assertEqual(location.name, "test_en")
        self.assertEqual(location.name_nepali, "test_ne")

    def test_location_str(self):
        location = Location("test_en", "test_ne")
        self.assertEqual(str(location), "test_en")

    def test_location_repr(self):
        location = Location("test_en", "test_ne")
        self.assertEqual(repr(location), "test_en")

    def test_districts_from_province(self):
        province = Province("Province1", "Province1")
        district = District(province, "District1", "District1")
        self.assertListEqual(province.districts, [district])

    def test_municipalities_from_province_and_district(self):
        province = Province("Province1", "Province1")
        district = District(province, "District1", "District1")
        municipality = Municipality(
            district, "Municipality1", "Municipality1", MunicipalityType.METROPOLITAN
        )
        self.assertListEqual(province.municipalities, [municipality])
        self.assertListEqual(district.municipalities, [municipality])

    def test_municipality_province_district_and_type(self):
        province = Province("Province1", "Province1")
        district = District(province, "District1", "District1")
        municipality = Municipality(
            district, "Municipality1", "Municipality1", MunicipalityType.METROPOLITAN
        )
        self.assertEqual(municipality.province, province)
        self.assertEqual(municipality.district, district)
        self.assertEqual(municipality.municipality_type, MunicipalityType.METROPOLITAN)

    # MunicipalityType
    def test_municipality_type_with_invalid_data(self):
        with self.assertRaises(ValueError):
            MunicipalityType("Hello")

    def test_municipality_type_with_valid_data(self):
        municipality_type = MunicipalityType("Metropolitan City")
        self.assertEqual(municipality_type, MunicipalityType.METROPOLITAN)

    def test_municipality_type_str(self):
        municipality_type = MunicipalityType.RURAL_MUNICIPALITY
        self.assertEqual(str(municipality_type), municipality_type.value)

    def test_municipality_type_repr(self):
        municipality_type = MunicipalityType.SUB_METROPOLITAN
        self.assertEqual(repr(municipality_type), municipality_type.value)
