Nepali
======

  
Python package for processing every nepali stuffs

Requirements
------------
	Python >= 3


Installation
-----------
	pip install nepali


Features
--------
1. English to Nepali, Nepali to English date conversions with Nepali Timezone
2. Nepali Characters (Months, Days, etc)
3. Number to nepali numbers and nepali numbers to english.


NepaliDate
-------------

Represents nepali date, converts English date to nepali date and nepali date to english date

```python
from nepali.datetime import NepaliDate  
```

**Creating new object**
```python
# object with current date
np_date = NepaliDate(year, month, day)

# object with today's date
np_date = NepaliDate.today()
```

**Object from python's datetime.date**
```python
import datetime

date = datetime.date.today()
np_date = NepaliDate.from_date(date)
```

**Get python's datetime.date object**
```python
np_date.to_date()
```

**Get python's datetime.datetime object**
```python
np_date.to_datetime()
```


NepaliDateTime
-------------

Represents nepali date time

```python
from nepali.datetime import NepaliDateTime  
```

**Creating new object**
```python
# object with specific datetime
np_datetime = NepaliDateTime(year, month, day[, hour[, minute[, second]]]) # arguments must be nepali

# object with current datetime
np_datetime = NepaliDateTime.now()
```

**Object from python's datetime.datetime**
```python
import datetime

dt = datetime.datetime.now()
np_datetime = NepaliDateTime.from_datetime(dt)
```

**Get NepaliDate object**
```python
np_datetime.date()
```

**Get python's datetime.time object**
```python
np_datetime.time()
```

**Get python's datetime.datetime object**
```python
np_datetime.to_datetime()
```

**Date String Format**\
_Equivalent to python's datetime strftime format_
```python
npDateTime = NepaliDateTime.now()
print(npDateTime.strftime('%a %A %w %d %b %B %m %y %Y %H %I %p %M %S'))
print(npDateTime.strftime_en('%a %A %w %d %b %B %m %y %Y %H %I %p %M %S'))
```
```
बुध बुधबार ३ २६ मंसिर मंसिर ०८ ७५ २०७५ ११ ११ शुभप्रभात ०६ १३
Wed Wednesday 3 26 Mangsir Mangsir 08 75 2075 11 11 AM 06 13
```

**timedelta operations**
```python
ndt = NepaliDateTime.now()
print(ndt + datetime.timedelta(hours=5))
print(ndt - datetime.timedelta(hours=5))
```

HumanizeDateTime
-------------

HumanizeDate converts NepaliDateTime to nepali human readable form

```python
from nepali.datetime import HumanizeDateTime  
```

**Creating new object**
```python
# object from nepali datetime
ndt = NepaliDateTime.now()
humanize = HumanizeDateTime(ndt)

# object from python datetime
dt = datetime.datetime.now()
humanize = HumanizeDateTime(dt)
```

**Get string**
```python
humanize.to_str()
```

**Humanize with threshold**\
returns date in nepali characters if more than threshold(in seconds) else returns humanize form
```python
humanize = HumanizeDateTime(ndt, threshold=60) # 60 seconds
humanize.to_str()

# custom format after threshold
humanize = HumanizeDateTime(ndt, threshold=60, format='%Y-%m-%d') # 60 seconds
humanize.to_str()
```

For Django Template
-------------------

Add `'nepali'` to your `INSTALLED_APPS` setting.
```python
INSTALLED_APPS = [
	...
	'nepali',
	...
]
```

IN your Template

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
```

```python
{{ datetimeobj|nepalihumanize }}
```