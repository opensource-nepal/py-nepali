from django import template

from nepali.number import NepaliNumber

register = template.Library()

@register.filter(name='nepalinumber')
def nepalinumber(value):
	return NepaliNumber.convert(value)

@register.filter(name='nepalinumber_with_comma')
def nepalinumber_with_comma(value):
	return NepaliNumber.convert_and_add_comma(value)