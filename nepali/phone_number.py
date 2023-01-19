import re
from enum import Enum


_mobile_number_re = re.compile(r"^(?:\+977|977)?(?:-)?(?:98[0-7]|97[0-6]|[89][0-9]|[0][1789])[0-9]{8}$")
_landline_number_re = re.compile(r"^(?:\+977|977)?(?:-)?(?:0)?(?:[01][1-9]|2[13-9]|[3-9][0-9])[0-9]{6,7}$")


class Operators(Enum):
    NEPAL_TELECOM = "Nepal Telecom"
    NCELL = "Ncell"
    SMART_CELL = "Smart Cell"
    UTL = "UTL"
    HELLO_MOBILE = "Hello Mobile"

    def __str__(self) -> str:
        return self.value


def is_mobile_number(number: str) -> bool:
    """
    Returns True is the input number is mobile number.

    >>> is_mobile = is_mobile_number(number)
    >>> if is_mobile:
    >>>     ...
    """
    try:
        return bool(_mobile_number_re.match(number))
    except:
        return False


def is_landline_number(number: str) -> bool:
    """
    Returns True is the input number is mobile number.

    >>> is_mobile = is_mobile_number(number)
    >>> if is_mobile:
    >>>     ...
    """
    try:
        return bool(_landline_number_re.match(number))
    except:
        return False


def is_valid(number: str) -> bool:
    return is_mobile_number(number) or is_landline_number(number)


def get_exact_number(number: str) -> str:
    # replacing start 977
    if number.startswith('977'):
        number = number.replace('977', '')
    # replacing +977 and all -
    return number.replace('+977', '').replace('-', '')


def parse(number: str):
    """
    TODO: To be implemented
    """
    if not number and type(number) != str:
        return None

    number = number.replace('-', '')

    # checking if mobile number
    if is_mobile_number(number):
        return _parse_mobile_number(number)

    if is_landline_number(number):
        return _parse_mobile_number(number)

    return None


def _parse_mobile_number(number: str) -> dict:
    """
    TODO: To be implemented
    """
    number = get_exact_number(number)
    detail = {
        "type": "Mobile",
        "number": number,
    }
    return detail


def _parse_landline_number(number) -> dict:
    """
    TODO: To be implemented
    """
    number = get_exact_number(number)
    return {
        "type": "Landline",
        "number": number,
    }
