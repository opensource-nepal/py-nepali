"""
validates parsing
"""
import re
from typing import Optional, Tuple

from nepali.char import nepali_to_english_text
from nepali.constants import NEPALI_MONTHS_EN, WEEKS_ABBR_EN, WEEKS_EN
from nepali.datetime import nepalidatetime, nepalimonth, nepaliweek

__nepali_time_re__CACHE = None


class NepaliTimeRE(dict):
    def __init__(self):
        """Create keys/values.
        Order of execution is important for dependency reasons.
        """
        base = super()
        base.__init__(
            {
                # The " [1-9]" part of the regex is to make %c from ANSI C work
                "d": r"(?P<d>3[0-2]|[1-2]\d|0[1-9]|[1-9]| [1-9])",
                "-d": r"(?P<d>3[0-2]|[1-2]\d|0[1-9]|[1-9]| [1-9])",  # same as "d"
                "f": r"(?P<f>[0-9]{1,6})",
                "H": r"(?P<H>2[0-3]|[0-1]\d|\d)",
                "-H": r"(?P<H>2[0-3]|[0-1]\d|\d)",
                "I": r"(?P<I>1[0-2]|0[1-9]|[1-9])",
                "-I": r"(?P<I>1[0-2]|0[1-9]|[1-9])",
                "G": r"(?P<G>\d\d\d\d)",
                "j": r"(?P<j>36[0-6]|3[0-5]\d|[1-2]\d\d|0[1-9]\d|00[1-9]|[1-9]\d|0[1-9]|[1-9])",
                "m": r"(?P<m>1[0-2]|0[1-9]|[1-9])",
                "-m": r"(?P<m>1[0-2]|0[1-9]|[1-9])",  # same as "m"
                "M": r"(?P<M>[0-5]\d|\d)",
                "-M": r"(?P<M>[0-5]\d|\d)",  # same as "M"
                "S": r"(?P<S>6[0-1]|[0-5]\d|\d)",
                "-S": r"(?P<S>6[0-1]|[0-5]\d|\d)",  # same as "S"
                "w": r"(?P<w>[0-6])",
                "y": r"(?P<y>\d\d)",
                "Y": r"(?P<Y>\d\d\d\d)",
                "z": r"(?P<z>[+-]\d\d:?[0-5]\d(:?[0-5]\d(\.\d{1,6})?)?|(?-i:Z))",
                "A": self.__seqToRE(WEEKS_EN, "A"),
                "a": self.__seqToRE(WEEKS_ABBR_EN, "a"),
                "B": self.__seqToRE(NEPALI_MONTHS_EN, "B"),
                "b": self.__seqToRE(NEPALI_MONTHS_EN, "b"),
                "p": self.__seqToRE(
                    (
                        "AM",
                        "PM",
                    ),
                    "p",
                ),
                "%": "%",
            }
        )

    def __seqToRE(self, to_convert, directive):
        """Convert a list to a regex string for matching a directive.
        Want possible matching values to be from longest to shortest.  This
        prevents the possibility of a match occurring for a value that also
        a substring of a larger value that should have matched (e.g., 'abc'
        matching when 'abcdef' should have been the match).
        """
        to_convert = sorted(to_convert, key=len, reverse=True)
        for value in to_convert:
            if value != "":
                break
        else:
            return ""
        regex = "|".join(re.escape(stuff) for stuff in to_convert)
        regex = f"(?P<{directive}>{regex}"
        return f"{regex})"

    def pattern(self, date_format):
        """
        Handle conversion from format directives to regex.
        """
        processed_format = ""
        regex_chars = re.compile(r"([\\.^$*+?\(\){}\[\]|])")
        date_format = regex_chars.sub(r"\\\1", date_format)
        whitespace_replacement = re.compile(r"\s+")
        date_format = whitespace_replacement.sub(r"\\s+", date_format)
        while "%" in date_format:
            directive_index = date_format.index("%") + 1
            index_increment = 1

            if date_format[directive_index] == "-":
                index_increment = 2

            if (
                date_format[directive_index : directive_index + index_increment]
                not in self
            ):
                return None

            processed_format = "%s%s%s" % (
                processed_format,
                date_format[: directive_index - 1],
                self[date_format[directive_index : directive_index + index_increment]],
            )
            date_format = date_format[directive_index + index_increment :]
        return f"^{processed_format}{date_format}$"

    def compile(self, date_format):
        """Return a compiled re object for the format string."""
        return re.compile(self.pattern(date_format), re.IGNORECASE)


def get_nepali_time_re_object():
    global __nepali_time_re__CACHE
    if __nepali_time_re__CACHE is None:
        __nepali_time_re__CACHE = NepaliTimeRE()
    return __nepali_time_re__CACHE


def extract(datetime_str, format):
    """
    Extracts year, month, day, hour, minute, etc from the given format.

    eg.
    USAGE: extract("2078-01-12", format="%Y-%m-%d")
    INPUT:
    datetime_str="2078-01-12"
    format="%Y-%m-%d"

    OUTPUT:
    {
        "Y": 2078,
        "m": 1,
        "d": 12,
    }
    """

    # converting datetime_str to english if any exists
    datetime_str = nepali_to_english_text(datetime_str)

    re_compiled_format = get_nepali_time_re_object().compile(format)
    match = re_compiled_format.match(datetime_str)
    if match is None:
        return {}
    return match.groupdict()


