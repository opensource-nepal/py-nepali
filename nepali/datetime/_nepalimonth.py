from typing import Union

MONTHS_EN = [
    "Baishakh",
    "Jestha",
    "Ashad",
    "Sharwan",
    "Bhadra",
    "Ashwin",
    "Kartik",
    "Mangsir",
    "Poush",
    "Magh",
    "Falgun",
    "Chaitra",
]

MONTHS_NE = [
    "बैशाख",
    "जेठ",
    "असार",
    "साउन",
    "भदौ",
    "असोज",
    "कात्तिक",
    "मंसिर",
    "पुस",
    "माघ",
    "फागुन",
    "चैत",
]


class nepalimonth_meta(type):
    def __call__(cls, month: Union[int, str], *args, **kwargs):
        """
        Parses the month data and manages the cache.
        """
        value = None

        if isinstance(month, int):
            value = int(month)
        elif isinstance(month, str):
            value = cls._parse_str(month)

        if value is None or value < 1 or value > 12:
            raise ValueError(f"Invalid month: {month}")

        return super(nepalimonth_meta, cls).__call__(value, *args, **kwargs)

    def _parse_str(cls, month: str) -> int:
        """
        Parses str value of the month and returns int
        """
        if month.isdigit():
            return int(month)

        try:
            return (MONTHS_EN + MONTHS_NE).index(month.capitalize()) % 12 + 1
        except ValueError:
            return -1  # invalid month range


class nepalimonth(metaclass=nepalimonth_meta):
    """
    Represents Nepali month: Baishakh, Jestha, ..., Chaitra.
    Baishak: 1,
    Jestha: 2,
    ...
    Chaitra: 3

    >>> nepalimonth(1)
    >>> nepalimonth("Baishakh")
    >>> nepalimonth("बैशाख")

    :param Union[int, str] month: Month data to be parsed.

    :raises TypeError: Invalid object type is passed.
    :raises ValueError: The value is invalid.
    """

    def __init__(self, month) -> None:
        self._value = month

    @property
    def value(self) -> int:
        return self._value

    @property
    def name(self) -> str:
        """Month's english name"""
        return MONTHS_EN[self._value - 1]

    @property
    def name_ne(self) -> str:
        """Month's nepali name"""
        return MONTHS_NE[self._value - 1]
