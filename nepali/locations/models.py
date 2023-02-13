from enum import Enum
from typing import List


class Location:
    def __init__(self, name: str, name_nepali: str):
        self.__name = name
        self.__name_nepali = name_nepali

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

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
        self.__municipalities = []

    def _add_district(self, district: "District") -> None:
        """Do not use outside of the model, automatically called from the models."""
        self.__districts.append(district)

    def _add_municipality(self, municipality: "Municipality") -> None:
        """Do not use outside of the model, automatically called from the models."""
        self.__municipalities.append(municipality)

    @property
    def districts(self) -> List["District"]:
        return self.__districts

    @property
    def municipalities(self) -> List["Municipality"]:
        return self.__municipalities


class District(Location):
    def __init__(self, province: Province, name: str, name_nepali: str):
        super().__init__(name, name_nepali)
        self.__province = province
        self.__municipalities = []
        self.__province._add_district(self)

    def _add_municipality(self, district: "Municipality") -> None:
        """Do not use outside of the model, automatically called from the models."""
        self.__municipalities.append(district)

    @property
    def province(self) -> Province:
        return self.__province

    @property
    def municipalities(self) -> List["Municipality"]:
        return self.__municipalities


class MunicipalityType(Enum):
    METROPOLITAN = "Metropolitan City"
    SUB_METROPOLITAN = "Sub-Metropolitan City"
    MUNICIPALITY = "Municipality"
    RURAL_MUNICIPALITY = "Rural Municipality"

    def __str__(self) -> str:
        return self.value

    def __repr__(self) -> str:
        return self.value


class Municipality(Location):
    def __init__(
        self,
        district: District,
        name: str,
        name_nepali: str,
        municipality_type: MunicipalityType,
    ):
        super().__init__(name, name_nepali)
        self.__district = district
        self.__municipality_type = municipality_type
        self.__district._add_municipality(self)
        self.__district.province._add_municipality(self)

    @property
    def province(self) -> Province:
        return self.district.province

    @property
    def district(self) -> District:
        return self.__district

    @property
    def municipality_type(self) -> MunicipalityType:
        return self.__municipality_type
