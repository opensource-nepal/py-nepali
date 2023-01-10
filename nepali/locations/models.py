from enum import Enum


class Location:
    def __init__(self, name, name_nepali):
        self.__name = name
        self.__name_nepali = name_nepali

    @property
    def name(self):
        return self.__name

    @property
    def name_nepali(self):
        return self.__name_nepali


class Province(Location):
    def __init__(self, name: str, name_nepali: str):
        super().__init__(name, name_nepali)
        self.__districts = []

    def _set_districts(self, districts: list["District"]) -> None:
        self.__districts = districts

    def _add_district(self, district: "District") -> None:
        self.__districts.append(district)

    @property
    def districts(self) -> list["District"]:
        return self.__districts

    @property
    def municipalities(self) -> list["Municipality"]:
        return []


class District(Location):
    def __init__(self, province: Province, name: str, name_nepali: str):
        super().__init__(name, name_nepali)
        self.__province = province
        self.__municipalities = []
        self.__province._add_district(self)

    def _set_municipalities(self, municipalities: list["Municipality"]) -> None:
        self.__municipalities = municipalities

    def _add_municipality(self, district: "Municipality") -> None:
        self.__municipalities.append(district)

    @property
    def province(self) -> Province:
        return self.__province

    @property
    def municipalities(self) -> list["Municipality"]:
        return self.__municipalities


class MunicipalityType(Enum):
    METROPOLITAN = "Metropolitan City"
    SUB_METROPOLITAN = "Sub-Metropolitan City"
    MUNICIPALITY = "Municipality"
    RURAL_MUNICIPALITY = "Rural Municipality"

    def __str__(self) -> str:
        return self.value


class Municipality(Location):
    def __init__(self, district: District, name: str, name_nepali: str, municipality_type: MunicipalityType):
        super().__init__(name, name_nepali)
        self.__district = district
        self.__municipality_type = municipality_type
        self.__district._add_municipality(self)

    @property
    def province(self) -> Province:
        return self.district.province

    @property
    def district(self) -> District:
        return self.__district

    @property
    def municipality_type(self) -> MunicipalityType:
        return self.__municipality_type
