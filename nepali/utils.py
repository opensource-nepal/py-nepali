import pytz

from .timezone import NepaliTimeZone, get_timezone

def to_utc(datetime_obj):
    if not datetime_obj.tzinfo:
        datetime_obj = datetime_obj.replace(tzinfo=get_timezone())
    return datetime_obj.astimezone(pytz.timezone('UTC'))

def to_local(datetime_obj):
    if not datetime_obj.tzinfo:
        datetime_obj = datetime_obj.replace(tzinfo=get_timezone())
    return datetime_obj.astimezone(NepaliTimeZone())