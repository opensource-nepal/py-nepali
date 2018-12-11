class NepaliChar:

	def number(num):
		nepaliNumbers = ['०','१','२','३','४','५','६','७','८','९'];
		np_num = '';
		en_num = str(num);
		for e in en_num:
			np_num = str(np_num)+str(nepaliNumbers[ int(e) ])
		return np_num

	def day(day):
		days = ['आइतबार','सोमबार','मंगलबार','बुधबार','बिहिबार','शुक्रबार','शनिबार'];
		return days[day-1];

	def half_day(day):
		days = ['आइत','सोम','मंगल','बुध','बिहि','शुक्र','शनि']
		return days[day-1]

	def month(month):
		months = ['बैशाख','जेठ','असार','श्रावण','भदौ','आश्विन','कार्तिक','मंसिर','पुष','माघ','फाल्गुन','चैत्र']
		return months[month-1]

class EnglishChar:

	def day(day):
		days = ['Sunday','Monday','Tuesday','Wednesday','Thrusday','Friday','Saturday'];
		return days[day-1];

	def half_day(day):
		days = ['Sun','Mon','Tue','Wed','Thu','Fri','Sat']
		return days[day-1]

	def month(month):
		months = ['Baishakh','Jestha','Ashad','Sharwan','Bhadra','Ashwin','Kartik','Mangsir','Poush','Magh','Falgun','Chaitra']
		return months[month-1]