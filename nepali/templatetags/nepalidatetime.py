"""
This module contains django templatetags for nepali date and time.
"""
import datetime
import warnings
from typing import Optional, Union

from django import template
from django.utils import timezone

from nepali.datetime import nepalidate as _nepalidate
from nepali.datetime import nepalidatetime as _nepalidatetime
from nepali.datetime import nepalihumanize as humanize
from nepali.exceptions import InvalidNepaliDateTimeObjectException
from nepali.utils import to_nepalidatetime

_DEFAULT_DATE_FORMAT = "%B %d, %Y, %A"
DEPRECIATION_WARNING_MESSAGE = (
    "The templatetag 'nepalidatetime' has been depreciated "
    "and will be removed in the future release. "
    "Please use `django-nepali` package."
)
_datetime = Union[datetime.date, datetime.datetime, _nepalidate, _nepalidatetime]
register = template.Library()


@register.filter(name="nepalidate")
def nepalidate(
    datetime_obj: _datetime, format: str = _DEFAULT_DATE_FORMAT
) -> Union[str, None]:
    """
    Renders the datetime object into nepali datetime format in 'en-US' locale (English).

    Usage:
    ```
    {{ datetime_obj|nepalidate }}
    {{ datetime_obj|nepalidate:"%Y-%m-%d" }}
    ```

    :param datetime_obj: Datetime object
    :param format: Output format, defaults to "%B %d, %Y, %A"
    :returns: Nepali datetime format in 'en-US' locale
    """
    warnings.warn(
        message=DEPRECIATION_WARNING_MESSAGE,
        category=DeprecationWarning,
    )
    return nepalidate_en(datetime_obj, format=format)


@register.filter(name="nepalidate_en")
def nepalidate_en(
    datetime_obj: _datetime, format: str = _DEFAULT_DATE_FORMAT
) -> Union[str, None]:
    """
    Renders the datetime object into nepali datetime format in 'en-US' locale (English).

    Usage:
    ```
    {{ datetime_obj|nepalidate_en }}
    {{ datetime_obj|nepalidate_en:"%Y-%m-%d" }}
    ```

    :param datetime_obj: Datetime object
    :param format: Output format, defaults to "%B %d, %Y, %A"
    :returns: Nepali datetime format in 'en-US' locale
    """
    warnings.warn(
        message=DEPRECIATION_WARNING_MESSAGE,
        category=DeprecationWarning,
    )
    try:
        nepali_datetime_obj = to_nepalidatetime(datetime_obj)
        return nepali_datetime_obj.strftime_en(format)
    except InvalidNepaliDateTimeObjectException:
        return None


@register.filter(name="nepalidate_ne")
def nepalidate_ne(
    datetime_obj: _datetime, format: str = _DEFAULT_DATE_FORMAT
) -> Union[str, None]:
    """
    Renders the datetime object into nepali datetime format in 'ne' locale (Nepali).

    Usage:
    ```
    {{ datetime_obj|nepalidate_ne }}
    {{ datetime_obj|nepalidate_ne:"%Y-%m-%d" }}
    ```

    :param datetime_obj: Datetime object
    :param format: Output format, defaults to "%B %d, %Y, %A"
    :returns: Nepali datetime format in 'ne' locale
    """
    warnings.warn(
        message=DEPRECIATION_WARNING_MESSAGE,
        category=DeprecationWarning,
    )
    try:
        nepali_datetime_obj = to_nepalidatetime(datetime_obj)
        return nepali_datetime_obj.strftime_ne(format)
    except InvalidNepaliDateTimeObjectException:
        return None


@register.filter(name="nepalihumanize")
def nepalihumanize(
    datetime_obj: _datetime,
    threshold: Optional[int] = None,
    format: Optional[str] = None,
) -> Union[str, None]:
    """
    Renders the datetime object to a human readable form for 'ne' locale (Nepali).

    Usage:
    ```
    {{ datetime_obj|nepalihumanize }}
    ```

    :param datetime_obj: Datetime object
    :param threshold: Threshold in seconds that determines when to render
        the datetime object in the standard datetime format, optional
    :param format: Output format if threshold exceeded, optional
    :returns: Datetime object in human readable form
    """
    warnings.warn(
        message=DEPRECIATION_WARNING_MESSAGE,
        category=DeprecationWarning,
    )
    try:
        nepali_datetime_obj = to_nepalidatetime(datetime_obj)
        return humanize(nepali_datetime_obj, threshold=threshold, format=format)
    except InvalidNepaliDateTimeObjectException:
        return None


@register.simple_tag
def nepalinow(format: str = _DEFAULT_DATE_FORMAT) -> str:
    """
    Renders the current nepali datetime in 'en-US' locale (English).

    Usage:
    ```
    {% nepalinow %}
    {% nepalinow '%Y-%m-%d' %}
    ```

    :param datetime_obj: Datetime object
    :param format: Output format, defaults to "%B %d, %Y, %A"
    :returns: Current nepali datetime
    """
    warnings.warn(
        message=DEPRECIATION_WARNING_MESSAGE,
        category=DeprecationWarning,
    )
    return nepalinow_en(format)


@register.simple_tag
def nepalinow_en(format: str = _DEFAULT_DATE_FORMAT) -> str:
    """
    Renders the current nepali datetime in 'en-US' locale (English).

    Usage:
    ```
    {% nepalinow_en %}
    {% nepalinow_en '%Y-%m-%d' %}
    ```

    :param datetime_obj: Datetime object
    :param format: Output format, defaults to "%B %d, %Y, %A"
    :returns: Current nepali datetime
    """
    warnings.warn(
        message=DEPRECIATION_WARNING_MESSAGE,
        category=DeprecationWarning,
    )
    return to_nepalidatetime(timezone.now()).strftime(format)


@register.simple_tag
def nepalinow_ne(format: str = _DEFAULT_DATE_FORMAT) -> str:
    """
    Renders the current nepali datetime in 'ne' locale (Nepali).

    Usage:
    ```
    {% nepalinow_ne %}
    {% nepalinow_ne '%Y-%m-%d' %}
    ```

    :param datetime_obj: Datetime object
    :param format: Output format, defaults to "%B %d, %Y, %A"
    :returns: Current nepali datetime
    """
    warnings.warn(
        message=DEPRECIATION_WARNING_MESSAGE,
        category=DeprecationWarning,
    )
    return to_nepalidatetime(timezone.now()).strftime_ne(format)
