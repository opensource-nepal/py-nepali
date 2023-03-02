"""
Contains the class for the nepalinumber feature
"""

from typing import Any, Tuple, Union


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
        self.value = value

    def __str__(self) -> str:
        """
        Called when the object is called with functions
        like print or logger.debug()
        """
        return str(self.value)

    def __repr__(self) -> str:
        return str(self.value)

    def __int__(self) -> int:
        """
        Called when the object is typecasted into integer
        """
        return int(self.value)

    def __float__(self) -> float:
        """
        Called when the object is typecasted into float
        """
        return float(self.value)

    def __add(self, other) -> Union[int, float]:
        """
        Adds the value in the object with the passed object

        :param other: The other number/object to be added to the object
        :raises TypeError: Raised when unsupported data types
            are added to the nepalinumber object
        :return: A new nepalinumber object with the added values
        """
        if isinstance(other, nepalinumber):
            return self.value + other.value

        return self.value + other

    def __mul(self, other) -> Union[int, float]:
        """
        Multiplies the value in the object with the passed object

        :param other: The other number/object to be added to the object
        :raises TypeError: Raised when unsupported data types
            are multiplied to the nepalinumber object
        :return: A new nepalinumber object with the multiplied values
        """
        if isinstance(other, nepalinumber):
            return self.value * other.value

        return self.value * other

    def __eq__(self, other) -> bool:
        """
        Checks if nepalinumber is equal to another object

        :param other: The other number/object which is to be checked for
            equality againt nepalinumber
        :return: True if equal else False
        """
        if isinstance(other, nepalinumber):
            return self.value == other.value

        return self.value == other

    def __ne__(self, other) -> bool:
        """
        Checks if nepalinumber is not equal to another object

        :param other: The other number/object which is to be checked for
            equality againt nepalinumber
        :return: True if not equal else False
        """
        if isinstance(other, nepalinumber):
            return self.value != other.value

        return self.value != other

    def __neg__(self) -> "nepalinumber":
        """
        Returns the negative value of the nepalinumber value
        """
        return nepalinumber((-1) * self.value)

    def __add__(self, other) -> "nepalinumber":
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
            return nepalinumber(self.__add(other))
        except TypeError:
            raise TypeError(
                f"unsupported operand type(s) for +: 'nepalinumber' and '{type(other).__name__}'"
            ) from None  # resets stacktrace because we don't
        # want to show stacktrace from self.__add()

    def __radd__(self, other) -> "nepalinumber":
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
            return nepalinumber(self.__add(other))
        except TypeError:
            raise TypeError(
                f"unsupported operand type(s) for +: '{type(other).__name__}' and 'nepalinumber'"
            ) from None

    def __sub__(self, other) -> "nepalinumber":
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
                return nepalinumber(self.value - other.value)

            return nepalinumber(self.value - other)
        except TypeError:
            raise TypeError(
                f"unsupported operand type(s) for -: 'nepalinumber' and '{type(other).__name__}'"
            ) from None

    def __rsub__(self, other) -> "nepalinumber":
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
                return nepalinumber(other.value - self.value)

            return nepalinumber(other - self.value)
        except TypeError:
            raise TypeError(
                f"unsupported operand type(s) for -: '{type(other).__name__}' and 'nepalinumber'"
            ) from None

    def __mul__(self, other) -> "nepalinumber":
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
            return nepalinumber(self.__mul(other))
        except TypeError:
            raise TypeError(
                f"unsupported operand type(s) for *: 'nepalinumber' and '{type(other).__name__}'"
            ) from None

    def __rmul__(self, other) -> "nepalinumber":
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
            return nepalinumber(self.__mul(other))
        except TypeError:
            raise TypeError(
                f"unsupported operand type(s) for *: '{type(other).__name__}' and 'nepalinumber'"
            ) from None

    def __truediv__(self, other) -> "nepalinumber":
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
                return nepalinumber(self.value / other.value)

            return nepalinumber(self.value / other)
        except TypeError:
            raise TypeError(
                f"unsupported operand type(s) for /: 'nepalinumber' and '{type(other).__name__}'"
            ) from None

    def __rtruediv__(self, other) -> "nepalinumber":
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
                return nepalinumber(other.value / self.value)

            return nepalinumber(other / self.value)
        except TypeError:
            raise TypeError(
                f"unsupported operand type(s) for /: '{type(other).__name__}' and 'nepalinumber'"
            ) from None

    def __floordiv__(self, other) -> "nepalinumber":
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
                return nepalinumber(self.value // other.value)

            return nepalinumber(self.value // other)
        except TypeError:
            raise TypeError(
                f"unsupported operand type(s) for //: 'nepalinumber' and '{type(other).__name__}'"
            ) from None

    def __rfloordiv__(self, other) -> "nepalinumber":
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
                return nepalinumber(other.value // self.value)

            return nepalinumber(other // self.value)
        except TypeError:
            raise TypeError(
                f"unsupported operand type(s) for //: '{type(other).__name__}' and 'nepalinumber'"
            ) from None

    def __mod__(self, other) -> "nepalinumber":
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
                return nepalinumber(self.value % other.value)

            return nepalinumber(self.value % other)
        except TypeError:
            raise TypeError(
                f"unsupported operand type(s) for %: 'nepalinumber' and '{type(other).__name__}'"
            ) from None

    def __rmod__(self, other) -> "nepalinumber":
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
                return nepalinumber(other.value % self.value)

            return nepalinumber(other % self.value)
        except TypeError:
            raise TypeError(
                f"unsupported operand type(s) for %: '{type(other).__name__}' and 'nepalinumber'"
            ) from None

    def __divmod__(self, other) -> Tuple["nepalinumber", "nepalinumber"]:
        """
        Called when the built-in function divmod() is used
        with nepalinumber as the dividend and other as divisior

        :param other: The other number/object that is to be
            divisior for the value in the nepalinumber object
        :raises TypeError: Raised when unsupported data types are
            used as divisior for nepalinumber object
        :return: Returns a tuple of quotient and remainder
        """
        try:
            if isinstance(other, nepalinumber):
                quotient, remainder = divmod(self.value, other.value)

            quotient, remainder = divmod(self.value, other)

            return nepalinumber(quotient), nepalinumber(remainder)
        except TypeError:
            raise TypeError(
                f"unsupported operand type(s) for divmod(): 'nepalinumber' and '{type(other).__name__}'"
            ) from None

    def __rdivmod__(self, other) -> Tuple["nepalinumber", "nepalinumber"]:
        """
        Called when the built-in function divmod() is used
        with nepalinumber as the divisior and other as divident

        :param other: The other number/object that is to be
            dividend for the value in the nepalinumber object
        :raises TypeError: Raised when unsupported data types are
            used as dividend for nepalinumber object
        :return: Returns a tuple of quotient and remainder
        """
        try:
            if isinstance(other, nepalinumber):
                quotient, remainder = divmod(other.value, self.value)

            quotient, remainder = divmod(other, self.value)

            return nepalinumber(quotient), nepalinumber(remainder)
        except TypeError:
            raise TypeError(
                f"unsupported operand type(s) for divmod(): '{type(other).__name__}' and 'nepalinumber'"
            ) from None

    def __pow__(self, other) -> "nepalinumber":
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
                return nepalinumber(self.value**other.value)

            return nepalinumber(self.value**other)
        except TypeError:
            raise TypeError(
                f"unsupported operand type(s) for ** or pow(): 'nepalinumber' and '{type(other).__name__}'"
            ) from None

    def __rpow__(self, other) -> "nepalinumber":
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
                return nepalinumber(other.value**self.value)

            return nepalinumber(other**self.value)
        except TypeError:
            raise TypeError(
                f"unsupported operand type(s) for ** or pow(): '{type(other).__name__}' and 'nepalinumber'"
            ) from None
