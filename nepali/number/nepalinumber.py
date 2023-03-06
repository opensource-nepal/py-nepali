"""
Contains the class for the nepalinumber feature
"""


from typing import Any, Type, Union
from .utils import NP_NUMBERS, NP_NUMBERS_SET


class nepalinumber:
    """
    Represents the nepali(devanagari) numbers and
    the features related to arithmetic operations
    on them
    """

    def __init__(self, value) -> None:
        """
        Constructor/Initializer
        """
        self.value = self.__parse(value)

    def _raise_parse_exception(self, obj, ex_class: Type[Exception] = ValueError):
        raise ex_class(
            f"could not convert {obj.__class__.__name__} to {self.__class__.__name__}: '{obj}'"
        )

    def __parse(self, value: Any) -> Union[int, float]:
        """
        Parses nepali number input into a valid value.

        Eg:
        >>> self.__parse("१२")
        12
        >>> self.__parse("१२.३")
        12.3
        >>> self.__parse(1)
        1
        >>> self.__parse("invalid")
        ValueError: could not convert str to nepalinumber: 'invalid'

        :param value: Value to be parsed.
        :return: returns value int or float
        :raises ValueError: If the value is invalid
        :raises TypeError: If the value object can't be parsed
        """
        if isinstance(value, int):
            return int(value)

        elif isinstance(value, float):
            return float(value)

        elif isinstance(value, str):
            return self.__parse_str(value)

        return self.__parse_object(value)

    def __parse_str(self, value: str) -> Union[int, float]:
        """
        Parses str object into int and float.
        This is a low level implementation.

        :raises ValueError: If the value is invalid
        """
        result = 0
        sign = 1
        decimal_found = False
        decimal_place = 1
        i = 0

        # for negative sign
        if value[0] == "-":
            sign = -1
            i = 1

        while i < len(value):
            # decimal number found
            if value[i] == ".":
                if decimal_found:
                    # decimal was already found
                    self._raise_parse_exception(value)
                decimal_found = True
                i += 1
                continue

            digit = ord(value[i]) - ord("0")
            if digit < 0 or digit > 9:
                # checking nepali character
                if value[i] not in NP_NUMBERS_SET:
                    self._raise_parse_exception(value)
                digit = NP_NUMBERS.index(value[i])

            if decimal_found:
                decimal_place /= 10
                result += digit * decimal_place
            else:
                result = result * 10 + digit

            i += 1
        return sign * result

    def __parse_object(self, obj: Any) -> Union[int, float]:
        """
        Parses object using __int__, __float__, and __str__.

        :raises TypeError: If the value object can't be parsed
        """
        try:
            if hasattr(obj, "__float__"):
                return float(obj)
            elif hasattr(obj, "__int__"):
                return int(obj)
            return self.__parse_str(str(obj))
        except (ValueError, TypeError):
            # object conversion must raise TypeError if fails
            self._raise_parse_exception(obj, ex_class=TypeError)
