import time

class NepaliDateConverter:
	
	__enMonths = [31, 28, 31, 30, 31, 30,31, 31, 30, 31, 30, 31]
	enLeapMonths = [31, 29, 31, 30, 31, 30,31, 31, 30, 31, 30, 31]
	
	# List of nepali months
	__npMonths = [
		[ 30, 32, 31, 32, 31, 30, 30, 30, 29, 30, 29, 31 ],	# 2000 BS - 1944 AD
		[ 31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30 ],	# 2001 BS
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
		[ 31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30 ],	# 2071 BS
		[ 31, 32, 31, 32, 31, 30, 30, 29, 30, 29, 30, 30 ],	# 2072 BS
		[ 31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 31 ],	# 2073 BS
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
		[ 30, 32, 31, 32, 31, 30, 30, 30, 29, 30, 30, 30 ],	# 2090 BS
		[ 31, 31, 32, 31, 31, 31, 30, 30, 29, 30, 30, 30 ],
		[ 30, 31, 32, 32, 31, 30, 30, 30, 29, 30, 30, 30 ],
		[ 30, 32, 31, 32, 31, 30, 30, 30, 29, 30, 30, 30 ],
		[ 31, 31, 32, 31, 31, 30, 30, 30, 29, 30, 30, 30 ],
		[ 31, 31, 32, 31, 31, 31, 30, 29, 30, 30, 30, 30 ],
		[ 30, 31, 32, 32, 31, 30, 30, 29, 30, 29, 30, 30 ],
		[ 31, 32, 31, 32, 31, 30, 30, 30, 29, 30, 30, 30 ],
		[ 31, 31, 32, 31, 31, 31, 29, 30, 29, 30, 29, 31 ],
		[ 31, 31, 32, 31, 31, 31, 30, 29, 29, 30, 30, 30 ]	 # 2099 BS - 2042 AD
	]

	def set_current_date(self):
		year = int(time.strftime("%Y"))
		month = int(time.strftime("%m"))
		date = int(time.strftime("%d"))
		self.set_english_date(year, month, date)

	# English to Nepali date conversion

	def set_english_date(self,year, month, date):
		"""
		* Sets specific en dates to self object *
		Reference np 2000/1/1 with en date 1943/4/14
		"""
		if(not self.__isEnRange(year,month,date)):
			raise Exception("Date out of range")

		self.__enYear = year
		self.__enMonth = month
		self.__enDay = date

		# Setting np reference to 2000/1/1 with en date 1943/4/14
		self.__npYear = 2000
		self.__npMonth = 1
		self.__npDay = 1

		difference = self.enDateDifference(1943, 4, 14)

		# Getting np year until the difference remains less than 365
		index = 0
		while( difference >= self.__npYearDays(index) ):
			self.__npYear+=1
			difference = difference - self.__npYearDays(index)
			index+=1

		# Getting np month until the difference remains less than 31
		i = 0
		while(difference >= self.__npMonths[index][i]):
			difference = difference - self.__npMonths[index][i]
			self.__npMonth+=1
			i+=1

		# Remaning days is the date
		self.__npDay = self.__npDay + difference
		
		self.__calculate_week_day()
		

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
		""" counts english date in days with 0000-01-01 """

		totalDays = year * 365 + date
				
		for i in range(0,month-1):
			totalDays = totalDays + self.__enMonths[i]
		
		totalDays = totalDays + self.__countleap(year, month)
		return totalDays


	def __countleap(self, year, month):
		""" counts total leap years from year/month to 0000/01 """
		if (month <= 2):
			year-=1
		
		return (year//4-year//100+year//400)
		

	def __isEnRange(self, year, month, date):
		""" checks if english date in within range 1944 - 2042 """ 
		if(year < 1944 or year > 2042):
			return False
		
		if(month < 1 or month > 12):
			return False
		
		if(date < 1 or date > 31):
			return False
		
		return True
	

	def __isLeapYear(self, year):
		""" independent method to check leap year """
		if(year%4 == 0):
			if(year%100 == 0):
				return (year%400 == 0)
			else:
				return True								
		else:
			return False



	# Nepali to English date conversion

	def set_nepali_date(self, year, month, date):
		"""
		* Sets specific np dates to self object *
		Reference en 1994/1/1 with en date 2000/9/17
		"""
		if(not self.__isNpRange(year,month,date)):
			raise Exception("Date out of range")

		self.__npYear = year
		self.__npMonth = month
		self.__npDay = date
		
		# Setting en reference to 1944/1/1 with np date 2000/9/17
		self.__enYear = 1944
		self.__enMonth = 1
		self.__enDay = 1
		
		difference = self.npDateDifference(2000, 9, 17)
		
		# Getting en year until the difference remains less than 365
		while( (difference >= 366 and self.__isLeapYear(self.__enYear)) or	(difference >= 365 and not(self.__isLeapYear(self.__enYear)) ) ):
			if( self.__isLeapYear(self.__enYear) ):
				difference -= 366
			else:
				difference -= 365
			self.__enYear += 1
		
		# Getting en month until the difference remains less than 31
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
		
		self.__calculate_week_day()


	def toNpString(self, format="-"):
		return str(self.npYear())+format+str(self.npMonthStr())+format+str(self.npDayStr())

	
	def npDateDifference(self, year, month, date):
		""" 
		Getting difference from the current date with the date provided 
		"""
		difference = self.__countTotalNpDays(self.__npYear, self.__npMonth, self.__npDay) - self.__countTotalNpDays(year, month, date)
		if(difference < 0):
			return -difference
		else:
			return difference


	def __countTotalNpDays(self, year, month, date):
		""" counts nepali date in days with 2000-01-01 (nepali date) """

		total = 0
		if(year < 2000):
			return 0
		
		total = total + (date-1)
		
		yearIndex = year - 2000
		for i in range(0,month-1):
			total = total + self.__npMonths[yearIndex][i]
		
		for i in range(0,yearIndex):
			total = total + self.__npYearDays(i)
		
		return total


	def __npYearDays(self, index):
		"""
		count total days of specific year ( from index)
		input: index (year)
		return total (days)

		eg, for 2075 => 2075-2000 = 75 
		__npYearDays(75) => 365 days

		"""
		total = 0
		
		for i in range(0,12):
			total += self.__npMonths[index][i]
		
		return total
		

	def __isNpRange(self, year, month, date):
		""" checks if nepali date is in range 2000-2098 """
		if(year < 2000 or year > 2098):
			return False
		
		if(month < 1 or month > 12):
			return False
		
		if(date < 1 or date > self.__npMonths[year-2000][month-1]):
			return False
		
		return True

	def __calculate_week_day(self):
		# Reference date 1943/4/14 Wednesday 
		difference = self.enDateDifference(1943, 4, 14)
		self.__week_day = ((3 + (difference%7) ) % 7 ) + 1
		return self.__week_day

	# Properties
	def weekday(self):
		return self.__week_day

	@property
	def year_en(self):
		return self.__enYear
	
	@property
	def month_en(self):
		return self.__enMonth
	
	@property
	def day_en(self):
		return self.__enDay
	
	@property
	def year_np(self): 
		return self.__npYear
	
	@property
	def month_np(self):
		return self.__npMonth
	
	@property
	def day_np(self):
		return self.__npDay


	# Class static methods

	@classmethod
	def get_converter_object(cls):
		if not hasattr(cls, '__converter_Cache'):
			cls.__converter_Cache = cls()
		return cls.__converter_Cache

	@classmethod
	def english_to_nepali(cls, year, month, day):
		converter = cls.get_converter_object()
		converter.set_english_date(year, month, day)
		return converter.year_np, converter.month_np, converter.day_np

	@classmethod
	def nepali_to_english(cls, year, month, day):
		converter = cls.get_converter_object()
		converter.set_nepali_date(year, month, day)
		return converter.year_en, converter.month_en, converter.day_en

	@classmethod
	def current_english_date(cls):
		converter = cls.get_converter_object()
		converter.set_current_date()
		return converter.year_en, converter.month_en, converter.day_en

	@classmethod
	def current_nepali_date(cls):
		return cls.english_to_nepali(*cls.current_english_date())
