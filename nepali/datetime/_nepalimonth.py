from functools import cached_property
from typing import Any, Dict, Optional, Union

from .constants import MONTHS_EN, MONTHS_NE


class NepaliMonthMeta(type):
    _cache: Dict[int, "nepalimonth"] = {}

    def __call__(cls, month: Union[int, str], *args, **kwargs) -> "nepalimonth":
        """
        Parses the month data and manages the cache.

        :param month: An integer or string representing the month.
        :type month: Union[int, str]
        :return: An instance of the nepalimonth class representing the given month.
        :rtype: nepalimonth
        :raises ValueError: If the given month is invalid.
        """
        value: Optional[int] = None
        value = None

        if isinstance(month, int):
            value = int(month)
        elif isinstance(month, str):
            try:
                value = cls._parse_str(month)
            except ValueError:
                pass

        # checking if month is valid
        if value is None or value < 1 or value > 12:
            raise ValueError(f"Invalid month: {month}")

        # checking cache
        if value not in cls._cache:
            cls._cache[value] = super(NepaliMonthMeta, cls).__call__(
                value, *args, **kwargs
            )

        return cls._cache[value]

    def _parse_str(cls, month: str) -> int:
        """
        Parses str value of the month and returns int.

        :param month: A string representing the month.
        :type month: str
        :return: An integer representing the month.
        :rtype: int
        :raises ValueError: If the given string does not represent a valid month.
        """
        if month.isdigit():
            return int(month)

        month = month.capitalize()
        month_names = MONTHS_EN + MONTHS_NE
        try:
            index = month_names.index(month)
        except ValueError:
            raise ValueError(f"Invalid month name: {month}")

        return (index % 12) + 1


class nepalimonth(metaclass=NepaliMonthMeta):
    """
    Represents Nepali month: Baishakh, Jestha, ..., Chaitra.
    Baishak: 1,
    Jestha: 2,
    ...
    Chaitra: 12

    >>> nepalimonth(1)
    >>> nepalimonth("Baishakh")
    >>> nepalimonth("बैशाख")

    :param Union[int, str] month: Month data to be parsed.

    :raises ValueError: The value is invalid.
    """

    def __init__(self, month) -> None:
        self.__value = month

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f"<nepalimonth: {self.__value}>"

    def __int__(self) -> int:
        return self.value

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, nepalimonth):
            return self.value == other.value
        elif isinstance(other, int):
            return self.value == other

        return False

    @cached_property
    def value(self) -> int:
        return self.__value

    @cached_property
    def name(self) -> str:
        """Month's english name"""
        return MONTHS_EN[self.__value - 1]

    @cached_property
    def name_ne(self) -> str:
        """Month's nepali name"""
        return MONTHS_NE[self.__value - 1]
