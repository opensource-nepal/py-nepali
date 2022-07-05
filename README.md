Nepali
======

Python package for converting nepali date time to python's datetime easily. Also supports parsing and timezone features.

Requirements
------------
	Python >= 3


Installation
-----------
	pip install nepali


Features
--------
1. Nepali datetime support
2. Parse nepali datetime
3. Nepali Characters (Months, Days, etc)
4. Number to nepali numbers and nepali numbers to english.


nepalidate
-------------

Represents nepali date, converts English date to nepali date and nepali date to english date

```python
from nepali.datetime import nepalidate  
```

**Creating new object**
```python
# object with current date
np_date = nepalidate(year, month, day)

# object with today's date
np_date = nepalidate.today()

# parse date
np_date = nepalidate.strptime('2078-01-12', format='%Y-%m-%d')
```

**Object from python's datetime.date**
```python
import datetime

date = datetime.date.today()
np_date = nepalidate.from_date(date)
```

**Get python's datetime.date object**
```python
np_date.to_date()
```

**Get python's datetime.datetime object**
```python
np_date.to_datetime()
```


nepalidatetime
-------------

Represents nepali date time

```python
from nepali.datetime import nepalidatetime  
```

**Creating new object**
```python
# object with specific datetime
np_datetime = nepalidatetime(year, month, day[, hour[, minute[, second]]]) # arguments must be nepali

# object with current datetime
np_datetime = nepalidatetime.now()

# parse datetime
np_datetime = nepalidatetime.strptime('2078-01-12 13:12', format='%Y-%m-%d %H:%M')
```

**Object from python's datetime.datetime**
```python
import datetime

dt = datetime.datetime.now()
np_datetime = nepalidatetime.from_datetime(dt)
```

**Get nepalidate object**
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
npDateTime = nepalidatetime.now()
print(npDateTime.strftime('%a %A %w %d %b %B %m %y %Y %H %I %p %M %S'))
print(npDateTime.strftime_en('%a %A %w %d %b %B %m %y %Y %H %I %p %M %S'))
```
```
बुध बुधबार ३ २६ मंसिर मंसिर ०८ ७५ २०७५ ११ ११ शुभप्रभात ०६ १३
Wed Wednesday 3 26 Mangsir Mangsir 08 75 2075 11 11 AM 06 13
```

**timedelta operations**
```python
ndt = nepalidatetime.now()
print(ndt + datetime.timedelta(hours=5))
print(ndt - datetime.timedelta(hours=5))
```

parse
---
Parses datetime from a string.

_parse uses very high cost method, so avoid this as much as you can._

```python
from nepali.datetime import parser as nepalidatetime_parser
ndt = nepalidatetime_parser.parse('29 Jestha, 2078, 1:30 PM')
```

nepalihumanize
-------------

nepalihumanize converts nepalidatetime to nepali human readable form

```python
from nepali.datetime import nepalihumanize  
```

**Creating new object**
```python
# object from nepali datetime
ndt = nepalidatetime.now()
humanize_str = nepalihumanize(ndt)

# object from python datetime
dt = datetime.datetime.now()
humanize_str = nepalihumanize(dt)
```


**Humanize with threshold**\
returns date in nepali characters if more than threshold(in seconds) else returns humanize form
```python
humanize_str = nepalihumanize(ndt, threshold=60) # 60 seconds

# custom format after threshold
humanize_str = nepalihumanize(ndt, threshold=60, format='%Y-%m-%d') # 60 seconds
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
{{ datetimeobj|nepalidate_en:"%Y-%m-%d" }}
```

```python
{{ datetimeobj|nepalihumanize }}
```
