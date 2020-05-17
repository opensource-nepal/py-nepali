from django import template
from django.utils import timezone

from nepali.datetime import nepalidatetime, nepalihumanize as humanize
from nepali.utils import to_local, to_utc, to_nepali_datetime

register = template.Library()

@register.filter(name='nepalidate')
def nepalidate(datetime_obj, format="%B %d, %Y, %A"):
	nepali_datetime_obj = to_nepali_datetime(datetime_obj)
	if nepali_datetime_obj == None: return None
	return nepali_datetime_obj.strftime(format)

@register.filter(name='nepalidate_en')
def nepalidate_en(datetime_obj, format="%B %d, %Y, %A"):
	nepali_datetime_obj = to_nepali_datetime(datetime_obj)
	if nepali_datetime_obj == None: return None
	return nepali_datetime_obj.strftime_en(format)

@register.filter(name='nepalihumanize')
def nepalihumanize(datetime_obj, threshold=None, format=None):
	""" templatetag to humanize nepalidatetime """
	nepali_datetime_obj = to_nepali_datetime(datetime_obj)
	if nepali_datetime_obj == None: return None
	return humanize(nepali_datetime_obj, threshold=threshold, format=format)
	
@register.simple_tag
def nepalinow(format="%B %d, %Y, %A"):
	""" templatetag to display current datetime in nepali format """
	return to_nepali_datetime(timezone.now()).strftime(format)
