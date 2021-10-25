'''
validates parsing
'''

def _extract(datetime_str, format):
	'''
	extracts year, month, day, hour, minute from the given format
	
	eg.
	INPUT:
	datetime_str="2078-01-12" 
	format="%Y-%m-%d"

	OUTPUT:
	{
		"%Y": 2078,
		"%m": 1,
		"%d": 12,
	}
	'''
	pass

def _transform(data):
	'''
	transforms different format data to uniform data

	eg.
	INPUT:
	data = {
		"%Y": 2078,
		"%b": "मंसिर",
		"%d": 12,
	}

	OUTPUT:
	{
		"year": 2078,
		"month": 8,
		"day": 12
	}
	'''

def _validate(datetime_str, format):
	'''
	validates datetime_str with the format
	Perform step by step test for fast performance. The steps are:
	-
	-
	returns False if validation failed
	returns nepalidatetime object if validation success.
	'''