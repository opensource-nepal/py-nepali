from .number import NepaliNumber


MONTHS_MAP = {
	'बैशाख': 'Baishakh',
	'जेठ': 'Jestha',
	'असार': 'Ashad',
	'साउन': 'Sharwan',
	'भदौ': 'Bhadra',
	'असोज': 'Ashwin',
	'कात्तिक': 'Kartik',
	'मंसिर': 'Mangsir',
	'पुस': 'Poush',
	'माघ': 'Magh',
	'फागुन': 'Falgun',
	'चैत': 'Chaitra',
}

DAYS_MAP = {
	'आइतबार': 'Sunday',
	'सोमबार': 'Monday',
	'मंगलबार': 'Tuesday',
	'बुधबार': 'Wednesday',
	'बिहीबार': 'Thursday',
	'शुक्रबार': 'Friday',
	'शनिबार': 'Saturday',
}

HALF_DAYS_MAP = {
	'आइत': 'Sun',
	'सोम': 'Mon',
	'मंगल': 'Tue',
	'बुध': 'Wed',
	'बिही': 'Thu',
	'शुक्र': 'Fri',
	'शनि': 'Sat',
}

AM_PM_MAP = {
	'शुभप्रभात' : 'AM',
	'मध्यान्ह': 'PM',
	'अपरान्ह': 'PM',
}



class NepaliChar:

	@staticmethod
	def number(num):
		return NepaliNumber.convert(num)

	@staticmethod
	def day(day):
		days = ['आइतबार','सोमबार','मंगलबार','बुधबार','बिहीबार','शुक्रबार','शनिबार']
		return days[day-1]

	@staticmethod
	def half_day(day):
		days = ['आइत','सोम','मंगल','बुध','बिही','शुक्र','शनि']
		return days[day-1]

	@staticmethod
	def month(month):
		months = ['बैशाख','जेठ','असार','साउन','भदौ','असोज','कात्तिक','मंसिर','पुस','माघ','फागुन','चैत']
		return months[month-1]

class EnglishChar:
	months = ['Baishakh','Jestha','Ashad','Sharwan','Bhadra','Ashwin','Kartik','Mangsir','Poush','Magh','Falgun','Chaitra']
	days = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
	days_half = ['Sun','Mon','Tue','Wed','Thu','Fri','Sat']
	
	@staticmethod
	def day(day):
		return EnglishChar.days[day-1]

	@staticmethod
	def half_day(day):
		return EnglishChar.days_half[day-1]

	@staticmethod
	def month(month):
		return EnglishChar.months[month-1]


def nepali_to_english_text(text):
	# TODO: optimization

	from .number import NepaliNumber

	# replacing months
	for k,v in MONTHS_MAP.items():
		text = text.replace(k, v)
	
	# replacing days
	for k,v in DAYS_MAP.items():
		text = text.replace(k, v)
	
	# replacing half days
	for k,v in HALF_DAYS_MAP.items():
		text = text.replace(k, v)

	for k,v in AM_PM_MAP.items():
		text = text.replace(k, v)

	return NepaliNumber.revert(text)