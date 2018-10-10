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