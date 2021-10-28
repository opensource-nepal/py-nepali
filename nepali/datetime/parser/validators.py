'''
validates parsing
'''
import re
from nepali.char import EnglishChar


class NepaliTimeRE(dict):
    
    def __init__(self):
        """Create keys/values.
        Order of execution is important for dependency reasons.
        """
        base = super()
        base.__init__({
            # The " [1-9]" part of the regex is to make %c from ANSI C work
            'd': r"(?P<d>3[0-1]|[1-2]\d|0[1-9]|[1-9]| [1-9])",
            '-d': r"(?P<d>3[0-1]|[1-2]\d|0[1-9]|[1-9]| [1-9])", # same as "d"
            'f': r"(?P<f>[0-9]{1,6})",
            'H': r"(?P<H>2[0-3]|[0-1]\d|\d)",
            '-H': r"(?P<H>2[0-3]|[0-1]\d|\d)",
            'I': r"(?P<I>1[0-2]|0[1-9]|[1-9])",
            '-I': r"(?P<I>1[0-2]|0[1-9]|[1-9])",
            'G': r"(?P<G>\d\d\d\d)",
            'j': r"(?P<j>36[0-6]|3[0-5]\d|[1-2]\d\d|0[1-9]\d|00[1-9]|[1-9]\d|0[1-9]|[1-9])",
            'm': r"(?P<m>1[0-2]|0[1-9]|[1-9])",
            '-m': r"(?P<m>1[0-2]|0[1-9]|[1-9])", # same as "m"
            'M': r"(?P<M>[0-5]\d|\d)",
            '-M': r"(?P<M>[0-5]\d|\d)", # same as "M"
            'S': r"(?P<S>6[0-1]|[0-5]\d|\d)",
            '-S': r"(?P<S>6[0-1]|[0-5]\d|\d)", # same as "S"
            'w': r"(?P<w>[0-6])",

            'y': r"(?P<y>\d\d)",
            'Y': r"(?P<Y>\d\d\d\d)",
            'z': r"(?P<z>[+-]\d\d:?[0-5]\d(:?[0-5]\d(\.\d{1,6})?)?|(?-i:Z))",

            'A': self.__seqToRE(EnglishChar.days, 'A'),
            'a': self.__seqToRE(EnglishChar.days_half, 'a'),
            'B': self.__seqToRE(EnglishChar.months, 'B'),
            'b': self.__seqToRE(EnglishChar.months, 'b'),
            'p': self.__seqToRE(('AM', 'PM',), 'p'),

            '%': '%'
        })
    
    def __seqToRE(self, to_convert, directive):
        """Convert a list to a regex string for matching a directive.
        Want possible matching values to be from longest to shortest.  This
        prevents the possibility of a match occurring for a value that also
        a substring of a larger value that should have matched (e.g., 'abc'
        matching when 'abcdef' should have been the match).
        """
        to_convert = sorted(to_convert, key=len, reverse=True)
        for value in to_convert:
            if value != '':
                break
        else:
            return ''
        regex = '|'.join(re.escape(stuff) for stuff in to_convert)
        regex = '(?P<%s>%s' % (directive, regex)
        return '%s)' % regex

    def pattern(self, format):
        '''
        Handle conversion from format directives to regexes.
        '''
        processed_format = ''
        regex_chars = re.compile(r"([\\.^$*+?\(\){}\[\]|])")
        format = regex_chars.sub(r"\\\1", format)
        whitespace_replacement = re.compile(r'\s+')
        format = whitespace_replacement.sub(r'\\s+', format)
        while '%' in format:
            directive_index = format.index('%')+1
            index_increment = 1
            if format[directive_index] == '-':
                index_increment = 2
            processed_format = "%s%s%s" % (processed_format,
                                            format[:directive_index-1],
                                            self[format[directive_index: directive_index+index_increment]])
            format = format[directive_index+index_increment:]
        return "%s%s" % (processed_format, format)

    def compile(self, format):
        """Return a compiled re object for the format string."""
        return re.compile(self.pattern(format), re.IGNORECASE)
        

def _extract(datetime_str, format):
    '''
    Extracts year, month, day, hour, minute from the given format.
    
    eg.
    INPUT:
    datetime_str="2078-01-12" 
    format="%Y-%m-%d"

    OUTPUT:
    {
        "Y": 2078,
        "m": 1,
        "d": 12,
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