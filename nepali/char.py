import warnings
from . import number

from .datetime._nepalimonth import nepalimonth

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
        return number.english_to_nepali(num)

    @staticmethod
    def day(day):
        days = [
            "आइतबार",
            "सोमबार",
            "मंगलबार",
            "बुधबार",
            "बिहीबार",
            "शुक्रबार",
            "शनिबार",
        ]
        return days[day - 1]

    @staticmethod
    def half_day(day):
        days = ["आइत", "सोम", "मंगल", "बुध", "बिही", "शुक्र", "शनि"]
        return days[day - 1]

    @staticmethod
    def month(month):
        warnings.warn(
            message="NepaliChar.month has been depreciated and will be removed in the future release.",
            category=DeprecationWarning,
        )
        return nepalimonth(month).name_ne


class EnglishChar:
    days = [
        "Sunday",
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
    ]
    days_half = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]

    @staticmethod
    def day(day):
        return EnglishChar.days[day - 1]

    @staticmethod
    def half_day(day):
        return EnglishChar.days_half[day - 1]

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
