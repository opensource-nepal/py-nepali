#
#
#	Author : Ajesh Sen Thapa
#	Website: www.ajesh.com.np
#
#

import time
from datetime import datetime, timedelta

from .chars import NepaliChar

class NepaliDate:
	
	def __init__(self):

		self.__enMonths = [31, 28, 31, 30, 31, 30,31, 31, 30, 31, 30, 31]
		self.enLeapMonths = [31, 29, 31, 30, 31, 30,31, 31, 30, 31, 30, 31]
		
		# List of np months
		self.__npMonths = [
			[ 30, 32, 31, 32, 31, 30, 30, 30, 29, 30, 29, 31 ],	#2000
			[ 31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30 ],	#2001
			[ 31, 31, 32, 32, 31, 30, 30, 29, 30, 29, 30, 30 ],
			[ 31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 31 ],
			[ 30, 32, 31, 32, 31, 30, 30, 30, 29, 30, 29, 31 ],
			[ 31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30 ],
			[ 31, 31, 32, 32, 31, 30, 30, 29, 30, 29, 30, 30 ],
			[ 31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 31 ],
			[ 31, 31, 31, 32, 31, 31, 29, 30, 30, 29, 29, 31 ],
			[ 31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30 ],
			[ 31, 31, 32, 32, 31, 30, 30, 29, 30, 29, 30, 30 ],
			[ 31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 31 ],
			[ 31, 31, 31, 32, 31, 31, 29, 30, 30, 29, 30, 30 ],
			[ 31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30 ],
			[ 31, 31, 32, 32, 31, 30, 30, 29, 30, 29, 30, 30 ],
			[ 31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 31 ],
			[ 31, 31, 31, 32, 31, 31, 29, 30, 30, 29, 30, 30 ],
			[ 31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30 ],
			[ 31, 32, 31, 32, 31, 30, 30, 29, 30, 29, 30, 30 ],
			[ 31, 32, 31, 32, 31, 30, 30, 30, 29, 30, 29, 31 ],
			[ 31, 31, 31, 32, 31, 31, 30, 29, 30, 29, 30, 30 ],
			[ 31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30 ],
			[ 31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 30 ],
			[ 31, 32, 31, 32, 31, 30, 30, 30, 29, 30, 29, 31 ],
			[ 31, 31, 31, 32, 31, 31, 30, 29, 30, 29, 30, 30 ],
			[ 31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30 ],
			[ 31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 31 ],
			[ 30, 32, 31, 32, 31, 30, 30, 30, 29, 30, 29, 31 ],
			[ 31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30 ],
			[ 31, 31, 32, 31, 32, 30, 30, 29, 30, 29, 30, 30 ],
			[ 31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 31 ],
			[ 30, 32, 31, 32, 31, 30, 30, 30, 29, 30, 29, 31 ],
			[ 31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30 ],
			[ 31, 31, 32, 32, 31, 30, 30, 29, 30, 29, 30, 30 ],
			[ 31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 31 ],
			[ 30, 32, 31, 32, 31, 31, 29, 30, 30, 29, 29, 31 ],
			[ 31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30 ],
			[ 31, 31, 32, 32, 31, 30, 30, 29, 30, 29, 30, 30 ],
			[ 31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 31 ],
			[ 31, 31, 31, 32, 31, 31, 29, 30, 30, 29, 30, 30 ],
			[ 31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30 ],
			[ 31, 31, 32, 32, 31, 30, 30, 29, 30, 29, 30, 30 ],
			[ 31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 31 ],
			[ 31, 31, 31, 32, 31, 31, 29, 30, 30, 29, 30, 30 ],
			[ 31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30 ],
			[ 31, 32, 31, 32, 31, 30, 30, 29, 30, 29, 30, 30 ],
			[ 31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 31 ],
			[ 31, 31, 31, 32, 31, 31, 30, 29, 30, 29, 30, 30 ],
			[ 31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30 ],
			[ 31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 30 ],
			[ 31, 32, 31, 32, 31, 30, 30, 30, 29, 30, 29, 31 ],
			[ 31, 31, 31, 32, 31, 31, 30, 29, 30, 29, 30, 30 ],
			[ 31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30 ],
			[ 31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 30 ],
			[ 31, 32, 31, 32, 31, 30, 30, 30, 29, 30, 29, 31 ],
			[ 31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30 ],
			[ 31, 31, 32, 31, 32, 30, 30, 29, 30, 29, 30, 30 ],
			[ 31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 31 ],
			[ 30, 32, 31, 32, 31, 30, 30, 30, 29, 30, 29, 31 ],
			[ 31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30 ],
			[ 31, 31, 32, 32, 31, 30, 30, 29, 30, 29, 30, 30 ],
			[ 31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 31 ],
			[ 30, 32, 31, 32, 31, 31, 29, 30, 29, 30, 29, 31 ],
			[ 31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30 ],
			[ 31, 31, 32, 32, 31, 30, 30, 29, 30, 29, 30, 30 ],
			[ 31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 31 ],
			[ 31, 31, 31, 32, 31, 31, 29, 30, 30, 29, 29, 31 ],
			[ 31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30 ],
			[ 31, 31, 32, 32, 31, 30, 30, 29, 30, 29, 30, 30 ],
			[ 31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 31 ],
			[ 31, 31, 31, 32, 31, 31, 29, 30, 30, 29, 30, 30 ],
			[ 31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30 ],	#2071
			[ 31, 32, 31, 32, 31, 30, 30, 29, 30, 29, 30, 30 ],	#2072
			[ 31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 31 ],	#2073
			[ 31, 31, 31, 32, 31, 31, 30, 29, 30, 29, 30, 30 ],
			[ 31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30 ],
			[ 31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 30 ],
			[ 31, 32, 31, 32, 31, 30, 30, 30, 29, 30, 29, 31 ],
			[ 31, 31, 31, 32, 31, 31, 30, 29, 30, 29, 30, 30 ],
			[ 31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30 ],
			[ 31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 30 ],
			[ 31, 31, 32, 32, 31, 30, 30, 30, 29, 30, 30, 30 ],
			[ 30, 32, 31, 32, 31, 30, 30, 30, 29, 30, 30, 30 ],
			[ 31, 31, 32, 31, 31, 30, 30, 30, 29, 30, 30, 30 ],
			[ 31, 31, 32, 31, 31, 30, 30, 30, 29, 30, 30, 30 ],
			[ 31, 32, 31, 32, 30, 31, 30, 30, 29, 30, 30, 30 ],
			[ 30, 32, 31, 32, 31, 30, 30, 30, 29, 30, 30, 30 ],
			[ 31, 31, 32, 31, 31, 31, 30, 30, 29, 30, 30, 30 ],
			[ 30, 31, 32, 32, 30, 31, 30, 30, 29, 30, 30, 30 ],
			[ 30, 32, 31, 32, 31, 30, 30, 30, 29, 30, 30, 30 ],
			[ 30, 32, 31, 32, 31, 30, 30, 30, 29, 30, 30, 30 ],	#2090
			[ 31, 31, 32, 31, 31, 31, 30, 30, 29, 30, 30, 30 ],
			[ 30, 31, 32, 32, 31, 30, 30, 30, 29, 30, 30, 30 ],
			[ 30, 32, 31, 32, 31, 30, 30, 30, 29, 30, 30, 30 ],
			[ 31, 31, 32, 31, 31, 30, 30, 30, 29, 30, 30, 30 ],
			[ 31, 31, 32, 31, 31, 31, 30, 29, 30, 30, 30, 30 ],
			[ 30, 31, 32, 32, 31, 30, 30, 29, 30, 29, 30, 30 ],
			[ 31, 32, 31, 32, 31, 30, 30, 30, 29, 30, 30, 30 ],
			[ 31, 31, 32, 31, 31, 31, 29, 30, 29, 30, 29, 31 ],
			[ 31, 31, 32, 31, 31, 31, 30, 29, 29, 30, 30, 30 ]	 #2099
		]
		self.setCurrentDate()


	def setCurrentDate(self):
		"""
		Setting current en date
		"""
		year = int(time.strftime("%Y"))
		month = int(time.strftime("%m"))
		date = int(time.strftime("%d"))
		self.setEnDate(year, month, date)

	
	#En to Np date conversion

	def setEnDate(self,year, month, date):
		"""
		* Sets specific en dates to self object *
		Refrence np 2000/1/1 with en date 1943/4/14
		"""
		if(not self.__isEnRange(year,month,date)):
			raise Exception("Invalid date format.")

		self.__enYear = year
		self.__enMonth = month
		self.__enDay = date

		# Setting np reference to 2000/1/1 with en date 1943/4/14
		self.__npYear = 2000
		self.__npMonth = 1
		self.__npDay = 1

		difference = self.enDateDifference(1943, 4, 14)

		# Getting np year untill the difference remains less than 365
		index = 0
		while( difference >= self.____npYearDays(index) ):
			self.__npYear+=1
			difference = difference - self.____npYearDays(index)
			index+=1

		# Getting np month untill the difference remains less than 31
		i = 0
		while(difference >= self.__npMonths[index][i]):
			difference = difference - self.__npMonths[index][i]
			self.__npMonth+=1
			i+=1

		# Remaning days is the date
		self.__npDay = self.__npDay + difference
		
		self.weekDay()
		

	def toEnString(self, format='-'):
		return str(self.__enYear)+format+str(self.__enMonth)+format+str(self.__enDay)
		

	def enDateDifference(self, year, month, date):
		"""
		returns difference of days from the self date with the date provided
		"""
		difference = self.__countTotalEnDays(self.__enYear, self.__enMonth, self.__enDay) - self.__countTotalEnDays(year, month, date)
		if difference < 0: 
			return -difference
		else:
			return difference
	

	def __countTotalEnDays(self, year, month, date):

		totalDays = year * 365 + date
				
		for i in range(0,month-1):
			totalDays = totalDays + self.__enMonths[i]
		
		totalDays = totalDays + self.__countleap(year, month)
		return totalDays


	def __countleap(self, year, month):
		if (month <= 2):
			year-=1
		
		return (year//4-year//100+year//400)
		

	def __isEnRange(self, year, month, date):
		
		if(year < 1944 or year > 2042):
			return False
		
		if(month < 1 or month > 12):
			return False
		
		if(date < 1 or date > 31):
			return False
		
		return True
	

	def __isLeapYear(self, year):

		if(year%4 == 0):
			if(year%100 == 0):
				return (year%400 == 0)
			else:
				return True								
		else:
			return False



	# Np to En date conversion

	def setNpDate(self, year, month, date):
		"""
		* Sets specific np dates to self object *
		Refrence en 1994/1/1 with en date 2000/9/17
		"""
		if(not self.__isNpRange(year,month,date)):
			raise Exception("Invalid date format.")

		self.__npYear = year
		self.__npMonth = month
		self.__npDay = date
		
		# Setting en reference to 1944/1/1 with np date 2000/9/17
		self.__enYear = 1944
		self.__enMonth = 1
		self.__enDay = 1
		
		difference = self.npDateDifference(2000, 9, 17)
		
		# Getting en year untill the difference remains less than 365
		while( (difference >= 366 and self.__isLeapYear(self.__enYear)) or	(difference >= 365 and not(self.__isLeapYear(self.__enYear)) ) ):
			if( self.__isLeapYear(self.__enYear) ):
				difference -= 366
			else:
				difference -= 365
			self.__enYear += 1
		
		# Getting en month untill the difference remains less than 31
		if(self.__isLeapYear(self.__enYear)):
			monthDays = self.enLeapMonths
		else: 
			monthDays = self.__enMonths
		i = 0
		while( difference >= monthDays[i]):
			self.__enMonth+=1
			difference = difference - monthDays[i]
			i+=1
		
		# Remaning days is the date
		self.__enDay = self.__enDay + difference
		
		self.weekDay()


	def toNpString(self, format="-"):
		return str(self.__npYear)+format+str(self.__npMonth)+format+str(self.__npDay)

	
	def npDateDifference(self, year, month, date):

		# Getting difference from the current date with the date provided
		difference = self.__countTotalNpDays(self.__npYear, self.__npMonth, self.__npDay) - self.__countTotalNpDays(year, month, date)
		if(difference < 0):
			return -difference
		else:
			return difference


	def __countTotalNpDays(self, year, month, date):

		total = 0
		if(year < 2000):
			return 0
		
		total = total + (date-1)
		
		yearIndex = year - 2000
		for i in range(0,month-1):
			total = total + self.__npMonths[yearIndex][i]
		
		for i in range(0,yearIndex):
			total = total + self.____npYearDays(i)
		
		return total


	def ____npYearDays(self, index):
		total = 0
		
		for i in range(0,12):
			total += self.__npMonths[index][i]
		
		return total
		

	def __isNpRange(self, year, month, date):
		if(year < 2000 or year > 2098):
			return False
		
		if(month < 1 or month > 12):
			return False
		
		if(date < 1 or date > self.__npMonths[year-2000][month-1]):
			return False
		
		return True


	# Class Regular methods

	def weekDay(self):
		# Reference date 1943/4/14 Wednesday 
		difference = self.enDateDifference(1943, 4, 14)
		self.__week_day = ((3 + (difference%7) ) % 7 ) + 1
		return self.__week_day

	def enYear(self):
		return self.__enYear
	
	def enMonth(self):
		return self.__enMonth
	
	def enDay(self):
		return self.__enDay
	
	def npYear(self): 
		return self.__npYear
	
	def npMonth(self):
		return self.__npMonth
	
	def npDay(self):
		return self.__npDay

	def __str__(self):
		return "En Date: "+self.toEnString()+"\nNp Date: "+self.toNpString()+"\nDay: "+str(self.__week_day)


class HumanizeDate:
	__past_text = "अघि"
	__future_text = "पछि"
	__now_text = "भर्खरै"
	__year_text = "वर्ष"
	__month_text = "महिना"
	__day_text = "दिन"
	__hour_text = "घण्टा"
	__minute_text = "मिनेट"
	__second_text = "सेकेन्ड"

	def	__init__(self, *args, **kwargs):
		if not kwargs.get('date'):
			raise Exception('Date is required.') 
		self.date = kwargs['date'] + timedelta(hours=5, minutes=45)
		self.threshold = kwargs.get('threshold')
		current_date_time = datetime.now()
		current_date_time = current_date_time.replace(tzinfo=None)
		date = self.date.replace(tzinfo=None)
		self.seconds = int((current_date_time-date).total_seconds())
		self.interval_tense = self.__past_text
		if(self.seconds < 0):
			self.interval_tense = self.__future_text

	def get_str(self):
		seconds = self.seconds
		if( seconds < 0):
			seconds = 0 - seconds

		if not self.threshold == None:
			if( seconds >= self.threshold):
				return self.get_datetime().strip()
		
		return self.get_humanize().strip()


	def get_humanize(self):
		interval_value = 0
		interval_text = ""
		if( self.seconds == 0 ):
			# now
			return self.__now_text

		elif( self.seconds < 60):
			# seconds
			interval_value = self.seconds
			interval_text = self.__second_text
			
		elif( self.seconds < 3600):
			# minute
			interval_value = self.seconds//60
			interval_text = self.__minute_text

		elif( self.seconds < 86400):
			# hour
			interval_value = self.seconds//3600
			interval_text = self.__hour_text

		elif( self.seconds < 2592000):
			# day
			interval_value = self.seconds//86400
			interval_text = self.__day_text

		elif( self.seconds < 946080000):
			# month
			interval_value = self.seconds//2592000
			interval_text = self.__month_text

		else:
			# year
			interval_value = self.seconds//946080000
			interval_text = self.__year_text

		interval_value = NepaliChar.npNumber(interval_value)
		return str(interval_value)+' '+str(interval_text)+' '+self.interval_tense


	def get_datetime(self):
		local_date_time = self.date
		converter = DateConverter()
		converter.setEnDate(local_date_time.year, local_date_time.month, local_date_time.day)

		year = NepaliChar.npNumber(converter.__npYear())
		month = NepaliChar.__npMonth(converter.__npMonth())
		date = NepaliChar.npNumber(converter.__npDay())
		day = NepaliChar.__npDay(converter.weekDay())
		return month+' '+date+', '+year