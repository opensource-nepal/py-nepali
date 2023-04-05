from typing import Any


NP_NUMBERS = ["०", "१", "२", "३", "४", "५", "६", "७", "८", "९"]
NP_NUMBERS_SET = set(NP_NUMBERS)


def english_to_nepali(number: Any) -> str:
    """
    Converts english number to nepali.
    """
    number = str(number)
    converted_number = []
    for n in number:
        num = ord(n) - ord("0")
        if num in range(0, 10):
            converted_number.append(NP_NUMBERS[num])
        else:
            converted_number.append(n)
    return "".join(converted_number)


def nepali_to_english(number: Any) -> str:
    """
    Converts nepali number to english.
    """
    number = str(number)
    converted_number = []
    for n in number:
        if n in NP_NUMBERS_SET:
            converted_number.append(str(NP_NUMBERS.index(n)))
        else:
            converted_number.append(n)
    return "".join(converted_number)


def add_comma_english(number: Any) -> str:
    """
    Adds comma in english style
    Eg. 123456789 => 123,456,789
    """
    return "{:,}".format(int(number))


def add_comma(number: Any, convert=False) -> str:
    """
    Adds comma in nepali style
    Eg. 123456789 => 12,34,56,789

    :param number Any: Number to be converted
    :param convert bool: If true converts english number to nepali
    """
    if convert:
        number = english_to_nepali(number)
    else:
        number = str(number)

    number_with_comma = []
    counter = 0
    for nepali_number_char in list(str(number))[::-1]:
        if counter == 3 or (counter != 1 and (counter - 1) % 2 == 0):
            number_with_comma.append(",")
        number_with_comma.append(nepali_number_char)
        counter += 1

    return "".join(number_with_comma[::-1])


def convert_and_add_comma(number: Any) -> str:
    """
    Converts the number into nepali text and adds comma to it.
    """
    return add_comma(number, convert=True)
