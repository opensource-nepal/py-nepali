import pytz

from .timezone import NepaliTimeZone

def to_utc(datetime_obj):
	if datetime_obj.tzinfo:
		return datetime_obj.astimezone(pytz.timezone('UTC'))
	return datetime_obj.replace(tzinfo=pytz.timezone('UTC'))

def to_local(datetime_obj):
	if datetime_obj.tzinfo:
		return datetime_obj.astimezone(NepaliTimeZone())
	return datetime_obj.replace(tzinfo=NepaliTimeZone())