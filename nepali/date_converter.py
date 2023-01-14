"""
This python file contains nepali date converter module.

USAGE:
y, m, d = nepali_date_converter.english_to_nepali(2023, 1, 15)
y, m, d = nepali_date_converter.nepali_to_english(2079, 10, 1)
"""


class NepaliDateConverter:
    """
    Nepali Date Converter

    All the functions here contains the method to convert english date to nepali and nepali date to english.
    """
    # Reference date for conversion is 2000/01/01 BS and 1943/4/14 AD

    EN_MONTHS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    EN_LEAP_YEAR_MONTHS = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  # Leap year months (Just 29 on Feb)
    
    # Nepali months data
    # [
    #   ((LIST_OF_MONTHS), TOTAL_DAYS_IN_YEAR),
    #   ...
    # ]
    #
    NP_MONTHS_DATA = [
        ((30, 32, 31, 32, 31, 30, 30, 30, 29, 30, 29, 31), 365),  # 2000 BS - 1944 AD
        ((31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30), 365),  # 2001 BS
        ((31, 31, 32, 32, 31, 30, 30, 29, 30, 29, 30, 30), 365),
        ((31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 31), 366),
        ((30, 32, 31, 32, 31, 30, 30, 30, 29, 30, 29, 31), 365),
        ((31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30), 365),
        ((31, 31, 32, 32, 31, 30, 30, 29, 30, 29, 30, 30), 365),
        ((31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 31), 366),
        ((31, 31, 31, 32, 31, 31, 29, 30, 30, 29, 29, 31), 365),
        ((31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30), 365),
        ((31, 31, 32, 32, 31, 30, 30, 29, 30, 29, 30, 30), 365),
        ((31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 31), 366),
        ((31, 31, 31, 32, 31, 31, 29, 30, 30, 29, 30, 30), 365),
        ((31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30), 365),
        ((31, 31, 32, 32, 31, 30, 30, 29, 30, 29, 30, 30), 365),
        ((31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 31), 366),
        ((31, 31, 31, 32, 31, 31, 29, 30, 30, 29, 30, 30), 365),
        ((31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30), 365),
        ((31, 32, 31, 32, 31, 30, 30, 29, 30, 29, 30, 30), 365),
        ((31, 32, 31, 32, 31, 30, 30, 30, 29, 30, 29, 31), 366),
        ((31, 31, 31, 32, 31, 31, 30, 29, 30, 29, 30, 30), 365),
        ((31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30), 365),
        ((31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 30), 365),
        ((31, 32, 31, 32, 31, 30, 30, 30, 29, 30, 29, 31), 366),
        ((31, 31, 31, 32, 31, 31, 30, 29, 30, 29, 30, 30), 365),
        ((31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30), 365),
        ((31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 31), 366),
        ((30, 32, 31, 32, 31, 30, 30, 30, 29, 30, 29, 31), 365),
        ((31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30), 365),
        ((31, 31, 32, 31, 32, 30, 30, 29, 30, 29, 30, 30), 365),
        ((31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 31), 366),
        ((30, 32, 31, 32, 31, 30, 30, 30, 29, 30, 29, 31), 365),
        ((31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30), 365),
        ((31, 31, 32, 32, 31, 30, 30, 29, 30, 29, 30, 30), 365),
        ((31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 31), 366),
        ((30, 32, 31, 32, 31, 31, 29, 30, 30, 29, 29, 31), 365),
        ((31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30), 365),
        ((31, 31, 32, 32, 31, 30, 30, 29, 30, 29, 30, 30), 365),
        ((31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 31), 366),
        ((31, 31, 31, 32, 31, 31, 29, 30, 30, 29, 30, 30), 365),
        ((31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30), 365),
        ((31, 31, 32, 32, 31, 30, 30, 29, 30, 29, 30, 30), 365),
        ((31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 31), 366),
        ((31, 31, 31, 32, 31, 31, 29, 30, 30, 29, 30, 30), 365),
        ((31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30), 365),
        ((31, 32, 31, 32, 31, 30, 30, 29, 30, 29, 30, 30), 365),
        ((31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 31), 366),
        ((31, 31, 31, 32, 31, 31, 30, 29, 30, 29, 30, 30), 365),
        ((31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30), 365),
        ((31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 30), 365),
        ((31, 32, 31, 32, 31, 30, 30, 30, 29, 30, 29, 31), 366),
        ((31, 31, 31, 32, 31, 31, 30, 29, 30, 29, 30, 30), 365),
        ((31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30), 365),
        ((31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 30), 365),
        ((31, 32, 31, 32, 31, 30, 30, 30, 29, 30, 29, 31), 366),
        ((31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30), 365),
        ((31, 31, 32, 31, 32, 30, 30, 29, 30, 29, 30, 30), 365),
        ((31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 31), 366),
        ((30, 32, 31, 32, 31, 30, 30, 30, 29, 30, 29, 31), 365),
        ((31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30), 365),
        ((31, 31, 32, 32, 31, 30, 30, 29, 30, 29, 30, 30), 365),
        ((31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 31), 366),
        ((30, 32, 31, 32, 31, 31, 29, 30, 29, 30, 29, 31), 365),
        ((31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30), 365),
        ((31, 31, 32, 32, 31, 30, 30, 29, 30, 29, 30, 30), 365),
        ((31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 31), 366),
        ((31, 31, 31, 32, 31, 31, 29, 30, 30, 29, 29, 31), 365),
        ((31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30), 365),
        ((31, 31, 32, 32, 31, 30, 30, 29, 30, 29, 30, 30), 365),
        ((31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 31), 366),
        ((31, 31, 31, 32, 31, 31, 29, 30, 30, 29, 30, 30), 365),
        ((31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30), 365),
        ((31, 32, 31, 32, 31, 30, 30, 29, 30, 29, 30, 30), 365),
        ((31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 31), 366),
        ((31, 31, 31, 32, 31, 31, 30, 29, 30, 29, 30, 30), 365),
        ((31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30), 365),
        ((31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 30), 365),
        ((31, 32, 31, 32, 31, 30, 30, 30, 29, 30, 29, 31), 366),
        ((31, 31, 31, 32, 31, 31, 30, 29, 30, 29, 30, 30), 365),
        ((31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30), 365),
        ((31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 30), 365),
        ((31, 31, 32, 32, 31, 30, 30, 30, 29, 30, 30, 30), 366),
        ((30, 32, 31, 32, 31, 30, 30, 30, 29, 30, 30, 30), 365),
        ((31, 31, 32, 31, 31, 30, 30, 30, 29, 30, 30, 30), 365),
        ((31, 31, 32, 31, 31, 30, 30, 30, 29, 30, 30, 30), 365),
        ((31, 32, 31, 32, 30, 31, 30, 30, 29, 30, 30, 30), 366),
        ((30, 32, 31, 32, 31, 30, 30, 30, 29, 30, 30, 30), 365),
        ((31, 31, 32, 31, 31, 31, 30, 30, 29, 30, 30, 30), 366),
        ((30, 31, 32, 32, 30, 31, 30, 30, 29, 30, 30, 30), 365),
        ((30, 32, 31, 32, 31, 30, 30, 30, 29, 30, 30, 30), 365),
        ((30, 32, 31, 32, 31, 30, 30, 30, 29, 30, 30, 30), 365),
        ((31, 31, 32, 31, 31, 31, 30, 30, 29, 30, 30, 30), 366),
        ((30, 31, 32, 32, 31, 30, 30, 30, 29, 30, 30, 30), 365),
        ((30, 32, 31, 32, 31, 30, 30, 30, 29, 30, 30, 30), 365),
        ((31, 31, 32, 31, 31, 30, 30, 30, 29, 30, 30, 30), 365),
        ((31, 31, 32, 31, 31, 31, 30, 29, 30, 30, 30, 30), 366),
        ((30, 31, 32, 32, 31, 30, 30, 29, 30, 29, 30, 30), 364),
        ((31, 32, 31, 32, 31, 30, 30, 30, 29, 30, 30, 30), 366),
        ((31, 31, 32, 31, 31, 31, 29, 30, 29, 30, 29, 31), 365),
        ((31, 31, 32, 31, 31, 31, 30, 29, 29, 30, 30, 30), 365),  # 2099 BS - 2042 AD
    ]

    # ENGLISH DATE CONVERSION

    def check_english_date(self, year, month, day):
        """checks if english date in within range 1944 - 2042"""
        if (year < 1944 or year > 2042):
            return False
        if (month < 1 or month > 12):
            return False
        if (day < 1 or day > 31):
            return False
        return True

    def _get_total_days_from_english_date(self, year, month, day):
        """counts and returns total days from the date 0000-01-01"""
        total_days = year * 365 + day
        for i in range(0, month-1):
            total_days = total_days + self.EN_MONTHS[i]

        # adding leap days (ie. leap year count)
        if (month <= 2):  # checking February month (where leap exists)
            year -= 1
        total_days += year//4 - year//100 + year//400

        return total_days

    def _get_days_between_english_dates(self, year1, month1, day1, year2, month2, day2):
        """returns difference days between to english dates"""
        return abs(
            self._get_total_days_from_english_date(year1, month1, day1)
            - self._get_total_days_from_english_date(year2, month2, day2)
        )

    # NEPALI DATE CONVERSION

    def check_nepali_date(self, year, month, day):
        """checks if nepali date is in range 2000-2098"""
        if (year < 2000 or year > 2098):
            return False
        if (month < 1 or month > 12):
            return False
        if (day < 1 or day > self.NP_MONTHS_DATA[year-2000][0][month-1]):
            return False
        return True

    def _get_total_days_from_nepali_date(self, year, month, day):
        """counts and returns total days from the nepali date 2000-01-01"""
        total = day - 1  # taking ref with Date's day 1, so -1

        # adding days of months of 2000
        year_index = year - 2000
        for i in range(0, month-1):
            total = total + self.NP_MONTHS_DATA[year_index][0][i]

        # adding days of year
        for i in range(0, year_index):
            total = total + self.NP_MONTHS_DATA[i][1]

        return total

    def _get_days_between_nepali_dates(self, year1, month1, day1, year2, month2, day2):
        """returns difference days between to english dates"""
        return abs(
            self._get_total_days_from_nepali_date(year1, month1, day1)
            - self._get_total_days_from_nepali_date(year2, month2, day2)
        )

    def _is_leap_year(self, year):
        """checks if the english year is leap year or not"""
        if (year % 4 == 0):
            if (year % 100 == 0):
                return (year % 400 == 0)
            return True
        return False

    # public methods

    def english_to_nepali(self, year, month, day):
        """
        Converts english date to nepali
        return year, month, day
        """
        # VALIDATION
        # checking if date is in range
        if not self.check_english_date(year, month, day):
            raise ValueError("Date out of range")

        # REFERENCE
        # Setting nepali reference to 2000/01/01 with english date 1943/04/14
        np_year = 2000
        np_month = 1
        np_day = 1

        # DIFFERENCE
        # calculating difference days from 1943/04/14
        difference = self._get_days_between_english_dates(year, month, day, 1943, 4, 14)

        # YEAR
        # Incrementing year until the difference remains less than 365
        year_data_index = 0
        while (difference >= self.NP_MONTHS_DATA[year_data_index][1]):
            difference = difference - self.NP_MONTHS_DATA[year_data_index][1]
            np_year += 1
            year_data_index += 1

        # MONTH
        # Incrementing month until the difference remains less than next nepali month days (mostly 31)
        i = 0
        while (difference >= self.NP_MONTHS_DATA[year_data_index][0][i]):
            difference = difference - self.NP_MONTHS_DATA[year_data_index][0][i]
            np_month += 1
            i += 1

        # DAY
        # Remaining difference is the day
        np_day += difference

        return np_year, np_month, np_day

    def nepali_to_english(self, year, month, day):
        """
        Converts english date to nepali
        return year, month, day
        """
        # VALIDATION
        # checking if date is in range
        if not self.check_nepali_date(year, month, day):
            raise ValueError("Date out of range")

        # REFERENCE
        # Setting english reference to 1944/01/01 with nepali date 2000/09/17
        en_year = 1944
        en_month = 1
        en_day = 1

        # DIFFERENCE
        # calculating difference days from 2000/09/17
        difference = self._get_days_between_nepali_dates(year, month, day, 2000, 9, 17)

        # YEAR
        # Incrementing year until the difference remains less than 365 (or 365)
        while (
            (difference >= 366 and self._is_leap_year(en_year))
            or (difference >= 365 and not (self._is_leap_year(en_year)))
        ):
            difference -= 366 if self._is_leap_year(en_year) else 365
            en_year += 1

        # MONTH
        # Incrementing month until the difference remains less than next english month (mostly 31)
        month_days = self.EN_LEAP_YEAR_MONTHS if self._is_leap_year(en_year) else self.EN_MONTHS
        i = 0
        while (difference >= month_days[i]):
            difference = difference - month_days[i]
            en_month += 1
            i += 1

        # DAY
        # Remaining difference is the day
        en_day += difference

        return en_year, en_month, en_day


converter = NepaliDateConverter()
