import time
import datetime

print("The epch on this time starts at: " + time.strftime('%c', time.gmtime(0)))

print(f"The current timezone is {time.tzname[0]} with an offset of {time.timezone}")

if time.daylight != 0:
    print("\tDaylight Savings is in effect ")
    print("\tThe DST timezone is " + time.tzname[1])
else:
    print("\t Daylight savings is not in effect")

print("Local time is " + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
print("Local time is " + time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()))

print(datetime.datetime.today())
print(datetime.datetime.now())
print(datetime.datetime.utcnow())