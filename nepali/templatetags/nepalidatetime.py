from django import template

from nepali.datetime import NepaliDateTime, HumanizeDateTime
from nepali.utils import to_local, to_utc

register = template.Library()

@register.filter(name='nepalidate')
def nepalidate(datetime_obj, format):
	# if str(datetime_obj.tzinfo) == 'UTC':
	# 	return NepaliDateTime.from_datetime(datetime_obj, True).strftime(format)
	datetime_obj = to_local(datetime_obj)
	return NepaliDateTime.from_datetime(datetime_obj).strftime(format)

@register.filter(name='nepalidate_en')
def nepalidate_en(datetime_obj, format):
	# if str(datetime_obj.tzinfo) == 'UTC':
	# 	return NepaliDateTime.from_datetime(datetime_obj, True).strftime_en(format)
	datetime_obj = to_local(datetime_obj)
	return NepaliDateTime.from_datetime(datetime_obj).strftime_en(format)

@register.filter(name='nepalihumanize')
def nepalihumanize(datetime_obj, threshold=None, format=None):
	# if str(datetime_obj.tzinfo) == 'UTC':
	# 	return NepaliDateTime.from_datetime(datetime_obj, True).strftime(format)
	humanize = HumanizeDateTime(datetime_obj, threshold=threshold, format=format)
	return humanize.to_str()