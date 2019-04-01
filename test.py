import datetime
from nepali.datetime import *


# NepaliDate
npDate = NepaliDate.today()
print(1, repr(npDate))

npDate = NepaliDate(2075, 8, 20)
print(2, repr(npDate))

# NepaliTime
npTime = NepaliTime.now()
print(3, repr(npTime))

# NepaliDateTime

npDateTime = NepaliDateTime.now()
print(5, repr(npDateTime))

dt = datetime.datetime.now()
npDateTime = NepaliDateTime.from_datetime(dt)
print(6, repr(npDateTime))

npDateTime = NepaliDateTime(2075, 8, 20)
print(7, repr(npDateTime))


# NepaliDatetime timedelta operations
ndt1 = NepaliDateTime.now()
ndt2 = NepaliDateTime(2075, 12, 18)
td = datetime.timedelta(hours=1)
dt1 = datetime.datetime.now()

print(8, repr(ndt1 + td))

print(9, repr(ndt1 - td))
print(10, repr(ndt1 - ndt2))
print(11, repr(ndt2 - dt1))

print(12, repr(ndt1 < ndt2))
print(13, repr(ndt1 < dt1))

print(14, ndt1 <= ndt2)
print(15, ndt1 <= dt1)

print(16, ndt1 > ndt2)
print(17, ndt1 > dt1)

print(18, ndt1 >= ndt2)
print(19, ndt1 >= dt1)

print(20, ndt1 == ndt2)
print(21, ndt1 == dt1)

print(22, ndt1 != ndt2)
print(24, ndt1 != dt1)


# NepaliDateTime strftime()
npDateTime = NepaliDateTime.now()
print(25, npDateTime.strftime('%a %A %w %d %b %B %m %y %Y %H %I %p %M %S'))
print(26, npDateTime.strftime_en('%a %A %w %d %b %B %m %y %Y %H %I %p %M %S'))


# Humanize datetime
humanize = HumanizeDateTime(datetime.datetime.now())
print(27, humanize.to_str())

ndt = NepaliDateTime(2075, 8, 2)
humanize = HumanizeDateTime(ndt)
print(28, humanize.to_str())

ndt = NepaliDateTime(2075, 8, 2)
humanize = HumanizeDateTime(ndt, threshold=0)
print(29, humanize.to_str())

ndt = NepaliDateTime(2075, 8, 2)
humanize = HumanizeDateTime(ndt, threshold=0, format='%a %A %w %d %b %B %m %y %Y')
print(30, humanize.to_str())
