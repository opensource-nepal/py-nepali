import datetime
from typing import Any
from nepali.exceptions import InvalidNepaliDateTimeObjectException

from ._datetime import nepalidate, nepalidatetime


def to_nepalidatetime(datetime_object: Any) -> nepalidatetime:
    """
    Converts nepalidate, datetime.datetime, datetime.date to nepalidatetime.

    :param datetime_object: Object to be converted into nepalidatetime
    :return: nepalidatetime
    :raises InvalidNepaliDateTimeObjectException: If the input data is not a date time objects
    """
    if isinstance(datetime_object, nepalidatetime):
        return datetime_object
    elif isinstance(datetime_object, nepalidate):
        return nepalidatetime.from_nepali_date(datetime_object)
    elif isinstance(datetime_object, datetime.datetime):
        return nepalidatetime.from_datetime(datetime_object)
    elif isinstance(datetime_object, datetime.date):
        return nepalidatetime.from_date(datetime_object)
    raise InvalidNepaliDateTimeObjectException(
        "Argument must be instance of nepalidate or nepalidatetime or datetime.datetime or datetime.date"
    )


def to_nepalidate(datetime_object: Any) -> nepalidate:
    """
    Converts nepalidate, datetime.datetime, datetime.date to nepalidate.

    :param datetime_object: Object to be converted into nepalidate
    :return: nepalidate
    :raises InvalidNepaliDateTimeObjectException: If the input data is not a date time objects
    """
    return to_nepalidatetime(datetime_object).date()
