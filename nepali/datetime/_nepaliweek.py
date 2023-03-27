from typing import Any, Dict, Union

from .constants import WEEKS_EN, WEEKS_NE, WEEKS_ABBR_EN, WEEKS_ABBR_NE


class nepaliweek_meta(type):
    _cache: Dict[int, "nepaliweek"] = {}

    def __call__(cls, week: Union[int, str], *args, **kwargs):
        """
        Parses the week data and manages the cache.
        """
        value = None

        if isinstance(week, int):
            value = int(week)
        elif isinstance(week, str):
            value = cls._parse_str(week)

        # checking if week is valid
        if value is None or value < 1 or value > 7:
            raise ValueError(f"Invalid week: {week}")

        # checking cache
        if value not in cls._cache:
            cls._cache[value] = super(nepaliweek_meta, cls).__call__(
                value, *args, **kwargs
            )

        return cls._cache[value]

    def _parse_str(cls, week: str) -> int:
        """
        Parses str value of the week and returns int
        """
        if week.isdigit():
            return int(week)

        try:
            return (WEEKS_EN + WEEKS_NE + WEEKS_ABBR_EN + WEEKS_ABBR_NE).index(
                week.capitalize()
            ) % 7 + 1
        except ValueError:
            return -1  # invalid week range


class nepaliweek(metaclass=nepaliweek_meta):
    """
    Represents Nepali week: Sunday, Monday, ..., Saturday.
    Sunday: 1,
    Monday: 2,
    ...
    Saturday: 7

    >>> nepaliweek(1)
    >>> nepaliweek("Sunday")
    >>> nepaliweek("आइतबार")
    >>> nepaliweek("Sun")

    :param Union[int, str] week: Week data to be parsed.

    :raises ValueError: The value is invalid.
    """

    def __init__(self, week) -> None:
        self._value = week

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f"<nepaliweek: {self._value}>"

    def __int__(self) -> int:
        return self.value

    def __eq__(self, other: Any) -> bool:
        try:
            return self.value == int(other)
        except:
            return False

    @property
    def value(self) -> int:
        return self._value

    @property
    def name(self) -> str:
        """Week's english name"""
        return WEEKS_EN[self._value - 1]

    @property
    def abbr(self) -> str:
        """Week's english abbreviated name"""
        return WEEKS_ABBR_EN[self._value - 1]

    @property
    def name_ne(self) -> str:
        """Week's nepali name"""
        return WEEKS_NE[self._value - 1]

    @property
    def abbr_ne(self) -> str:
        """Week's nepali abbreviated name"""
        return WEEKS_ABBR_NE[self._value - 1]