def __convert_12_hour_to_24_hour(hour: int, am_pm: str) -> int:
    """Converts hours from 12-hour format to 24-hour format.

    :param hour: The hour value to convert.
    :param am_pm: Either "am" or "pm"; signifies whether the hour is in am or pm.

    :returns: The value of `hour` converted to 24-hour format.
    """
    am_pm = am_pm.lower()
    if am_pm == "am" and hour == 12:
        return 0
    elif am_pm == "pm" and hour != 12:
        return hour + 12
    return hour


def __calculate_year(data: dict) -> Optional[int]:
    """Calculates the year value from given data.

    :param data: The dictionary of the format:
                    {
                        "Y": 2078,
                        "b": "Mangsir",
                        "d": 12,
                        ...
                    }

    :returns: The year value of given date data.
    """
    if "y" in data:
        return int(data["y"]) + 2000
    elif "Y" in data:
        return int(data["Y"])
    return None


def __calculate_month(data: dict) -> nepalimonth:
    """Calculates the month value from given data.

    :param data: The dictionary of the format:
                    {
                        "Y": 2078,
                        "b": "Mangsir",
                        "d": 12,
                        ...
                    }

    :returns: The month value of given date data.
    """
    if "m" in data:
        return nepalimonth(int(data["m"]))
    elif "b" in data:
        return nepalimonth(data["b"])
    elif "B" in data:
        return nepalimonth(data["B"])
    return nepalimonth(1)


def __calculate_day(data: dict) -> int:
    """Calculates the day value from given data.

    :param data: The dictionary of the format:
                    {
                        "Y": 2078,
                        "b": "Mangsir",
                        "d": 12,
                        ...
                    }

    :returns: The day value of given date data.
    """
    if "d" in data:
        return int(data["d"])
    return 1


def __calculate_hour_minute_seconds(data: dict) -> Tuple[int, int, int, int]:
    """Calculates hour, minutes, seconds and microseconds from given data.

    :param data: The dictionary of the format:
                    {
                        "Y": 2078,
                        "b": "Mangsir",
                        "d": 12,
                        "H": 12,
                        "M": 12,
                        "S": 12,
                        "f": 12,
                        ...
                    }

    :returns: A tuple of hour, minute, seconds and microseconds.
    """
    hour = minute = second = fraction = 0
    if "H" in data:
        hour = int(data["H"])
    elif "I" in data:
        am_pm = data.get("p", "").lower() or "am"
        hour = __convert_12_hour_to_24_hour(hour=int(data["I"]), am_pm=am_pm)

    if "M" in data:
        minute = int(data["M"])

    if "S" in data:
        second = int(data["S"])

    if "f" in data:
        s = data["f"]
        # Pad to always return microseconds.
        s += "0" * (6 - len(s))
        fraction = int(s)

    return hour, minute, second, fraction


def __calculate_weekday(data: dict) -> Optional[nepaliweek]:
    """Calculates the weekday of the date given in data.

    :param data: The data that describes the date.

    :returns: The weekday value; 0 for Sunday, 1 for Monday, etc.
    """
    if "a" in data:
        return nepaliweek(data["a"])
    elif "A" in data:
        return nepaliweek(data["A"])
    elif "w" in data:
        return nepaliweek((int(data["w"]) - 1) % 7)
    return None


def transform(data: dict):
    """
    transforms different format data to uniform data

    eg.
    INPUT:
    data = {
        "Y": 2078,
        "b": "Mangsir",
        "d": 12,
        ...
    }

    OUTPUT:
    {
        "year": 2078,
        "month": 8,
        "day": 12,
        ...
    }
    """

    year = __calculate_year(data)
    month = __calculate_month(data)
    day = __calculate_day(data)
    hour, minute, second, fraction = __calculate_hour_minute_seconds(data)
    weekday = __calculate_weekday(data)

    return {
        "year": year,
        "month": month,
        "day": day,
        "hour": hour,
        "minute": minute,
        "second": second,
        "microsecond": fraction,
        "weekday": weekday,
    }


def validate(datetime_str, format):
    """
    validates datetime_str with the format
    Perform step by step test for fast performance. The steps are:
    -
    -
    returns False if validation failed
    returns nepalidatetime object if validation success.
    """

    # 1. validate if format is correct.
    if get_nepali_time_re_object().pattern(format) is None:
        # regex pattern generation failed
        return None

    # 2. validate if parse result if not empty
    parsed_result = extract(datetime_str, format)
    if parsed_result.get("Y") is None and parsed_result.get("y") is None:
        # compilation failed or year included
        return None

    # 3. validate if transformation
    transformed_data = transform(parsed_result)
    if transformed_data.get("year") is None:
        # could not transform data, not getting year
        return None

    # 4. create the datetime object
    return nepalidatetime(
        year=transformed_data["year"],
        month=transformed_data["month"],
        day=transformed_data["day"],
        hour=transformed_data["hour"],
        minute=transformed_data["minute"],
        second=transformed_data["second"],
        microsecond=transformed_data["microsecond"],
    )
