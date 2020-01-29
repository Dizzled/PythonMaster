import pytz #Timezone library
import datetime

country = "Europe/Moscow"

tzToDisplay = pytz.timezone(country)
localTime = datetime.datetime.now(tz=tzToDisplay)
print(f"The time in {country} is {localTime}")
print(f"UTC is {datetime.datetime.now()}")

for x in pytz.all_timezones:
    print(x)

for x in sorted(pytz.country_names):
    print(x + ": " + pytz.country_names[x])

#Using the get command to prevent the error for none during iteration for BV
for x in sorted(pytz.country_names):
    print(f"{x}: {pytz.country_names[x]}: {pytz.country_timezones.get(x)}")

# Keep in mind converting from UTC time to local time is easy, but converting it back from local to UTC is hard


