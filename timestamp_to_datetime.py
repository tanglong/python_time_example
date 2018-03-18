from datetime import datetime
import tzlocal  # $ pip install tzlocal

unix_timestamp = float("1284101485")
print(unix_timestamp)
local_timezone = tzlocal.get_localzone() # get pytz timezone
print(local_timezone)
local_time = datetime.fromtimestamp(unix_timestamp, local_timezone)
print(local_time)
