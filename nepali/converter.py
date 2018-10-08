#
#
#	Author : Ajesh Sen Thapa
#	Website: www.ajesh.com.np
#
#

import time
from datetime import datetime, timedelta

class DateConverter:
	
	def __init__(self):

		self.englishMonths = [31, 28, 31, 30, 31, 30,31, 31, 30, 31, 30, 31]
		self.englishLeapMonths = [31, 29, 31, 30, 31, 30,31, 31, 30, 31, 30, 31]
		
		# List of nepali months
		self.nepaliMonths = [
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
		Setting current english date
		"""
		year = int(time.strftime("%Y"))
		month = int(time.strftime("%m"))
		date = int(time.strftime("%d"))
		self.setEnglishDate(year, month, date)

	
	#English to Nepali date conversion

	def setEnglishDate(self,year, month, date):
		if(not self.__isEnglishRange(year,month,date)):
			raise Exception("Invalid date format.")

		self.englishYear = year
		self.englishMonth = month
		self.englishDate = date

		#Setting nepali reference to 2000/1/1 with english date 1943/4/14
		self.nepaliYear = 2000
		self.nepaliMonth = 1
		self.nepaliDate = 1

		difference = self.enDateDifference(1943, 4, 14)

		#Getting nepali year untill the difference remains less than 365
		index = 0
		while( difference >= self.__nepaliYearDays(index) ):
			self.nepaliYear+=1
			difference = difference - self.__nepaliYearDays(index)
			index+=1

		#Getting nepali month untill the difference remains less than 31
		i = 0
		while(difference >= self.nepaliMonths[index][i]):
			difference = difference - self.nepaliMonths[index][i]
			self.nepaliMonth+=1
			i+=1

		#Remaning days is the date
		self.nepaliDate = self.nepaliDate + difference
		
		self.weekDay()
		

	def toEnglishString(self, format='-'):
		return str(self.englishYear)+format+str(self.englishMonth)+format+str(self.englishDate)
		

	def enDateDifference(self, year, month, date):
		
		#Getting difference from the current date with the date provided
		difference = self.__countTotalEnglishDays(self.englishYear, self.englishMonth, self.englishDate) - self.__countTotalEnglishDays(year, month, date)
		if difference < 0: 
			return -difference
		else:
			return difference
	

	def __countTotalEnglishDays(self, year, month, date):

		totalDays = year * 365 + date
				
		for i in range(0,month-1):
			totalDays = totalDays + self.englishMonths[i]
		
		totalDays = totalDays + self.__countleap(year, month)
		return totalDays


	def __countleap(self, year, month):
		if (month <= 2):
			year-=1
		
		return (year//4-year//100+year//400)
		

	def __isEnglishRange(self, year, month, date):
		
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



	#Nepali to English date conversion

	def setNepaliDate(self, year, month, date):

		if(not self.__isNepaliRange(year,month,date)):
			raise Exception("Invalid date format.")

		self.nepaliYear = year
		self.nepaliMonth = month
		self.nepaliDate = date
		
		#Setting english reference to 1944/1/1 with nepali date 2000/9/17
		self.englishYear = 1944
		self.englishMonth = 1
		self.englishDate = 1
		
		difference = self.npDateDifference(2000, 9, 17)
		
		#Getting english year untill the difference remains less than 365
		while( (difference >= 366 and self.__isLeapYear(self.englishYear)) or	(difference >= 365 and not(self.__isLeapYear(self.englishYear)) ) ):
			if( self.__isLeapYear(self.englishYear) ):
				difference -= 366
			else:
				difference -= 365
			self.englishYear += 1
		
		#Getting english month untill the difference remains less than 31
		if(self.__isLeapYear(self.englishYear)):
			monthDays = self.englishLeapMonths
		else: 
			monthDays = self.englishMonths
		i = 0
		while( difference >= monthDays[i]):
			self.englishMonth+=1
			difference = difference - monthDays[i]
			i+=1
		
		#Remaning days is the date
		self.englishDate = self.englishDate + difference
		
		self.weekDay()


	def toNepaliString(self, format="-"):
		return str(self.nepaliYear)+format+str(self.nepaliMonth)+format+str(self.nepaliDate)

	
	def npDateDifference(self, year, month, date):

		#Getting difference from the current date with the date provided
		difference = self.__countTotalNepaliDays(self.nepaliYear, self.nepaliMonth, self.nepaliDate) - self.__countTotalNepaliDays(year, month, date)
		if(difference < 0):
			return -difference
		else:
			return difference


	def __countTotalNepaliDays(self, year, month, date):

		total = 0
		if(year < 2000):
			return 0
		
		total = total + (date-1)
		
		yearIndex = year - 2000
		for i in range(0,month-1):
			total = total + self.nepaliMonths[yearIndex][i]
		
		for i in range(0,yearIndex):
			total = total + self.__nepaliYearDays(i)
		
		return total


	def __nepaliYearDays(self, index):
		total = 0
		
		for i in range(0,12):
			total += self.nepaliMonths[index][i]
		
		return total
		

	def __isNepaliRange(self, year, month, date):
		if(year < 2000 or year > 2098):
			return False
		
		if(month < 1 or month > 12):
			return False
		
		if(date < 1 or date > self.nepaliMonths[year-2000][month-1]):
			return False
		
		return True


	#Class Regular methods

	def weekDay(self):
		#Reference date 1943/4/14 Wednesday 
		difference = self.enDateDifference(1943, 4, 14)
		self.day = ((3 + (difference%7) ) % 7 ) + 1
		return self.day

	def enYear(self):
		return self.englishYear
	
	def enMonth(self):
		return self.englishMonth

	def enMonth(self):
		return self.englishMonth
	
	def enDay(self):
		return self.englishDate
	
	def npYear(self): 
		return self.nepaliYear
	
	def npMonth(self):
		return self.nepaliMonth
	
	def npDay(self):
		return self.nepaliDate

	def __str__(self):
		return "English Date: "+self.toEnglishString()+"\nNepali Date: "+self.toNepaliString()+"\nDay: "+str(self.day)


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
		converter.setEnglishDate(local_date_time.year, local_date_time.month, local_date_time.day)

		year = NepaliChar.npNumber(converter.npYear())
		month = NepaliChar.npMonth(converter.npMonth())
		date = NepaliChar.npNumber(converter.npDay())
		day = NepaliChar.npDay(converter.weekDay())
		return month+' '+date+', '+year


class NepaliChar:

	def npNumber(num):
		nepaliNumbers = ['०','१','२','३','४','५','६','७','८','९'];
		np_num = '';
		en_num = str(num);
		for e in en_num:
			np_num = str(np_num)+str(nepaliNumbers[ int(e) ])
		return np_num

	def npDay(day):
		days = ['आइतबार','सोमबार','मंगलबार','बुधबार','बिहिबार','शुक्रबार','शनिबार'];
		return days[day-1];

	def npHalfDay(day):
		days = ['आइत','सोम','मंगल','बुध','बिहि','शुक्र','शनि']
		return days[day-1]

	def npMonth(month):
		months = ['बैशाख','जेठ','असार','श्रावण','भदौ','आश्विन','कार्तिक','मंसिर','पुष','माघ','फाल्गुन','चैत्र']
		return months[month-1]
