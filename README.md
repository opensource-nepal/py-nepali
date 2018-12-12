Nepali
======

  
Python package for processing every nepali stuffs

Requirements
------------
	Python >= 3


Installation
-----------
	pip install nepali

NepaliDate
-------------

Represents nepali date, converts English date to nepali date and nepali date to english date

```python
from nepali.datetime import NepaliDate  
```

**Creating new object**
```python
# object with current date
np_date = NepaliDate()

# object with today's date
np_date = NepaliDate.today()
```

**Object from python's datetime.date**
```python
import datetime

date = datetime.date.today()
np_date = NepaliDate.from_date(date)
```

**Set Current date**  
```python
np_date.setCurrentDate()
```

**Set English date**  
```python
np_date.setEnDate(2018, 8, 18)
```

**Set Nepali date**  
```python
np_date.setNpDate(2075, 6, 22)
```

**Nepali date details**  
```python
np_date.toNpString() # returns nepali date string  
np_date.npYear()  
np_date.npMonth()  
np_date.npDay()  
np_date.weekDay()
```

**English date details**  
```python
np_date.toEnString() # returns english date string  
np_date.enYear()  
np_date.enMonth()  
np_date.enDay()  
np_date.weekDay()
```

**Difference Days count**  
```python
np_date.npDateDifference(2070, 10, 8) # returns no of days difference for nepali date.  
np_date.enDateDifference(2017, 10, 8) # returns no of days difference for english date.
```

**Get python's datetime.date**
```python
np_date.to_date()
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
**Date String Format**
```python
npDateTime = NepaliDateTime.now()
print(npDateTime.strftime('%a %A %w %d %b %B %m %y %Y %H %I %p %M %S'))
print(npDateTime.strftime_en('%a %A %w %d %b %B %m %y %Y %H %I %p %M %S'))
```
`बुध बुधबार ३ २६ मंसिर मंसिर ०८ ७५ २०७५ ११ ११ शुभप्रभात ०६ १३
Wed Wednesday 3 26 Mangsir Mangsir 08 75 2075 11 11 AM 06 13`

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

**Humanize with threshold**
returns date in nepali characters if more than threshold(in seconds) else returns humanize form
```python
humanize = HumanizeDateTime(ndt, threshold=60) # 60 seconds
humanize.to_str()

# custom format after threshold
humanize = HumanizeDateTime(ndt, threshold=60, format='%Y-%m-%d') # 60 seconds
humanize.to_str()
```
