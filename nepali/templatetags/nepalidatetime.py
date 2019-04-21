from django import template
from django.utils import timezone

from nepali.datetime import nepalidatetime, nepalihumanize as humanize
from nepali.utils import to_local, to_utc

register = template.Library()

@register.filter(name='nepalidate')
def nepalidate(datetime_obj, format):
	datetime_obj = to_local(datetime_obj)
	return nepalidatetime.from_datetime(datetime_obj).strftime(format)

@register.filter(name='nepalidate_en')
def nepalidate_en(datetime_obj, format):
	datetime_obj = to_local(datetime_obj)
	return nepalidatetime.from_datetime(datetime_obj).strftime_en(format)

@register.filter(name='nepalihumanize')
def nepalihumanize(datetime_obj, threshold=None, format=None):
	""" templatetag to humanize nepalidatetime """
	return humanize(datetime_obj, threshold=threshold, format=format)
	
@register.simple_tag
def nepalinow(format="%B %d, %Y, %A"):
	""" templatetag to display current datetime in nepali format """
	datetime_obj = to_local(timezone.now())
	return nepalidatetime.from_datetime(datetime_obj).strftime(format)
