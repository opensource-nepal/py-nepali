class NepaliNumber:
	
	@classmethod
	def convert_and_add_comma(cls, number):
		return cls.add_comma(cls.convert(number))

	@staticmethod
	def convert(num):
		nepaliNumbers = ['०','१','२','३','४','५','६','७','८','९']
		np_num = ''
		en_num = str(num)
		for e in en_num:
			if e in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
				np_num = np_num+str(nepaliNumbers[int(e)])
			else:
				np_num = np_num+str(e)
		return np_num

	@staticmethod
	def revert(num):
		nepaliNumbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
		np_num = ''
		en_num = str(num)
		for e in en_num:
			if e in ['०','१','२','३','४','५','६','७','८','९']:
				np_num = np_num+str(nepaliNumbers[int(e)])
			else:
				np_num = np_num+str(e)
		return np_num

	@staticmethod
	def add_comma(number):
		number_with_comma = ""
		counter = 0
		for nepali_number_char in list(str(number))[::-1]:
			if counter == 3:
				number_with_comma = ',' + number_with_comma

			elif counter != 1 and counter != 3 and (counter-1) % 2 == 0:
				number_with_comma = ',' + number_with_comma
			
			number_with_comma = nepali_number_char + number_with_comma

			# increasing counter	
			counter += 1
		
		return number_with_comma

	@staticmethod
	def add_comma_english(number):
		return '{:,}'.format(number)
