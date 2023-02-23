import datetime
import pytz
from typing import Any

from .timezone import NepaliTimeZone, get_timezone
from .exceptions import InvalidNepaliDateTimeObjectException


# TODO: Move timezone methods to timezone.py

def to_utc_timezone(datetime_obj: datetime.datetime) -> datetime.datetime:
    """Changes the timezone of the given datetime object to UTC."""
    if type(datetime_obj) != datetime.datetime:
        # None datetime object
        return datetime_obj

    if (not hasattr(datetime_obj, "tzinfo")) or (not datetime_obj.tzinfo):
        datetime_obj = datetime_obj.replace(tzinfo=get_timezone())
    return datetime_obj.astimezone(pytz.timezone("UTC"))


def to_nepali_timezone(datetime_obj: datetime.datetime) -> datetime.datetime:
    """Changes the timezone of the given datetime object to NepaliTimeZone."""
    if type(datetime_obj) != datetime.datetime:
        return datetime_obj

    if (not hasattr(datetime_obj, "tzinfo")) or (not datetime_obj.tzinfo):
        datetime_obj = datetime_obj.replace(tzinfo=get_timezone())
    return datetime_obj.astimezone(NepaliTimeZone())


# TODO: Move inside the datetime

def to_nepalidatetime(datetime_object: Any) -> Any:  # TODO: return data type is nepalidatetime
    """
    Converts nepalidate, datetime.datetime, datetime.date to nepalidatetime.

    :return: nepalidatetime
    """
    from .datetime import nepalidate, nepalidatetime

    if type(datetime_object) == nepalidatetime:
        return datetime_object
    elif type(datetime_object) == nepalidate:
        return nepalidatetime.from_nepali_date(datetime_object)
    elif type(datetime_object) == datetime.datetime:
        return nepalidatetime.from_datetime(datetime_object)
    elif type(datetime_object) == datetime.date:
        return nepalidatetime.from_date(datetime_object)
    elif datetime_object == "" or datetime_object == None:
        return None
    raise InvalidNepaliDateTimeObjectException(
        "Argument must be instance of nepalidate or nepalidatetime or datetime.datetime or datetime.date"
    )


def to_nepalidate(datetime_object: Any) -> Any:  # TODO: return data type is nepalidate
    """
    Converts nepalidate, datetime.datetime, datetime.date to nepalidate.

    :return: nepalidate
    """
    nepalidatetime_obj = to_nepalidatetime(datetime_object)
    if nepalidatetime_obj != None:
        return nepalidatetime_obj.date()
    return
