# nepali

[![PyPI version](https://badge.fury.io/py/nepali.svg)](https://badge.fury.io/py/nepali)
[![CI status](https://github.com/opensource-nepal/py-nepali/actions/workflows/python-package.yml/badge.svg?branch=master)](https://github.com/opensource-nepal/py-nepali/actions)
[![Downloads](https://img.shields.io/pypi/dm/nepali.svg?maxAge=180)](https://pypi.org/project/nepali/)
[![codecov](https://codecov.io/gh/opensource-nepal/py-nepali/branch/master/graph/badge.svg?token=PTUHYWCJ4I)](https://codecov.io/gh/opensource-nepal/py-nepali)

`nepali` is a python package containing features that will be useful for Nepali projects.

The major feature of this package is nepalidatetime, which is compatible with python's datetime feature. It helps nepali date to english, parsing nepali datetime, nepali timezone, and timedelta support in nepali datetime.

## Example

```python
import datetime
from nepali import phone_number
from nepali.datetime import nepalidate, parser

nepali_datetime = parser.parse('2079-02-15')
# 2079-02-15 00:00:00

# convert
date = datetime.date(2017, 3, 15)
nepali_date = nepalidate.from_date(date)
# 2073-12-02

phone_number.parse("+977-9845217789")
# {
# 	'type': 	'Mobile',
#	'number':	'9845217789',
#	'operator': <Operator: Nepal Telecom>
# }
```

## Requirements

    Python >= 3

## Installation

    pip install nepali

## Date and Time

### date_converter

Date converter module converts english date to nepali and nepali date to english. It doesn't contain any extra functionality.

**Convert English date to Nepali Date**

```python
from nepali.date_converter import converter

np_year, np_month, np_date = converter.english_to_nepali(en_year, en_month, en_date)
```

Example

```python
from nepali.date_converter import converter

np_year, np_month, np_date = converter.english_to_nepali(2023, 2, 7)
print(np_year, np_month, np_date) # 2079 10 24
```

**Convert English date to Nepali Date**

```python
from nepali.date_converter import converter

en_year, en_month, en_date = converter.english_to_nepali(np_year, np_month, np_date)
```

Example

```python
from nepali.date_converter import converter

en_year, en_month, en_date = converter.nepali_to_english(2079, 10, 24)
print(en_year, en_month, en_date) # 2023 2 7
```

### nepalidate

**Creating a new nepalidate object**

```python
from nepali.datetime import nepalidate

# nepalidate object with year, month, day
np_date = nepalidate(year, month, day)

# nepalidate object with today's date
np_date = nepalidate.today()

# parse nepali date
np_date = nepalidate.strptime('2078-01-18', format='%Y-%m-%d')
```

**Getting nepalidate object from python datetime**

```python
# from date object
np_date = nepalidate.from_date(date_obj)

# from datetime object
np_date = nepalidate.from_datetime(datetime_obj)
```

**Attributes and Methods**

```python
np_date.year					# 2078 (year)
np_date.month					# 1 (month)
np_date.day						# 18 (day)

np_date.to_date() 				# datetime.date object
np_date.to_datetime()			# datetime.datetime object
np_date.to_nepalidatetime()		# nepalidatetime object

np_date.strftime("%Y-%m-%d")	# २०७८-०१-१८
np_date.strftime_en("%Y-%m-%d")	# 2078-01-18

np_date.weekday()				# Sunday => 0, Monday => 1, ..., Saturday => 6
```

### nepalidatetime

**Creating a new nepalidatetime object**

```python
from nepali.datetime import nepalidatetime

# nepalidate object with year, month, day, hour, minute, second
np_datetime = nepalidatetime(year, month, day[, hour[, minute[, second]]])

# nepalidate object with current date and time
np_datetime = nepalidate.now()
np_datetime = nepalidate.today()

# parse nepali datetime
np_datetime = nepalidatetime.strptime('2078-01-12 13:12', format='%Y-%m-%d %H:%M')
```

**Getting nepalidatetime object from python datetime**

```python
# from date object
np_datetime = nepalidatetime.from_date(date_obj)

# from datetime object
np_datetime = nepalidatetime.from_datetime(datetime_obj)
```

**Getting nepalidatetime object from nepalidate**

```python
np_datetime = nepalidatetime.from_nepalidate(nepali_date)
```

**Attributes and Methods**

```python
np_date.year							# 2078 (year)
np_date.month							# 1 (month)
np_date.day								# 18 (day)
np_date.hour							# 23 (hour)
np_date.minute							# 59 (minute)
np_date.second							# 59 (day)

np_date.to_date() 						# datetime.date object
np_date.to_datetime()					# datetime.datetime object
np_date.to_nepalidate()					# nepalidatetime object
np_date.to_time()						# nepalitime object (datetime.time compatible)

np_date.strftime("%Y-%m-%d %H:%M")		# २०७८-०१-१८ २३:५९
np_date.strftime_en("%Y-%m-%d %H:%M")	# 2078-01-18 23:59

np_date.weekday()						# Sunday => 0, Monday => 1, ..., Saturday => 6
```

**Timedelta support**

```python
# timedelta addition and subtraction
np_datetime - datetime.timedelta(days=3)	# returns nepalidatetime

# comparison between two dates
np_datetime1 - np_datetime2					# returns timedelta object
np_datetime1 < np_datetime2					# returns bool (True/False)
np_datetime1 >= datetime.datetime.now()		# returns bool (True/False)
...
```

### nepalihumanize

### timezone

### parse

### strftime() and strptime() Format Codes

| Directive | Meaning                                                   | Example                        |
| --------- | --------------------------------------------------------- | ------------------------------ |
| `%A`      | Weekday as locale’s abbreviated name.                     | Sun, Mon, …, Sat (आइत, सोम, …) |
| `%A`      | Weekday as locale’s full name.                            | Sunday, Monday, …, Saturday    |
| `%d`      | Day of the month as a zero-padded decimal number.         | 01, 02, …, 31                  |
| `%-d`     | Day of the month as a decimal number.                     | 1, 2, …, 31                    |
| `%B`      | Month as locale’s full name.                              | Baishak, Jestha, …, Chaitra    |
| `%m`      | Month as a zero-padded decimal number.                    | 01, 02, …, 12                  |
| `%-m`     | Month as a decimal number.                                | 1, 2, …, 12                    |
| `%y`      | Year without century as a zero-padded decimal number.     | 00, 01, …, 99                  |
| `%Y`      | Year with century as a decimal number.                    | 2001, 2078, 2079, …, 2099      |
| `%H`      | Hour (24-hour clock) as a zero-padded decimal number.     | 00, 01, …, 23                  |
| `%-H`     | Hour (24-hour clock) as a decimal number.                 | 0, 1, 2, …, 23                 |
| `%I`      | Hour (12-hour clock) as a zero-padded decimal number.     | 01, 02, …, 12                  |
| `%-I`     | Hour (12-hour clock) as a decimal number.                 | 1, 2, …, 12                    |
| `%p`      | Locale’s equivalent of either AM or PM.                   | AM, PM (en_US)                 |
| `%M`      | Minute as a zero-padded decimal number.                   | 00, 01, …, 59                  |
| `%-M`     | Minute as a decimal number.                               | 0, 1, 2, …, 59                 |
| `%S`      | Second as a zero-padded decimal number.                   | 00, 01, …, 59                  |
| `%-S`     | Second as a decimal number.                               | 0, 1, 2, …, 59                 |
| `%f`      | Microsecond as a decimal number, zero-padded to 6 digits. | 000000, 000001, …, 999999      |
| `%%`      | A literal `'%'` character.                                | %                              |

### Numbers

### Phone Number

### Others

## For Django Template

Add `'nepali'` to your `INSTALLED_APPS` setting.

```python
INSTALLED_APPS = [
    ...
    'nepali',
    ...
]
```

In your Template

```python
{% load nepalidatetime %}
```

```python
{% nepalinow %}
```

```python
{% nepalinow '%Y-%m-%d' %}
```

```python
{{ datetimeobj|nepalidate:"%Y-%m-%d" }}
{{ datetimeobj|nepalidate_en:"%Y-%m-%d" }}
```

```python
{{ datetimeobj|nepalihumanize }}
```
