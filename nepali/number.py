import warnings
from typing import Any


NP_NUMBERS = ["०", "१", "२", "३", "४", "५", "६", "७", "८", "९"]


def english_to_nepali(number: Any) -> str:
    """
    Converts english number to nepali.
    """
    number = str(number)
    converted_number = []
    for n in number:
        if n.isdigit() and int(n) in range(0, 10):
            converted_number.append(str(NP_NUMBERS[int(n)]))
        else:
            converted_number.append(n)
    return "".join(converted_number)


def nepali_to_english(number: Any) -> str:
    """
    Converts nepali number to english.
    """
    number = str(number)
    converted_number = []
    nepali_number_set = set(NP_NUMBERS)
    for n in number:
        if n in nepali_number_set:
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
    
    :param number: Number to be converted
    :param convert bool: If true converts english number to nepali
    """
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
    
    """
    return add_comma(english_to_nepali(number))


# Backward compatibility support for legacy NepaliNumber
class NepaliNumber:
    @classmethod
    def convert_and_add_comma(cls, number):
        warnings.warn(
            message="NepaliNumber.convert_and_add_comma has been moved to `convert_and_add_comma. This function is depreciated and will be removed in the future release.",
            category=DeprecationWarning,
        )
        return add_comma(english_to_nepali(number))

    @staticmethod
    def convert(num):
        warnings.warn(
            message="NepaliNumber.convert has been moved to `english_to_nepali. This function is depreciated and will be removed in the future release.",
            category=DeprecationWarning,
        )
        return english_to_nepali(num)

    @staticmethod
    def revert(num):
        warnings.warn(
            message="NepaliNumber.revert has been moved to `nepali_to_english. This function is depreciated and will be removed in the future release.",
            category=DeprecationWarning,
        )
        return nepali_to_english(num)

    @staticmethod
    def add_comma(number):
        warnings.warn(
            message="NepaliNumber.add_comma has been moved to `add_comma. This function is depreciated and will be removed in the future release.",
            category=DeprecationWarning,
        )
        return add_comma(number)

    @staticmethod
    def add_comma_english(number):
        warnings.warn(
            message="NepaliNumber.add_comma_english has been moved to `add_comma_english. This function is depreciated and will be removed in the future release.",
            category=DeprecationWarning,
        )
        return add_comma_english(number)
