import pytz
import datetime

from .timezone import NepaliTimeZone, get_timezone
from .exceptions import InvalidNepaliDateTimeObjectException

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

def to_nepali_datetime(datetime_object):
	""" converts nepalidate, datetime.datetime, datetime.date to nepalidatetime """
	from .datetime import NepaliDate, NepaliDateTime

	if type(datetime_object) == NepaliDateTime:
		return datetime_object
	elif type(datetime_object) == NepaliDate:
		return NepaliDateTime.from_nepali_date(datetime_object)
	elif type(datetime_object) == datetime.datetime:
		return NepaliDateTime.from_datetime(datetime_object)
	elif type(datetime_object) == datetime.date:
		return NepaliDateTime.from_date(datetime_object)
	elif datetime_object == '' or datetime_object == None:
		return None

	raise InvalidNepaliDateTimeObjectException('Argument must be instance of NepaliDate or NepaliDateTime or datetime.datetime or datetime.date') 