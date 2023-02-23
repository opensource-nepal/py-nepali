from django import template

from nepali.number import nepali_to_english, convert_and_add_comma

register = template.Library()


@register.filter(name="nepalinumber")
def nepalinumber(value):
    return nepali_to_english(value)


@register.filter(name="nepalinumber_with_comma")
def nepalinumber_with_comma(value):
    return convert_and_add_comma(value)
