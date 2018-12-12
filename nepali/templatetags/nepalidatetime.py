from django import template

from nepali.datetime import NepaliDateTime

register = template.Library()

@register.filter(name='nepalidate')
def nepalidate(datetime_obj, format):
	return NepaliDateTime.from_datetime(datetime_obj).strftime(format)

@register.filter(name='nepalidate_en')
def nepalidate_en(datetime_obj, format):
	return NepaliDateTime.from_datetime(datetime_obj).strftime_en(format)