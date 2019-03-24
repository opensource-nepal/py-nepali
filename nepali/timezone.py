import datetime

class NepaliTimeZone(datetime.tzinfo):
    def utcoffset(self, dt):
        return self.dst(dt) + datetime.timedelta(hours=5, minutes=45)

    def dst(self, dt):
        return datetime.timedelta(0)
    
    def tzname(self,dt):
        return "Asia/Kathmandu"