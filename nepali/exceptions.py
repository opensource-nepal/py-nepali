"""
Exceptions for nepali
"""

class InvalidDateFormatException(Exception):
    pass

class InvalidDateTimeFormatException(Exception):
    pass

class InvalidNepaliDateTimeObjectException(Exception):
    pass

class FormatNotMatchException(Exception):
    '''
    raised while parsing nepalidatetime format
    '''
    pass