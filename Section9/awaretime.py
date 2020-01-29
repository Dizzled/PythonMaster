import datetime
import pytz

localTime = datetime.datetime.now()
utcTime = datetime.datetime.utcnow()
# Naive doesn't contain timezone information
print("Naive local time {}".format(localTime))
print("Naive UTC {}".format(utcTime))

# Better to convert UTC time to local time and not try and store local time
# This is done below with the .astimezone
# It's difficult to convert local back to UTC and is error prone
#
awareLocalTime = pytz.utc.localize(utcTime).astimezone()
awareUTCTime = pytz.utc.localize(utcTime)

print("Aware local time {}, time zone {}".format(awareLocalTime, awareLocalTime.tzinfo))
print("Aware UTC {}, time zone {}".format(awareUTCTime, awareUTCTime.tzinfo))

