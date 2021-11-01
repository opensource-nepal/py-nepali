import datetime
import pytz
import warnings

from .timezone import NepaliTimeZone, get_timezone
from .exceptions import InvalidNepaliDateTimeObjectException

def to_utc_timezone(datetime_obj):
	if type(datetime_obj) != datetime.datetime:
		# None datetime object
		return datetime_obj

	if (not hasattr(datetime_obj, 'tzinfo')) or (not datetime_obj.tzinfo):
		datetime_obj = datetime_obj.replace(tzinfo=get_timezone())
	return datetime_obj.astimezone(pytz.timezone('UTC'))

def to_utc(datetime_obj):
	warnings.warn(
		message="to_utc is depreciated and no longer be available in version >= 1.0.0, use to_utc_timezone instead.", 
		category=DeprecationWarning
	)
	return to_utc_timezone(datetime_obj)

def to_nepali_timezone(datetime_obj):
	if type(datetime_obj) != datetime.datetime:
		return datetime_obj

	if (not hasattr(datetime_obj, 'tzinfo')) or (not datetime_obj.tzinfo):
		datetime_obj = datetime_obj.replace(tzinfo=get_timezone())
	return datetime_obj.astimezone(NepaliTimeZone())

def to_local(datetime_obj):
	warnings.warn(
		message="to_local is depreciated and no longer be available in version >= 1.0.0, use to_nepali_timezone instead.", 
		category=DeprecationWarning
	)
	return to_nepali_timezone(datetime_obj)

def to_nepalidatetime(datetime_object):
	"""
	Converts nepalidate, datetime.datetime, datetime.date to nepalidatetime. 
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
	elif datetime_object == '' or datetime_object == None:
		return None
	raise InvalidNepaliDateTimeObjectException('Argument must be instance of nepalidate or nepalidatetime or datetime.datetime or datetime.date') 

def to_nepali_datetime(datetime_object):
	warnings.warn(
		message="to_nepali_datetime is depreciated and no longer be available in version >= 1.0.0, use to_nepalidatetime instead.", 
		category=DeprecationWarning
	)
	return to_nepalidatetime(datetime_object)

def to_nepalidate(datetime_object):
	nepalidatetime_obj = to_nepalidatetime(datetime_object)
	if nepalidatetime_obj != None:
		return nepalidatetime_obj.date()
	return 