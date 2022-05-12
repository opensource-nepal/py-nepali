import datetime as pythonDateTime

from nepali.char import NepaliChar
from nepali.timezone import now
from nepali.exceptions import InvalidNepaliDateTimeObjectException
from nepali.utils import to_nepali_timezone

from ._datetime import nepalidate, nepalidatetime

class HumanizeDateTime:
	"""
	HumanizeDate converts NepaliDateTime to nepali human readable form
	"""

	__past_text = "अघि"
	__future_text = "पछि"
	__now_text = "भर्खरै"
	__year_text = "वर्ष"
	__month_text = "महिना"
	__day_text = "दिन"
	__hour_text = "घण्टा"
	__minute_text = "मिनेट"
	__second_text = "सेकेन्ड"

	def	__init__(self, datetime_obj, *args, **kwargs):
		""" 
		initializes humanize class
		datetime_obj: python datetime object to be humanized
		threshold (kwargs): threshold to be humanize
		format (kwargs): format to display behind threshold
		"""
		if type(datetime_obj) == nepalidatetime:
			self.datetime_obj = datetime_obj.to_datetime()
		elif type(datetime_obj) == nepalidate:
			self.datetime_obj = nepalidatetime.from_nepali_date(datetime_obj).to_datetime()
		elif type(datetime_obj) == pythonDateTime.date:
			self.datetime_obj = nepalidatetime.from_date(datetime_obj).to_datetime()
		elif type(datetime_obj) == pythonDateTime.datetime:
			self.datetime_obj = to_nepali_timezone(datetime_obj)
		else:
			raise InvalidNepaliDateTimeObjectException('Argument must be instance of NepaliDate or NepaliDateTime or datetime.datetime or datetime.date') 

		self.threshold = kwargs.get('threshold')
		self.format = kwargs.get('format')

		# seconds after from now to datetime_obj
		self.seconds = None


	def __calc_seconds(self):
		""" calculates total seconds from now """

		current_date_time = now()
		date = self.datetime_obj
		self.seconds = int((current_date_time-date).total_seconds())
		self.interval_tense = self.__past_text
		if(self.seconds < 0):
			self.interval_tense = self.__future_text

	def to_str(self):
		""" returns humanize string """

		self.__calc_seconds()	# refreshing seconds
		seconds = self.seconds
		if( seconds < 0):
			seconds = 0 - seconds

		if not self.threshold == None:
			if( seconds >= self.threshold):
				return self.get_datetime().strip()
		
		return self.get_humanize().strip()


	def get_humanize(self):
		"""
		returns humanize datetime
		"""
		self.__calc_seconds()	# refreshing seconds

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

		interval_value = NepaliChar.number(interval_value)
		return str(interval_value)+' '+str(interval_text)+' '+self.interval_tense


	def get_datetime(self):
		"""
		returns date in nepali characters
		"""
		if not self.format:
			self.format = '%B %d, %Y'
		ndt = nepalidatetime.from_datetime(self.datetime_obj)
		return ndt.strftime(self.format)

	def __str__(self):
		return self.to_str()

	def __repr__(self):
		return str(self)


def nepalihumanize(datetime_obj, threshold=None, format=None):
	""" returns to humanize nepalidatetime """
	return HumanizeDateTime(datetime_obj, threshold=threshold, format=format).to_str()
