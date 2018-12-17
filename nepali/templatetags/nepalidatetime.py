from django import template

from nepali.datetime import NepaliDateTime

register = template.Library()

@register.filter(name='nepalidate')
def nepalidate(datetime_obj, format):
	if str(datetime_obj.tzinfo) == 'UTC':
		return NepaliDateTime.from_datetime(datetime_obj, True).strftime(format)
	return NepaliDateTime.from_datetime(datetime_obj).strftime(format)

@register.filter(name='nepalidate_en')
def nepalidate_en(datetime_obj, format):
	if str(datetime_obj.tzinfo) == 'UTC':
		return NepaliDateTime.from_datetime(datetime_obj, True).strftime_en(format)
	return NepaliDateTime.from_datetime(datetime_obj).strftime_en(format)