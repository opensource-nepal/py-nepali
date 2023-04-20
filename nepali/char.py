import warnings

from . import number
from .datetime._nepalimonth import nepalimonth
from .datetime._nepaliweek import nepaliweek

MONTHS_MAP = {
    "बैशाख": "Baishakh",
    "जेठ": "Jestha",
    "असार": "Ashad",
    "साउन": "Sharwan",
    "भदौ": "Bhadra",
    "असोज": "Ashwin",
    "कात्तिक": "Kartik",
    "मंसिर": "Mangsir",
    "पुस": "Poush",
    "माघ": "Magh",
    "फागुन": "Falgun",
    "चैत": "Chaitra",
}

DAYS_MAP = {
    "आइतबार": "Sunday",
    "सोमबार": "Monday",
    "मंगलबार": "Tuesday",
    "बुधबार": "Wednesday",
    "बिहीबार": "Thursday",
    "शुक्रबार": "Friday",
    "शनिबार": "Saturday",
}

HALF_DAYS_MAP = {
    "आइत": "Sun",
    "सोम": "Mon",
    "मंगल": "Tue",
    "बुध": "Wed",
    "बिही": "Thu",
    "शुक्र": "Fri",
    "शनि": "Sat",
}

AM_PM_MAP = {
    "शुभप्रभात": "AM",
    "मध्यान्ह": "PM",
    "अपरान्ह": "PM",
}


class NepaliChar:
    @staticmethod
    def number(num):
        warnings.warn(
            message="NepaliChar.number has been depreciated and will be removed in the future release.",
            category=DeprecationWarning,
        )
        return number.english_to_nepali(num)

    @staticmethod
    def day(day):
        warnings.warn(
            message="NepaliChar.day has been depreciated and will be removed in the future release.",
            category=DeprecationWarning,
        )
        return nepaliweek(day).name_ne

    @staticmethod
    def half_day(day):
        warnings.warn(
            message="NepaliChar.half_day has been depreciated and will be removed in the future release.",
            category=DeprecationWarning,
        )
        return nepaliweek(day).abbr_ne

    @staticmethod
    def month(month):
        warnings.warn(
            message="NepaliChar.month has been depreciated and will be removed in the future release.",
            category=DeprecationWarning,
        )
        return nepalimonth(month).name_ne


class EnglishChar:
    @staticmethod
    def day(day):
        warnings.warn(
            message="EnglishChar.day has been depreciated and will be removed in the future release.",
            category=DeprecationWarning,
        )
        return nepaliweek(day).name

    @staticmethod
    def half_day(day):
        warnings.warn(
            message="EnglishChar.half_day has been depreciated and will be removed in the future release.",
            category=DeprecationWarning,
        )
        return nepaliweek(day).abbr

    @staticmethod
    def month(month):
        warnings.warn(
            message="EnglishChar.month has been depreciated and will be removed in the future release.",
            category=DeprecationWarning,
        )
        return nepalimonth(month).name


def nepali_to_english_text(text):
    # TODO: optimization

    # replacing months
    for k, v in MONTHS_MAP.items():
        text = text.replace(k, v)

    # replacing days
    for k, v in DAYS_MAP.items():
        text = text.replace(k, v)

    # replacing half days
    for k, v in HALF_DAYS_MAP.items():
        text = text.replace(k, v)

    for k, v in AM_PM_MAP.items():
        text = text.replace(k, v)

    return number.nepali_to_english(text)
