class NepaliNumber:
	
	@staticmethod
	def nepali(num):
		nepaliNumbers = ['०','१','२','३','४','५','६','७','८','९']
		np_num = ''
		en_num = str(num)
		for e in en_num:
			if e in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
				np_num = np_num+str(nepaliNumbers[int(e)])
			else:
				np_num = np_num+str(e)
		return np_num