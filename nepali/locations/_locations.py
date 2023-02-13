from typing import List, Tuple

from .models import Province, District, Municipality, MunicipalityType


def _loadData() -> Tuple[List[Province], List[District], List[Municipality]]:
    from ._data import _location_data

    provinces = []
    districts = []
    municipalities = []
    for province_data in _location_data:
        province = Province(
            name=province_data["name"], name_nepali=province_data["name_nepali"]
        )
        provinces.append(province)

        for district_data in province_data["districts"]:
            district = District(
                province=province,
                name=district_data["name"],
                name_nepali=district_data["name_nepali"],
            )
            districts.append(district)

            for municipality_data in district_data["municipalities"]:
                municipality = Municipality(
                    district=district,
                    name=municipality_data["name"],
                    name_nepali=municipality_data["name_nepali"],
                    municipality_type=MunicipalityType(
                        municipality_data["municipality_type"]
                    ),
                )
                municipalities.append(municipality)

    return provinces, districts, municipalities


provinces, districts, municipalities = _loadData()
