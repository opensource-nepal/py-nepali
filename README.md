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

## Usage

### Date and Time

#### date_converter
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
print(np_year, np_month, np_date)
# 2079 10 24
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
print(en_year, en_month, en_date)
# 2023 2 7
```

#### nepalidate

#### nepalidatetime

#### nepalihumanize

#### timezone

#### parse

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
