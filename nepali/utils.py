import pytz
import datetime

from .timezone import NepaliTimeZone, get_timezone

def to_utc(datetime_obj):
	if type(datetime_obj) != datetime.datetime:
		# None datetime object
		return datetime_obj

	if (not hasattr(datetime_obj, 'tzinfo')) or (not datetime_obj.tzinfo):
		datetime_obj = datetime_obj.replace(tzinfo=get_timezone())
	return datetime_obj.astimezone(pytz.timezone('UTC'))

def to_local(datetime_obj):
	if type(datetime_obj) != datetime.datetime:
		return datetime_obj

	if (not hasattr(datetime_obj, 'tzinfo')) or (not datetime_obj.tzinfo):
		datetime_obj = datetime_obj.replace(tzinfo=get_timezone())
	return datetime_obj.astimezone(NepaliTimeZone())