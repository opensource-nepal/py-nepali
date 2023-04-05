import datetime as pythonDateTime
from nepali import number
from nepali.exceptions import (
    InvalidDateFormatException,
    InvalidNepaliDateTimeObjectException,
)

from ._datetime import nepalidate, nepalidatetime
from ._nepalimonth import nepalimonth
from ._nepaliweek import nepaliweek


class NepaliDateTimeFormatter:
    """
    NepaliDateTimeFormatter: formats nepali datetime to string ( using strftime )
    """

    # format according to python's datetime with class method
    format_map = {
        "a": "weekdayHalf",
        "A": "weekdayFull",
        "w": "weekdayNumber",
        "d": "day",
        "-d": "day_nonzero",
        "b": "monthFull",
        "B": "monthFull",
        "m": "monthNumber",
        "-m": "monthNumber_nonzero",
        "y": "yearHalf",
        "Y": "yearFull",
        "H": "hour24",
        "-H": "hour24_nonzero",
        "I": "hour12",
        "-I": "hour12_nonzero",
        "p": "ampm",
        "M": "minute",
        "-M": "minute_nonzero",
        "S": "second",
        "-S": "second_nonzero",
    }

    def __init__(self, datetime_object, devanagari=False):
        # TODO: Change variable npDateTime into snakecase: `np_date_time`
        if type(datetime_object) == nepalidatetime:
            self.npDateTime = datetime_object
        elif type(datetime_object) == nepalidate:
            self.npDateTime = datetime_object.to_nepalidatetime()
        elif type(datetime_object) == pythonDateTime.date:
            self.npDateTime = nepalidatetime.from_date(datetime_object)
        elif type(datetime_object) == pythonDateTime.datetime:
            self.npDateTime = nepalidatetime.from_datetime(datetime_object)
        else:
            raise InvalidNepaliDateTimeObjectException(
                "Argument must be instance of nepalidate or nepalidatetime or datetime.datetime or datetime.date"
            )

        self.devanagari = devanagari

    def __str__(self):
        return str(self.npDateTime)

    def get_str(self, format):
        """generates formatted string"""
        i, n = 0, len(format)
        time_str = []
        try:
            while i < n:
                ch = format[i]
                i += 1
                if ch == "%":
                    if i < n:
                        ch = format[i]

                        if ch == "%":
                            # for % character
                            time_str.append("%")

                        elif ch == "-":
                            # special mid characters eg. "-" for non zero padded values
                            special_ch = ch
                            if i + 1 < n:
                                i += 1
                                ch = format[i]
                                time_str.append(
                                    getattr(self, self.get_format_map(special_ch + ch))
                                )
                        else:
                            # mapping % forwarded character
                            time_str.append(getattr(self, self.get_format_map(ch)))
                        i += 1
                else:
                    time_str.append(ch)
        except InvalidDateFormatException as e:
            raise e
        except Exception:
            raise Exception("Unable to convert NepaliDateTime to str")
        time_str = "".join(time_str)

        return time_str

    def get_format_map(self, ch: str) -> str:
        if ch not in self.format_map:
            raise InvalidDateFormatException("Invalid Date format %{}".format(ch))
        return self.format_map[ch]

    @property
    def weekdayHalf(self):
        """
        %a
        """
        week = nepaliweek(self.npDateTime.weekday())
        if not self.devanagari:
            return week.abbr
        return week.abbr_ne

    @property
    def weekdayFull(self):
        """
        %A
        """
        week = nepaliweek(self.npDateTime.weekday())
        if not self.devanagari:
            return week.name
        return week.name_ne

    @property
    def weekdayNumber(self):
        """
        %w
        """
        if not self.devanagari:
            return str(self.npDateTime.weekday())
        return number.english_to_nepali(self.npDateTime.weekday())

    @property
    def day(self):
        """
        %d
        """
        day = str(self.npDateTime.day)
        if len(day) < 2:
            day = "0" + day
        if not self.devanagari:
            return str(day)
        return number.english_to_nepali(day)

    @property
    def day_nonzero(self):
        """
        %-D
        """
        day = str(self.npDateTime.day)
        if not self.devanagari:
            return str(day)
        return number.english_to_nepali(day)

    @property
    def monthFull(self):
        """
        %B or %b
        """
        month = nepalimonth(self.npDateTime.month)
        if not self.devanagari:
            return month.name
        return month.name_ne

    @property
    def monthNumber(self):
        """
        %m
        """
        month = str(self.npDateTime.month)
        if len(month) < 2:
            month = "0" + month
        if not self.devanagari:
            return str(month)
        return number.english_to_nepali(month)

    @property
    def monthNumber_nonzero(self):
        """
        %-m
        """
        month = str(self.npDateTime.month)
        if not self.devanagari:
            return str(month)
        return number.english_to_nepali(month)

    @property
    def yearHalf(self):
        """
        %y
        """
        if not self.devanagari:
            return str(self.npDateTime.year)[2:]
        return number.english_to_nepali(str(self.npDateTime.year)[2:])

    @property
    def yearFull(self):
        """
        %Y
        """
        if not self.devanagari:
            return str(self.npDateTime.year)
        return number.english_to_nepali(self.npDateTime.year)

    @property
    def hour24(self):
        """
        %H
        """
        hour = str(self.npDateTime.hour)
        if len(hour) < 2:
            hour = "0" + hour
        if not self.devanagari:
            return str(hour)
        return number.english_to_nepali(hour)

    @property
    def hour24_nonzero(self):
        """
        %-H
        """
        hour = self.npDateTime.hour
        if not self.devanagari:
            return str(hour)
        return number.english_to_nepali(hour)

    @property
    def hour12(self):
        """
        %I
        """
        hour = self.npDateTime.hour
        if hour > 12:
            hour = hour - 12
        if hour == 0:
            hour = 12
        hour = str(hour)
        if len(hour) < 2:
            hour = "0" + hour

        if not self.devanagari:
            return str(hour)
        return number.english_to_nepali(hour)

    @property
    def hour12_nonzero(self):
        """
        %-I
        """
        hour = self.npDateTime.hour
        if hour > 12:
            hour = hour - 12
        if hour == 0:
            hour = 12
        hour = str(hour)
        if not self.devanagari:
            return str(hour)
        return number.english_to_nepali(hour)

    @property
    def ampm(self):
        """
        %p
        """
        if not self.devanagari:
            ampm = "AM"
            if self.npDateTime.hour > 12:
                ampm = "PM"
            return str(ampm)

        ampm = ""
        if self.npDateTime.hour < 12:
            ampm = "शुभप्रभात"
        elif self.npDateTime.hour >= 12 and self.npDateTime.hour < 18:
            ampm = "मध्यान्ह"
        else:
            ampm = "अपरान्ह"
        return str(ampm)

    @property
    def minute(self):
        """
        %M
        """
        minute = str(self.npDateTime.minute)
        if len(minute) < 2:
            minute = "0" + minute
        if not self.devanagari:
            return str(minute)
        return number.english_to_nepali(minute)

    @property
    def minute_nonzero(self):
        """
        %-M
        """
        minute = str(self.npDateTime.minute)
        if not self.devanagari:
            return str(minute)
        return number.english_to_nepali(minute)

    @property
    def second(self):
        """
        %S
        """
        second = str(self.npDateTime.second)
        if len(second) < 2:
            second = "0" + second
        if not self.devanagari:
            return str(second)
        return number.english_to_nepali(second)

    @property
    def second_nonzero(self):
        """
        %-S
        """
        second = str(self.npDateTime.second)
        if not self.devanagari:
            return str(second)
        return number.english_to_nepali(second)
