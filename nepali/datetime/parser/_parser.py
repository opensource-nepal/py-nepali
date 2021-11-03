from nepali.exceptions import InvalidDateTimeFormatException, FormatNotMatchException

from.validators import validate

__all__ = ["strptime", "parse",]

_standard_datetime_format_CACHE = None

def strptime(datetime_str, format):
	'''
	Parses nepalidatetime str with the corresponding format.
	returns nepalidatetime object.
	'''
	nepalidatetime_object = validate(datetime_str, format)
	if nepalidatetime_object == None:
		raise FormatNotMatchException('Datetime string did not match with the given format.') 
	return nepalidatetime_object

def _get_standard_formats():
	global _standard_datetime_format_CACHE
	if _standard_datetime_format_CACHE != None:
		return _standard_datetime_format_CACHE

	STANDARD_DATE_FORMAT = [
		'%Y-%m-%d',
		'%d-%m-%Y',
		'%Y %m %d',
		'%Y %B %d',
		'%d %B %Y',
		'%d %B, %Y',
		'%B %d, %Y',
		'%Y/%m/%d',
		'%d/%m/%Y',
	]

	STANDARD_TIME_FORMAT = [
		'%H:%M',
		'%I:%M %p',
		'%I %p',
		'%I%p',
		'%H:%M:%S',
		'%H:%M:%S:%f',
	]

	_standard_datetime_format_CACHE = STANDARD_DATE_FORMAT.copy()
	for time_format in STANDARD_TIME_FORMAT:
		for date_format in STANDARD_DATE_FORMAT:
			_standard_datetime_format_CACHE += ['{} {}'.format(date_format, time_format)]
			_standard_datetime_format_CACHE += ['{}, {}'.format(date_format, time_format)]
	return _standard_datetime_format_CACHE


def parse(datetime_str):
	"""
	parses nepali datetime
	eg. parse('2078-10-12') => <NepaliDateTime: 2078-10-12>
	"""
	standard_formats = _get_standard_formats()
	nepalidatetime_object = None
	for format in standard_formats:
		nepalidatetime_object = validate(datetime_str, format=format)
		if nepalidatetime_object != None:
			return nepalidatetime_object

	raise InvalidDateTimeFormatException('Invalid format to parse nepali datetime.') 