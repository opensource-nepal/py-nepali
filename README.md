Nepali
======

  
Python package for processing every nepali stuffs

Requirements
------------
	Python >= 3


Instalation
-----------
	pip install nepali

DateConverter
-------------

**Converts English date to nepali date and nepali date to english date**
```python
from nepali.converter import DateConverter  
converter = DateConverter()
```

**Set Current date**  
```python
converter.setCurrentDate()
```

**Set English date**  
```python
converter.setEnglishDate(2018, 8, 18)
```

**Set Nepali date**  
```python
converter.setNepaliDate(2075, 6, 22)
```

**Nepali date details**  
```python
converter.toNepaliString() # returns nepali date string  
converter.npYear()  
converter.npMonth()  
converter.npDay()  
converter.weekDay()
```

**English date details**  
```python
converter.toEnglishString() # returns english date string  
converter.enYear()  
converter.enMonth()  
converter.enDay()  
converter.weekDay()
```

**Difference Days count**  
```python
converter.npDateDifference(2070, 10, 8) # returns no of days difference for nepali date.  
converter.enDateDifference(2017, 10, 8) # returns no of days difference for english date.
```