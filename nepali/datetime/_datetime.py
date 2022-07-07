#
#
#	Author : Ajesh Sen Thapa
#	Website: www.ajesh.com.np
#
#

import time
import datetime as pythonDateTime
import warnings

from nepali.timezone import NepaliTimeZone, utc_now
from nepali.utils import to_nepali_timezone

from ._converter import NepaliDateConverter


class formater_class_mixin:
	def get_formater_class(self):
		return self.__class__.get_formater_class()

	@classmethod
	def get_formater_class(cls):
		if not hasattr(cls, '__formater_class__Cache'):
			from ._formarter import NepaliDateTimeFormater
			cls.__formater_class__Cache = NepaliDateTimeFormater
		return cls.__formater_class__Cache

	@classmethod
	def get_strptime_method(cls):
		if not hasattr(cls, '_strptime_method_CACHE'):
			from .parser import strptime
			cls._strptime_method_CACHE = strptime
		return cls._strptime_method_CACHE

class nepalidate(formater_class_mixin):
	def __init__(self, year, month, day) -> None:
		self.__year = year
		self.__month = month
		self.__day = day

		# converting to english date
		year_en, month_en, day_en = NepaliDateConverter.nepali_to_english(year, month, day)
		self.__python_date = pythonDateTime.date(year_en, month_en, day_en)

	def __str__(self):
		return self.strftime_en('%Y-%m-%d')

	def __repr__(self):
		return "<nepalidate> "+str(self)
	
	def to_datetime(self):
		return pythonDateTime.datetime.combine(self.__python_date, pythonDateTime.time(), tzinfo=NepaliTimeZone())

	def to_date(self):
		return self.__python_date

	def to_nepalidatetime(self):
		return nepalidatetime.from_nepali_date(self)

	def to_nepali_datetime(self):
		warnings.warn(
			message="nepalidate.to_nepali_datetime is depreciated and no longer be available in version >= 1.0.0, use nepalidate.to_nepalidatetime instead.", 
			category=DeprecationWarning
		)
		return self.to_nepalidatetime()

	def strftime(self, format):
		NepaliDateTimeFormater = self.get_formater_class()
		formater = NepaliDateTimeFormater(self)
		return formater.get_str(format)

	def strftime_en(self, format):
		NepaliDateTimeFormater = self.get_formater_class()
		formater = NepaliDateTimeFormater(self, english=True)
		return formater.get_str(format)

	
	# operators overloading
	# TODO: add more operators overloading
	def __eq__(self, other):
		""" equal """
		
		if type(other) == self.__class__:
			"""
			NepaliDate object
			"""
			return self.to_date() == other.to_date()

		elif type(other) == pythonDateTime.date:
			"""
			pythonDate object
			"""
			return self.to_date() == to_nepali_timezone(other)
			
		return False

	# static methods
	@classmethod
	def strptime(cls, datetime_str, format):
		nepalidatetime_strptime = cls.get_strptime_method()
		return nepalidatetime_strptime(datetime_str, format=format).date()

	@staticmethod
	def now(*args, **kwargs):
		return nepalidate.today()

	@staticmethod
	def today():
		year, month, day = NepaliDateConverter.current_nepali_date()
		return nepalidate(year, month, day)

	@staticmethod
	def from_datetime(datetime_object):
		return nepalidate.from_date(datetime_object.date())

	@staticmethod
	def from_date(date_object):
		npDate = nepalidate(*NepaliDateConverter.english_to_nepali(date_object.year, date_object.month, date_object.day))
		return npDate

	@staticmethod
	def from_nepalidatetime(datetime_object):
		return datetime_object.date()

	# property

	def weekday(self):
		'''
		Sunday => 0, Saturday => 6
		'''
		return (self.__python_date.weekday() + 1) % 7
		return self.__python_date.weekday()

	# nepali date properties
	@property
	def year(self):
		return self.__year

	@property
	def month(self):
		return self.__month

	@property
	def day(self):
		return self.__day

	@property
	def week_day(self):
		warnings.warn(
			message="nepalidate.week_day field is depreciated and no longer be available in version >= 1.0.0, use nepalidate.weekday() method instead.", 
			category=DeprecationWarning
		)
		return self.weekday()

class nepalitime(pythonDateTime.time):

	def __repr__(self):
		return "<nepalitime> "+str(self)

	# static methods
	
	@staticmethod
	def now(*args, **kwargs):
		dt_now = pythonDateTime.datetime.now()
		return nepalitime(dt_now.hour, dt_now.minute, dt_now.second, dt_now.microsecond)


