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

**Represents nepali date, converts English date to nepali date and nepali date to english date**
```python
from nepali.dates import NepaliDate  
np_date = NepaliDate()
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