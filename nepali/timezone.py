import datetime

class NepaliTimeZone(datetime.tzinfo):
    def utcoffset(self, dt):
        return self.dst(dt) + datetime.timedelta(hours=5, minutes=45)

    def dst(self, dt):
        return datetime.timedelta(0)
    
    def tzname(self,dt):
        return "Asia/Kathmandu"

    def __str__(self):
        return "Asia/Kathmandu"

def get_timezone():
    return datetime.datetime.now(datetime.timezone.utc).astimezone().tzinfo

def now():
    return datetime.datetime.now(get_timezone())

def utc_now():
    return datetime.datetime.now(datetime.timezone.utc)

