import datetime as pythonDateTime

from nepali.date_converter import converter as nepali_date_converter
from nepali.timezone import NepaliTimeZone, utc_now, to_nepali_timezone

from ._nepalimonth import nepalimonth


class formatter_class_mixin:
    """
    mixin for date time formatter.
    adds methods `strftime(format)`
    """

    def get_formatter_class(self):
        return self.__class__.init_formatter_class()

    @classmethod
    def init_formatter_class(cls):
        if not hasattr(cls, "__formatter_class__Cache"):
            from ._formatter import NepaliDateTimeFormatter

            cls.__formatter_class__Cache = NepaliDateTimeFormatter
        return cls.__formatter_class__Cache

    @classmethod
    def get_strptime_method(cls):
        if not hasattr(cls, "_strptime_method_CACHE"):
            from .parser import strptime

            cls._strptime_method_CACHE = strptime
        return cls._strptime_method_CACHE

    def strftime(self, format: str) -> str:
        return self.strftime_en(format)

    def strftime_en(self, format: str) -> str:
        NepaliDateTimeFormatter = self.get_formatter_class()
        formatter = NepaliDateTimeFormatter(self, devanagari=False)
        return formatter.get_str(format)

    def strftime_ne(self, format: str) -> str:
        NepaliDateTimeFormatter = self.get_formatter_class()
        formatter = NepaliDateTimeFormatter(self, devanagari=True)
        return formatter.get_str(format)


class nepalidate(formatter_class_mixin):
    def __init__(self, year, month, day) -> None:
        if isinstance(month, nepalimonth):
            month = month.value

        self.__year = year
        self.__month = month
        self.__day = day

        # converting to english date
        year_en, month_en, day_en = nepali_date_converter.nepali_to_english(
            year, month, day
        )
        self.__python_date = pythonDateTime.date(year_en, month_en, day_en)

    def __str__(self):
        return self.strftime_en("%Y-%m-%d")

    def __repr__(self):
        return f"<nepalidate> {self}"

    def to_datetime(self):
        return pythonDateTime.datetime.combine(
            self.__python_date, pythonDateTime.time(), tzinfo=NepaliTimeZone()
        )

    def to_date(self):
        return self.__python_date

    def to_nepalidatetime(self):
        return nepalidatetime.from_nepali_date(self)

    # operators overloading

    def __add__(self, other):
        """addition"""
        if type(other) == pythonDateTime.timedelta:
            # timedelta object
            return nepalidate.from_date(self.to_date() + other)
        return NotImplemented

    def __sub__(self, other):
        """subtraction"""
        if type(other) == self.__class__:
            # nepalidate object
            return self.to_date() - other.to_date()

        elif type(other) == pythonDateTime.date:
            # python date object
            return self.to_date() - other

        elif type(other) == pythonDateTime.timedelta:
            # timedelta object
            return nepalidate.from_date(self.to_date() - other)

        return NotImplemented

    def __lt__(self, other):
        """less than"""
        if type(other) == self.__class__:
            # nepalidatetime object
            return self.to_date() < other.to_date()

        elif type(other) == pythonDateTime.date:
            # python date object
            return self.to_date() < other

        return NotImplemented

    def __le__(self, other):
        """less than equal"""
        if type(other) == self.__class__:
            # nepalidate object
            return self.to_date() <= other.to_date()

        elif type(other) == pythonDateTime.date:
            # python date object
            return self.to_date() <= other

        return NotImplemented

    def __eq__(self, other):
        """equal"""
        if type(other) == self.__class__:
            # nepalidate object
            return self.to_date() == other.to_date()

        elif type(other) == pythonDateTime.date:
            # python date object
            return self.to_date() == other

        return False

    def __ne__(self, other):
        """not equal"""
        if type(other) == self.__class__:
            # nepalidate object
            return self.to_date() != other.to_date()

        elif type(other) == pythonDateTime.date:
            # python date object
            return self.to_date() != other

        return True

    def __gt__(self, other):
        """greater than"""
        if type(other) == self.__class__:
            # nepalidate object
            return self.to_date() > other.to_date()

        elif type(other) == pythonDateTime.date:
            # python date object
            return self.to_date() > other

        return NotImplemented

    def __ge__(self, other):
        """greater than equal"""
        if type(other) == self.__class__:
            # nepalidate object
            return self.to_date() >= other.to_date()

        elif type(other) == pythonDateTime.date:
            # python date object
            return self.to_date() >= other

        return NotImplemented

    # static methods
    @classmethod
    def strptime(cls, datetime_str, format):
        nepalidatetime_strptime = cls.get_strptime_method()
        return nepalidatetime_strptime(datetime_str, format=format).date()

    @staticmethod
    def now():
        return nepalidate.today()

    @staticmethod
    def today():
        return nepalidate.from_date(pythonDateTime.date.today())

    @staticmethod
    def from_datetime(datetime_object):
        return nepalidate.from_date(datetime_object.date())

    @staticmethod
    def from_date(date_object):
        npDate = nepalidate(
            *nepali_date_converter.english_to_nepali(
                date_object.year, date_object.month, date_object.day
            )
        )
        return npDate

    @staticmethod
    def from_nepalidatetime(datetime_object):
        return datetime_object.date()

    # property

    def weekday(self):
        """
        Sunday => 0, Saturday => 6
        """
        return (self.__python_date.weekday() + 1) % 7

    # nepali date properties
    @property
    def year(self):
        return self.__year

    @property
    def month(self):
        return self.__month

    @property
    def day(self):
        return self.__day


