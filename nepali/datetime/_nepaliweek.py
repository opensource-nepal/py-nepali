from functools import cached_property
from typing import Any, Dict, Optional, Union

from .constants import WEEKS_EN, WEEKS_NE, WEEKS_ABBR_EN, WEEKS_ABBR_NE


class NepaliWeekMeta(type):
    _cache: Dict[int, "nepaliweek"] = {}

    def __call__(cls, week: Union[int, str], *args, **kwargs) -> "nepaliweek":
        """
        Parses the week data and manages the cache.

        :param week: An integer or string representing the week.
        :type week: Union[int, str]
        :return: An instance of the nepaliweek class representing the given week.
        :rtype: nepaliweek
        :raises ValueError: If the given week is invalid.
        """
        value: Optional[int] = None

        if isinstance(week, int):
            value = int(week)
        elif isinstance(week, str):
            try:
                value = cls._parse_str(week)
            except ValueError:
                pass

        # checking if week is valid
        if value is None or not (0 <= value <= 6):
            raise ValueError(f"Invalid week: {week}")

        # checking cache
        if value not in cls._cache:
            cls._cache[value] = super().__call__(value, *args, **kwargs)

        return cls._cache[value]

    def _parse_str(cls, week: str) -> int:
        """
        Parses str value of the week and returns int.

        :param week: A string representing the week.
        :type week: str
        :return: An integer representing the week.
        :rtype: int
        :raises ValueError: If the given string does not represent a valid week.
        """
        if week.isdigit():
            return int(week)

        week = week.capitalize()
        week_names = WEEKS_EN + WEEKS_NE + WEEKS_ABBR_EN + WEEKS_ABBR_NE
        try:
            index = week_names.index(week)
        except ValueError:
            raise ValueError(f"Invalid week name: {week}")

        return index % 7


class nepaliweek(metaclass=NepaliWeekMeta):
    """
    Represents Nepali week: Sunday, Monday, ..., Saturday.
    Sunday: 0,
    Monday: 1,
    ...
    Saturday: 6

    >>> nepaliweek(0)
    >>> nepaliweek("Sunday")
    >>> nepaliweek("आइतबार")
    >>> nepaliweek("Sun")

    :param Union[int, str] week: Week data to be parsed.
    :raises ValueError: The value is invalid.
    """

    def __init__(self, week) -> None:
        self.__value = week

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f"<nepaliweek: {self.__value}>"

    def __int__(self) -> int:
        return self.value

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, nepaliweek):
            return self.value == other.value
        elif isinstance(other, int):
            return self.value == other

        return False

    @cached_property
    def value(self) -> int:
        return self.__value

    @cached_property
    def name(self) -> str:
        """Week's english name"""
        return WEEKS_EN[self.__value]

    @cached_property
    def abbr(self) -> str:
        """Week's english abbreviated name"""
        return WEEKS_ABBR_EN[self.__value]

    @cached_property
    def name_ne(self) -> str:
        """Week's nepali name"""
        return WEEKS_NE[self.__value]

    @cached_property
    def abbr_ne(self) -> str:
        """Week's nepali abbreviated name"""
        return WEEKS_ABBR_NE[self.__value]