class nepalidatetime(formater_class_mixin):
	"""
	nepalidatetime
	"""

	def __init__(self, year, month, day, hour=0, minute=0, second=0, microsecond=0):
		self.__npDate = nepalidate(year, month, day)
		self.__npTime = nepalitime(hour, minute, second, microsecond) 

	def __str__(self):
		return str(self.__npDate)+' '+str(self.__npTime)

	def __repr__(self):
		return "<nepalidatetime> "+str(self)


	# operator overloadings

	def __add__(self, other):
		""" addition """

		if type(other) == pythonDateTime.timedelta:
			"""
			timedelta object
			"""
			return nepalidatetime.from_datetime(self.to_datetime() + other)


		return None

	def __sub__(self, other):
		""" substraction """

		if type(other) == self.__class__:
			"""
			nepalidatetime object
			"""
			return self.to_datetime() - other.to_datetime()

		elif type(other) == pythonDateTime.datetime:
			return self.to_datetime() - to_nepali_timezone(other)

		elif type(other) == pythonDateTime.timedelta:
			"""
			timedelta object
			"""
			return nepalidatetime.from_datetime(self.to_datetime() - other)


		return None

	def __lt__(self, other):
		""" less than """

		if type(other) == self.__class__:
			"""
			nepalidatetime object
			"""
			return self.to_datetime() < other.to_datetime()

		elif type(other) == pythonDateTime.datetime:
			"""
			pythonDateTime object
			"""
			return self.to_datetime() < to_nepali_timezone(other)


		return None

	def __le__(self, other):
		""" less than equal """

		if type(other) == self.__class__:
			"""
			nepalidatetime object
			"""
			return self.to_datetime() <= other.to_datetime()

		elif type(other) == pythonDateTime.datetime:
			"""
			pythonDateTime object
			"""
			return self.to_datetime() <= to_nepali_timezone(other)


		return None

	def __eq__(self, other):
		""" equal """
		
		if type(other) == self.__class__:
			"""
			nepalidatetime object
			"""
			return self.to_datetime() == other.to_datetime()

		elif type(other) == pythonDateTime.datetime:
			"""
			pythonDateTime object
			"""
			return self.to_datetime() == to_nepali_timezone(other)

		return False


	def __ne__(self, other):
		""" not equal """

		if type(other) == self.__class__:
			"""
			nepalidatetime object
			"""
			return self.to_datetime() != other.to_datetime()

		elif type(other) == pythonDateTime.datetime:
			"""
			pythonDateTime object
			"""
			return self.to_datetime() != to_nepali_timezone(other)
		
		return True
	
	def __gt__(self, other):
		""" greater than """

		if type(other) == self.__class__:
			"""
			nepalidatetime object
			"""
			return self.to_datetime() > other.to_datetime()

		elif type(other) == pythonDateTime.datetime:
			"""
			pythonDateTime object
			"""
			return self.to_datetime() > to_nepali_timezone(other)

			
		return None
	
	def __ge__(self, other):
		""" greater than equal """

		if type(other) == self.__class__:
			"""
			nepalidatetime object
			"""
			return self.to_datetime() >= other.to_datetime()

		elif type(other) == pythonDateTime.datetime:
			"""
			pythonDateTime object
			"""
			return self.to_datetime() >= to_nepali_timezone(other)

			
		return None 

	# object transformation
	def to_datetime(self):
		return pythonDateTime.datetime.combine(self.__npDate.to_date(), self.__npTime, tzinfo=NepaliTimeZone())

	def to_date(self):
		return self.to_datetime().date()

	def date(self):
		return self.__npDate

	def time(self):
		return self.__npTime

	# string format
	def strftime(self, format):
		NepaliDateTimeFormater = self.get_formater_class()
		formater = NepaliDateTimeFormater(self)
		return formater.get_str(format)

	def strftime_en(self, format):
		NepaliDateTimeFormater = self.get_formater_class()
		formater = NepaliDateTimeFormater(self, english=True)
		return formater.get_str(format)

	# static methods

	@classmethod
	def strptime(cls, datetime_str, format):
		nepalidatetime_strptime = cls.get_strptime_method()
		return nepalidatetime_strptime(datetime_str, format=format)

	@staticmethod
	def from_datetime(dt):
		dt = to_nepali_timezone(dt)
		nd = nepalidate.from_date(dt.date())
		return nepalidatetime(nd.year, nd.month, nd.day, dt.hour, dt.minute, dt.second, dt.microsecond)

	@staticmethod
	def from_date(date_object):
		nepali_date_object = nepalidate.from_date(date_object)
		return nepalidatetime.from_nepali_date(nepali_date_object)

	@staticmethod
	def from_nepali_date(nepali_date_object):
		return nepalidatetime(nepali_date_object.year, nepali_date_object.month, nepali_date_object.day)

	@staticmethod
	def now():
		return nepalidatetime.from_datetime(utc_now())

	# property

	@property
	def year(self):
		return self.__npDate.year

	@property
	def month(self):
		return self.__npDate.month

	@property
	def day(self):
		return self.__npDate.day

	def weekday(self):
		'''
		Sunday => 0, Saturday => 6
		'''
		return self.__npDate.weekday()

	@property
	def week_day(self):
		warnings.warn(
			message="nepalidate.week_day field is depreciated and no longer be available in version >= 1.0.0, use nepalidatetime.weekday() method instead.", 
			category=DeprecationWarning
		)
		return self.__npDate.weekday()

	@property
	def hour(self):
		return self.__npTime.hour

	@property
	def minute(self):
		return self.__npTime.minute

	@property
	def second(self):
		return self.__npTime.second


class NepaliDate(nepalidate):
	def __init__(self, *args, **kwargs):
		warnings.warn(
			message="NepaliDate is depreciated and no longer be available in version >= 1.0.0, use nepalidate instead.", 
			category=DeprecationWarning
		)
		super().__init__(*args, **kwargs)

class NepaliTime(nepalidate):
	def __init__(self, *args, **kwargs):
		warnings.warn(
			message="NepaliTime is depreciated and no longer be available in version >= 1.0.0, use nepalitime instead.", 
			category=DeprecationWarning
		)
		super().__init__(*args, **kwargs)

class NepaliDateTime(nepalidate):
	def __init__(self, *args, **kwargs):
		warnings.warn(
			message="NepaliDateTime is depreciated and no longer be available in version >= 1.0.0, use nepalidatetime instead.", 
			category=DeprecationWarning
		)
		super().__init__(*args, **kwargs)