class nepalitime(pythonDateTime.time):
    def __repr__(self):
        return f"<nepalitime> {self}"

    # static methods

    @staticmethod
    def now():
        dt_now = pythonDateTime.datetime.now()
        return nepalitime(dt_now.hour, dt_now.minute, dt_now.second, dt_now.microsecond)


class nepalidatetime(formatter_class_mixin):
    """
    nepalidatetime
    """

    def __init__(self, year, month, day, hour=0, minute=0, second=0, microsecond=0):
        self.__np_date = nepalidate(year, month, day)
        self.__np_time = nepalitime(hour, minute, second, microsecond)

    def __str__(self):
        return f"{self.__np_date} {self.__np_time}"

    def __repr__(self):
        return f"<nepalidatetime> {self}"

    # operator overloading

    def __add__(self, other):
        """addition"""
        if type(other) == pythonDateTime.timedelta:
            # timedelta object
            return nepalidatetime.from_datetime(self.to_datetime() + other)

        return NotImplemented

    def __sub__(self, other):
        """subtraction"""
        if type(other) == self.__class__:
            # nepalidatetime object
            return self.to_datetime() - other.to_datetime()

        elif type(other) == pythonDateTime.datetime:
            # python datetime object
            return self.to_datetime() - to_nepali_timezone(other)

        elif type(other) == pythonDateTime.timedelta:
            # timedelta object
            return nepalidatetime.from_datetime(self.to_datetime() - other)

        return NotImplemented

    def __lt__(self, other):
        """less than"""
        if type(other) == self.__class__:
            # nepalidatetime object
            return self.to_datetime() < other.to_datetime()

        elif type(other) == pythonDateTime.datetime:
            # python datetime object
            return self.to_datetime() < to_nepali_timezone(other)

        return NotImplemented

    def __le__(self, other):
        """less than equal"""
        if type(other) == self.__class__:
            # nepalidatetime object
            return self.to_datetime() <= other.to_datetime()

        elif type(other) == pythonDateTime.datetime:
            # python datetime object
            return self.to_datetime() <= to_nepali_timezone(other)

        return NotImplemented

    def __eq__(self, other):
        """equal"""
        if type(other) == self.__class__:
            # nepalidatetime object
            return self.to_datetime() == other.to_datetime()

        elif type(other) == pythonDateTime.datetime:
            # python datetime object
            return self.to_datetime() == to_nepali_timezone(other)

        return False

    def __ne__(self, other):
        """not equal"""
        if type(other) == self.__class__:
            # nepalidatetime object
            return self.to_datetime() != other.to_datetime()

        elif type(other) == pythonDateTime.datetime:
            # python datetime object
            return self.to_datetime() != to_nepali_timezone(other)

        return True

    def __gt__(self, other):
        """greater than"""
        if type(other) == self.__class__:
            # nepalidatetime object
            return self.to_datetime() > other.to_datetime()

        elif type(other) == pythonDateTime.datetime:
            # python datetime object
            return self.to_datetime() > to_nepali_timezone(other)

        return NotImplemented

    def __ge__(self, other):
        """greater than equal"""
        if type(other) == self.__class__:
            # nepalidatetime object
            return self.to_datetime() >= other.to_datetime()

        elif type(other) == pythonDateTime.datetime:
            # python datetime object
            return self.to_datetime() >= to_nepali_timezone(other)

        return NotImplemented

    # object transformation

    def to_datetime(self):
        return pythonDateTime.datetime.combine(
            self.__np_date.to_date(), self.__np_time, tzinfo=NepaliTimeZone()
        )

    def to_date(self):
        return self.to_datetime().date()

    def date(self):
        return self.__np_date

    def time(self):
        return self.__np_time

    # static methods

    @classmethod
    def strptime(cls, datetime_str, format):
        nepalidatetime_strptime = cls.get_strptime_method()
        return nepalidatetime_strptime(datetime_str, format=format)

    @staticmethod
    def from_datetime(dt):
        dt = to_nepali_timezone(dt)
        nd = nepalidate.from_date(dt.date())
        return nepalidatetime(
            nd.year, nd.month, nd.day, dt.hour, dt.minute, dt.second, dt.microsecond
        )

    @staticmethod
    def from_date(date_object):
        nepali_date_object = nepalidate.from_date(date_object)
        return nepalidatetime.from_nepali_date(nepali_date_object)

    @staticmethod
    def from_nepali_date(nepali_date_object):
        return nepalidatetime(
            nepali_date_object.year, nepali_date_object.month, nepali_date_object.day
        )

    @staticmethod
    def now():
        return nepalidatetime.from_datetime(utc_now())

    # property

    @property
    def year(self):
        return self.__np_date.year

    @property
    def month(self):
        return self.__np_date.month

    @property
    def day(self):
        return self.__np_date.day

    def weekday(self):
        """
        Sunday => 0, Saturday => 6
        """
        return self.__np_date.weekday()

    @property
    def hour(self):
        return self.__np_time.hour

    @property
    def minute(self):
        return self.__np_time.minute

    @property
    def second(self):
        return self.__np_time.second
