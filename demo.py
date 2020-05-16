import datetime
from nepali.datetime import NepaliDate, NepaliDateTime, NepaliDateTimeFormater
from nepali.char import NepaliChar
from nepali.number import NepaliNumber

d = datetime.date(2019, 1, 1)
dt = datetime.datetime(2019, 1, 1, 1, 1)

print(NepaliChar.number('123123123'))