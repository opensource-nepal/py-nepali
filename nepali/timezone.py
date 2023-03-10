import datetime
from typing import Union


class NepaliTimeZone(datetime.tzinfo):
    """
    NepaliTimeZone: "Asia/Kathmandu", +05:45
    """

    def utcoffset(self, dt):
        return self.dst(dt) + datetime.timedelta(hours=5, minutes=45)

    def dst(self, dt):
        return datetime.timedelta(0)

    def tzname(self, dt):
        return "Asia/Kathmandu"

    def __str__(self):
        return "Asia/Kathmandu"

    def __repr__(self):
        return "Asia/Kathmandu"

    def __eq__(self, o: object) -> bool:
        return isinstance(o, self.__class__)


def get_timezone() -> Union[datetime.tzinfo, None]:
    """
    Returns current device's timezone.
    Timezone of the machine.
    """
    return datetime.datetime.now(datetime.timezone.utc).astimezone().tzinfo


def now() -> datetime.datetime:
    """Returns current datetime object of the device"""
    return datetime.datetime.now(get_timezone())


def utc_now() -> datetime.datetime:
    """Returns UTC time datetime object"""
    return datetime.datetime.now(datetime.timezone.utc)


def to_utc_timezone(datetime_obj: datetime.datetime) -> datetime.datetime:
    """Changes the timezone of the given datetime object to UTC."""
    if type(datetime_obj) != datetime.datetime:
        # Not a datetime object
        return datetime_obj

    if not hasattr(datetime_obj, "tzinfo") or not datetime_obj.tzinfo:
        datetime_obj = datetime_obj.replace(tzinfo=get_timezone())
    return datetime_obj.astimezone(datetime.timezone.utc)


def to_nepali_timezone(datetime_obj: datetime.datetime) -> datetime.datetime:
    """Changes the timezone of the given datetime object to NepaliTimeZone."""
    if type(datetime_obj) != datetime.datetime:
        # Not a datetime object
        return datetime_obj

    if not hasattr(datetime_obj, "tzinfo") or not datetime_obj.tzinfo:
        datetime_obj = datetime_obj.replace(tzinfo=get_timezone())
    return datetime_obj.astimezone(NepaliTimeZone())
