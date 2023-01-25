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
