from datetime import datetime
#import tzlocal  # $ pip install tzlocal
import pytz
from tzlocal import get_localzone


local_tz = get_localzone()
print("cur system local zone:%s" % local_tz)


datetime1 = datetime(2011, 1, 3, 8, 19,25)
print("defaultdatetime1's value : %s" % datetime1)
print("defaultdatetime1's type : %s" % type(datetime1))
print("defaultdatetime1's zone : %s" % datetime1.tzname())
print("defaultdatetime1's timestamp: %s" % datetime1.strftime("%s"))

print("")
print("")
print("")


print("init datetime zone to Asia/Shanghai")
shanghaidatetime1 =  pytz.timezone('Asia/Shanghai').localize(datetime(2011, 1, 3, 8, 19,25))
print("shanghaidatetime1's value : %s" % shanghaidatetime1)
print("shanghaidatetime1's type : %s" % type(shanghaidatetime1))
print("shanghaidatetime1's zone : %s" % shanghaidatetime1.tzname())
print("shanghaidatetime1's timestamp: %s" % shanghaidatetime1.strftime("%s"))

print("")
print("")
print("")


print("change datetime to US/Eastern")
local_tz = pytz.timezone('US/Eastern')
#usEasterndatetime1 = datetime1.astimezone(local_tz) 
usEasterndatetime1 = shanghaidatetime1.astimezone(local_tz)
print("usEasterndatetime1's value : %s" % usEasterndatetime1)
print("usEasterndatetime1's type : %s" % type(usEasterndatetime1))
print("usEasterndatetime1's zone : %s" % usEasterndatetime1.tzname())
print("usEasterndatetime1's timestamp: %s" % usEasterndatetime1.strftime("%s"))


print("")
print("")
print("")

print("change datetime to UTC")
utcdatetime1 = usEasterndatetime1.astimezone(pytz.utc)
print("utcdatetime1's value: %s" % utcdatetime1)
print("utcdatetime1's type: %s" % type(utcdatetime1))
print("utcdatetime1's zone: %s" % utcdatetime1.tzname())
print("utcdatetime1's timestamp: %s" % utcdatetime1.strftime("%s"))

