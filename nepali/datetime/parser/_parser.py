from nepali.datetime import nepalidatetime
from nepali.number import NepaliNumber as nepalinumber
from nepali.exceptions import InvalidDateTimeFormatException

__all__ = ["parse",]

def parse(datetimestr):
	"""
	parses nepali datetime
	eg. parse('2078-10-12') => <NepaliDateTime: 2078-10-12>
	"""
	
	# converting all nepali numbers to english
	datetimestr = nepalinumber.convert(datetimestr)

	# normal %Y-%m-%d format
	dates = datetimestr.split('-')
	if (
		len(dates[0]) == 4 and dates[0].isdigit() and 
		len(dates[1]) == 2 and dates[1].isdigit() and 
		len(dates[2]) == 2 and dates[2].isdigit() ):
		return nepalidatetime(year=int(dates[0]), month=int(dates[1]), day=int(dates[2]))
	
	raise InvalidDateTimeFormatException('Invalid format to parse nepali datetime.') 