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
    NP_INITIAL_YEAR = 2000
    REFERENCE_EN_DATE = (1943, 4, 14)

    # Nepali months data
    # [
    #   ((LIST_OF_MONTHS), TOTAL_DAYS_IN_YEAR),
    #   ...
    # ]
    #
    NP_MONTHS_DATA = [
        (
            (30, 32, 31, 32, 31, 30, 30, 30, 29, 30, 29, 31),
            365,
        ),  # 2000 BS - 1943/1944 AD
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
        (
            (31, 31, 32, 31, 31, 31, 30, 29, 29, 30, 30, 30),
            365,
        ),  # 2099 BS - 2042/2043 AD
    ]

    # english month constant data (will never change)
    EN_MONTHS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    EN_LEAP_YEAR_MONTHS = [
        31,
        29,
        31,
        30,
        31,
        30,
        31,
        31,
        30,
        31,
        30,
        31,
    ]  # Leap year months (Just 29 on Feb)

    @classmethod
    def en_min_year(cls):
        return cls.REFERENCE_EN_DATE[0] + 1

    @classmethod
    def en_max_year(cls):
        return cls.REFERENCE_EN_DATE[0] + len(cls.NP_MONTHS_DATA) - 1

    @classmethod
    def np_min_year(cls):
        return cls.NP_INITIAL_YEAR

    # utility methods

    @classmethod
    def np_max_year(cls):
        return cls.NP_INITIAL_YEAR + len(cls.NP_MONTHS_DATA) - 1

    def _is_leap_year(self, year):
        """checks if the english year is leap year or not"""
        if year % 4 == 0:
            if year % 100 == 0:
                return year % 400 == 0
            return True
        return False

    def _get_en_months(self, year):
        return self.EN_LEAP_YEAR_MONTHS if self._is_leap_year(year) else self.EN_MONTHS

    #
    # ENGLISH DATE CONVERSION

    def check_english_date(self, year, month, day):
        if year < self.en_min_year() or year > self.en_max_year():
            return False
        if month < 1 or month > 12:
            return False
        if day < 1 or day > 31:
            return False
        return True

    def _get_total_days_from_english_date(self, year, month, day):
        """counts and returns total days from the date 0000-01-01"""
        total_days = year * 365 + day
        for i in range(0, month - 1):
            total_days = total_days + self.EN_MONTHS[i]

        # adding leap days (ie. leap year count)
        if month <= 2:  # checking February month (where leap exists)
            year -= 1
        total_days += year // 4 - year // 100 + year // 400

        return total_days

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
        np_year, np_month, np_day = self.NP_INITIAL_YEAR, 1, 1

        # DIFFERENCE
        # calculating days count from the reference date
        difference = abs(
            self._get_total_days_from_english_date(year, month, day)
            - self._get_total_days_from_english_date(*self.REFERENCE_EN_DATE)
        )

        # YEAR
        # Incrementing year until the difference remains less than 365
        year_data_index = 0
        while difference >= self.NP_MONTHS_DATA[year_data_index][1]:
            difference -= self.NP_MONTHS_DATA[year_data_index][1]
            np_year += 1
            year_data_index += 1

        # MONTH
        # Incrementing month until the difference remains less than next nepali month days (mostly 31)
        i = 0
        while difference >= self.NP_MONTHS_DATA[year_data_index][0][i]:
            difference -= self.NP_MONTHS_DATA[year_data_index][0][i]
            np_month += 1
            i += 1

        # DAY
        # Remaining difference is the day
        np_day += difference

        return np_year, np_month, np_day

    #
    # NEPALI DATE CONVERSION

    def check_nepali_date(self, year, month, day):
        if year < self.np_min_year() or year > self.np_max_year():
            return False
        if month < 1 or month > 12:
            return False
        if (
            day < 1
            or day > self.NP_MONTHS_DATA[year - self.NP_INITIAL_YEAR][0][month - 1]
        ):
            return False
        return True

    def _get_total_days_from_nepali_date(self, year, month, day):
        """counts and returns total days from the nepali initial date"""
        total_days = day - 1  # taking ref with Date's day 1, so -1

        # adding days of months of initial year
        year_index = year - self.NP_INITIAL_YEAR
        for i in range(0, month - 1):
            total_days = total_days + self.NP_MONTHS_DATA[year_index][0][i]

        # adding days of year
        for i in range(0, year_index):
            total_days = total_days + self.NP_MONTHS_DATA[i][1]

        return total_days

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
        # For absolute reference, moving date to Jan 1
        # Eg. ref: 1943/4/14 => 1943/01/01
        en_year, en_month, en_day = self.REFERENCE_EN_DATE[0], 1, 1
        # calculating difference from the adjusted reference (eg. 1943/4/14 - 1943/01/01)
        ref_year_months = self._get_en_months(en_year)
        reference_diff = (
            sum(ref_year_months[0 : self.REFERENCE_EN_DATE[1] - 1])
            + self.REFERENCE_EN_DATE[2]
            - 1  # day - 1
        )

        # DIFFERENCE
        # calculating days count from the reference date
        difference = abs(
            self._get_total_days_from_nepali_date(
                year, month, day
            )  # returns total days from initial date (nepali)
            + reference_diff
        )

        # YEAR
        # Incrementing year until the difference remains less than 365 (or 365)
        while (difference >= 366 and self._is_leap_year(en_year)) or (
            difference >= 365 and not (self._is_leap_year(en_year))
        ):
            difference -= 366 if self._is_leap_year(en_year) else 365
            en_year += 1

        # MONTH
        # Incrementing month until the difference remains less than next english month (mostly 31)
        month_days = self._get_en_months(en_year)
        i = 0
        while difference >= month_days[i]:
            difference -= month_days[i]
            en_month += 1
            i += 1

        # DAY
        # Remaining difference is the day
        en_day += difference

        return en_year, en_month, en_day


converter = NepaliDateConverter()
