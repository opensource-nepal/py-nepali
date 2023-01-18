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


def parse(number: str):
    if not number and type(number) != str:
        return None

    number = number.replace('-', '')

    # checking if mobile number
    match = _mobile_number_re.match(number)
    if match:
        return _parse_mobile_number(number)

    match = _landline_number_re.match(number)
    if match:
        return _parse_mobile_number(number)

    return None

def get_exact_number(number: str) -> str:
    # replacing start 977
    if number.startswith('977'):
        number.replace('977', '')

    # replacing +977
    number.replace('+977', '')

    # replacing all -
    number.replace('-', '')
    return number

def _parse_mobile_number(number: str) -> dict:
    number = get_exact_number(number)
    detail = {
        "type": "Mobile",
        "number": number,
    }
    return detail

def _parse_landline_number(number) -> dict:
    number = get_exact_number(number)
    return {
        "type": "Landline",
        "number": number,
    }