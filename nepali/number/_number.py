import warnings

from .utils import (
    add_comma,
    add_comma_english,
    english_to_nepali,
    nepali_to_english,
)


# Backward compatibility support for legacy NepaliNumber
class NepaliNumber:
    @classmethod
    def convert_and_add_comma(cls, number):
        warnings.warn(
            message="NepaliNumber.convert_and_add_comma has been moved to "
            "`convert_and_add_comma. This function is depreciated and will "
            "be removed in the future release.",
            category=DeprecationWarning,
        )
        return add_comma(english_to_nepali(number))

    @staticmethod
    def convert(num):
        warnings.warn(
            message="NepaliNumber.convert has been moved to `english_to_nepali. "
            "This function is depreciated and will be removed in the future release.",
            category=DeprecationWarning,
        )
        return english_to_nepali(num)

    @staticmethod
    def revert(num):
        warnings.warn(
            message="NepaliNumber.revert has been moved to `nepali_to_english. "
            "This function is depreciated and will be removed in the future release.",
            category=DeprecationWarning,
        )
        return nepali_to_english(num)

    @staticmethod
    def add_comma(number):
        warnings.warn(
            message="NepaliNumber.add_comma has been moved to `add_comma. "
            "This function is depreciated and will be removed in the future release.",
            category=DeprecationWarning,
        )
        return add_comma(number)

    @staticmethod
    def add_comma_english(number):
        warnings.warn(
            message="NepaliNumber.add_comma_english has been moved to "
            "`add_comma_english. This function is depreciated and will "
            "be removed in the future release.",
            category=DeprecationWarning,
        )
        return add_comma_english(number)
