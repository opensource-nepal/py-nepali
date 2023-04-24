"""
Contains the class for the nepalinumber feature
"""

from typing import Any, Tuple, Type, Union
from .utils import NP_NUMBERS, NP_NUMBERS_SET, english_to_nepali


class nepalinumber:
    """
    Represents the nepali(devanagari) numbers and
    the features related to arithmetic operations
    on them
    """

    def __init__(self, value: Any) -> None:
        """
        Constructor/Initializer
        """
        self.__value = self.__parse(value)

    def _raise_parse_exception(self, obj, ex_class: Type[Exception] = ValueError):
        raise ex_class(
            f"could not convert {obj.__class__.__name__} to {self.__class__.__name__}: '{obj}'"
        ) from None

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

    def __convert_or_return(self, obj) -> Union["nepalinumber", object]:
        """
        Will try to parse the given object and convert to nepalinumber
        else will return the same object

        :param obj: The object to convert

        :returns: Either a nepalinumber or the same object unchanged
        """
        try:
            return nepalinumber(obj)
        except (TypeError, ValueError):
            return obj

    def __str__(self) -> str:
        """
        Called when the object is called with functions
        like print or logger.debug()
        """
        return str(self.__value)

    def __repr__(self) -> str:
        return str(self.__value)

    def __int__(self) -> int:
        """
        Called when the object is typecasted into integer
        """
        return int(self.__value)

    def __float__(self) -> float:
        """
        Called when the object is typecasted into float
        """
        return float(self.__value)

    def __add(self, other) -> Union[int, float]:
        """
        Adds the value in the object with the passed object

        :param other: The other number/object to be added to the object
        :raises TypeError: Raised when unsupported data types
            are added to the nepalinumber object
        :return: A new nepalinumber object with the added values
        """
        if isinstance(other, nepalinumber):
            return self.__value + other.value

        return self.__value + other

    def __mul(self, other) -> Union[int, float]:
        """
        Multiplies the value in the object with the passed object

        :param other: The other number/object to be added to the object
        :raises TypeError: Raised when unsupported data types
            are multiplied to the nepalinumber object
        :return: A new nepalinumber object with the multiplied values
        """
        if isinstance(other, nepalinumber):
            return self.__value * other.value

        return self.__value * other

    def __eq__(self, other) -> bool:
        """
        Checks if nepalinumber is equal to another object

        :param other: The other number/object which is to be checked for
            equality againt nepalinumber
        :return: True if equal else False
        """
        if isinstance(other, nepalinumber):
            return self.__value == other.value

        return self.__value == other

    def __ne__(self, other) -> bool:
        """
        Checks if nepalinumber is not equal to another object

        :param other: The other number/object which is to be checked for
            equality againt nepalinumber
        :return: True if not equal else False
        """
        if isinstance(other, nepalinumber):
            return self.__value != other.value

        return self.__value != other

    def __neg__(self) -> "nepalinumber":
        """
        Returns the negative value of the nepalinumber value
        """
        return nepalinumber((-1) * self.__value)

    def __add__(self, other) -> Union["nepalinumber", object]:
        """
        Called when the addition operator +  is used after
        the nepalinumber object

        :param other: The other number/object that is to be
            added to the value onto the nepalinumber object
        :raises TypeError: Raised when unsupported data types
            are added to the nepalinumber object
        :return: Returns the added value as a nepalinumber
            object
        """
        try:
            return self.__convert_or_return(self.__add(other))
        except TypeError:
            return NotImplemented

    def __radd__(self, other) -> Union["nepalinumber", object]:
        """
        Called when the addition operator + is used before
        the nepalinumber object

        :param other: The other number/object that is to be
            added to the value onto the nepalinumber object
        :raises TypeError: Raised when nepalinumber object is
            added to unsupported data types
        :return: Returns the added value as a nepalinumber
            object
        """
        try:
            return self.__convert_or_return(self.__add(other))
        except TypeError:
            return NotImplemented

    def __sub__(self, other) -> Union["nepalinumber", object]:
        """
        Called when the subtraction operator - is used after
        the nepalinumber object

        :param other: The other number/object that is to be
            subtracted from the value in the nepalinumber object
        :raises TypeError: Raised when unsupported data types are
            subtracted from nepalinumber object
        :return: Returns the subtracted number as a nepalinumber object
        """
        try:
            if isinstance(other, nepalinumber):
                return self.__convert_or_return(self.__value - other.value)

            return self.__convert_or_return(self.__value - other)
        except TypeError:
            return NotImplemented

    def __rsub__(self, other) -> Union["nepalinumber", object]:
        """
        Called when the subtraction operator - is used before
        the nepalinumber object

        :param other: The other number/object that is to get
            subtracted by the value in the nepalinumber object
        :raises TypeError: Raised when nepalinumber object is
            subtracted from  unsupported data types
        :return: Returns the subtracted number as a nepalinumber
             object
        """
        try:
            if isinstance(other, nepalinumber):
                return self.__convert_or_return(other.value - self.__value)

            return self.__convert_or_return(other - self.__value)
        except TypeError:
            return NotImplemented

    def __mul__(self, other) -> Union["nepalinumber", object]:
        """
        Called when the multiplication operator * is used after
        the nepalinumber object

        :param other: The other number/object that is to be
            multiplied to the value onto the nepalinumber object
        :raises TypeError: Raised when unsupported data types
            are multiplied to the nepalinumber object
        :return: Returns the multiplied value as a nepalinumber
            object
        """
        try:
            if isinstance(other, str):
                return self.__value * other  # type: ignore

            return self.__convert_or_return(self.__mul(other))
        except TypeError:
            return NotImplemented

    def __rmul__(self, other) -> Union["nepalinumber", object]:
        """
        Called when the multiplication operator * is used before
        the nepalinumber object

        :param other: The other number/object that is to be
            multiplied to the value onto the nepalinumber object
        :raises TypeError: Raised when nepalinumber object is
            multiplied to unsupported data types
        :return: Returns the multiplied value as a nepalinumber
            object
        """
        try:
            if isinstance(other, str):
                return other * self.__value  # type: ignore

            return self.__convert_or_return(self.__mul(other))
        except TypeError:
            return NotImplemented

    def __truediv__(self, other) -> Union["nepalinumber", object]:
        """
        Called when the division operator / is used after
        the nepalinumber object

        :param other: The other number/object that is to divide
            the value in the nepalinumber object
        :raises TypeError: Raised when unsupported data types are
            used to divide nepalinumber object
        :return: Returns the quotient number as a nepalinumber object
        """
        try:
            if isinstance(other, nepalinumber):
                return self.__convert_or_return(self.__value / other.value)

            return self.__convert_or_return(self.__value / other)
        except TypeError:
            return NotImplemented

    def __rtruediv__(self, other) -> Union["nepalinumber", object]:
        """
        Called when the division operator / is used before
        the nepalinumber object

        :param other: The other number/object that is to get
            dividied by the value in the nepalinumber object
        :raises TypeError: Raised when nepalinumber object is
            used to divide unsupported data types
        :return: Returns the quotient number as a nepalinumber
             object
        """
        try:
            if isinstance(other, nepalinumber):
                return self.__convert_or_return(other.value / self.__value)

            return self.__convert_or_return(other / self.__value)
        except TypeError:
            return NotImplemented

    def __floordiv__(self, other) -> Union["nepalinumber", object]:
        """
        Called when the floor/integer division operator // is used
        after the nepalinumber object

        :param other: The other number/object that is to divide
            the value in the nepalinumber object
        :raises TypeError: Raised when unsupported data types are
            used to divide nepalinumber object
        :return: Returns the quotient number as a nepalinumber object
        """
        try:
            if isinstance(other, nepalinumber):
                return self.__convert_or_return(self.__value // other.value)

            return self.__convert_or_return(self.__value // other)
        except TypeError:
            return NotImplemented

    def __rfloordiv__(self, other) -> Union["nepalinumber", object]:
        """
        Called when the floor/integer division operator // is used
        before the nepalinumber object

        :param other: The other number/object that is to get
            dividied by the value in the nepalinumber object
        :raises TypeError: Raised when nepalinumber object is
            used to divide unsupported data types
        :return: Returns the quotient number as a nepalinumber
             object
        """
        try:
            if isinstance(other, nepalinumber):
                return self.__convert_or_return(other.value // self.__value)

            return self.__convert_or_return(other // self.__value)
        except TypeError:
            return NotImplemented

    def __mod__(self, other) -> Union["nepalinumber", object]:
        """
        Called when the modulo operator % is used after
        the nepalinumber object

        :param other: The other number/object that is to be
            perform modulo division from the value in the
            nepalinumber object
        :raises TypeError: Raised when unsupported data types are
            modulo divided from nepalinumber object
        :return: Returns the remainder number as a nepalinumber object
        """
        try:
            if isinstance(other, nepalinumber):
                return self.__convert_or_return(self.__value % other.value)

            return self.__convert_or_return(self.__value % other)
        except TypeError:
            return NotImplemented

    def __rmod__(self, other) -> Union["nepalinumber", object]:
        """
        Called when the modulo operator % is used before
        the nepalinumber object

        :param other: The other number/object that is to get
            modulo divided by the value in the nepalinumber object
        :raises TypeError: Raised when nepalinumber object is
            used modulo divide unsupported data types
        :return: Returns the remainder number as a nepalinumber
             object
        """
        try:
            if isinstance(other, nepalinumber):
                return self.__convert_or_return(other.value % self.__value)

            return self.__convert_or_return(other % self.__value)
        except TypeError:
            return NotImplemented

    def __divmod__(
        self, other
    ) -> Tuple[Union["nepalinumber", object], Union["nepalinumber", object]]:
        """
        Called when the built-in function divmod() is used
        with nepalinumber as the dividend and other as divisor

        :param other: The other number/object that is to be
            divisor for the value in the nepalinumber object
        :raises TypeError: Raised when unsupported data types are
            used as divisor for nepalinumber object
        :return: Returns a tuple of quotient and remainder
        """
        try:
            if isinstance(other, nepalinumber):
                quotient, remainder = divmod(self.__value, other.value)

            quotient, remainder = divmod(self.__value, other)

            return self.__convert_or_return(quotient), self.__convert_or_return(
                remainder
            )
        except TypeError:
            return NotImplemented

    def __rdivmod__(
        self, other
    ) -> Tuple[Union["nepalinumber", object], Union["nepalinumber", object]]:
        """
        Called when the built-in function divmod() is used
        with nepalinumber as the divisor and other as dividend

        :param other: The other number/object that is to be
            dividend for the value in the nepalinumber object
        :raises TypeError: Raised when unsupported data types are
            used as dividend for nepalinumber object
        :return: Returns a tuple of quotient and remainder
        """
        try:
            if isinstance(other, nepalinumber):
                quotient, remainder = divmod(other.value, self.__value)

            quotient, remainder = divmod(other, self.__value)

            return self.__convert_or_return(quotient), self.__convert_or_return(
                remainder
            )
        except TypeError:
            return NotImplemented

    def __pow__(self, other) -> Union["nepalinumber", object]:
        """
        Called when the power operator **  is used after
        the nepalinumber object

        :param other: The other number/object that is to be
            powered to the value onto the nepalinumber object
        :raises TypeError: Raised when unsupported data types
            are powered to the nepalinumber object
        :return: Returns the powered by value as a nepalinumber
            object
        """
        try:
            if isinstance(other, nepalinumber):
                return self.__convert_or_return(self.__value**other.value)

            return self.__convert_or_return(self.__value**other)
        except TypeError:
            return NotImplemented

    def __rpow__(self, other) -> Union["nepalinumber", object]:
        """
        Called when the power operator ** is used before
        the nepalinumber object

        :param other: The other number/object that is to be
            powered by the value onto the nepalinumber object
        :raises TypeError: Raised when unsupported data types
            are powered by the nepalinumber object
        :return: Returns the powered by value as a nepalinumber
            object
        """
        try:
            if isinstance(other, nepalinumber):
                return self.__convert_or_return(other.value**self.__value)

            return self.__convert_or_return(other**self.__value)
        except TypeError:
            return NotImplemented

    def str_ne(self) -> str:
        """
        Returns nepali (devanagari) format for the number

        :return: Stringified Nepali number
        """
        if not hasattr(self, "__str_ne"):
            self.__str_ne = english_to_nepali(self.__value)
        return self.__str_ne

    @property
    def value(self):
        return self.__value
