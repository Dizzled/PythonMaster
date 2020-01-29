# Create a program that allows a user to choose one of
# up to 9 time zones from a menu. You can choose any
# zones you want from the all_timezones list.
#
# The program will then display the time in that timezone, as
# well as local time and UTC time.
#
# Entering 0 as the choice will quit the program.
#
# Display the dates and times in a format suitable for the
# user of your program to understand, and include the
# timezone name when displaying the chosen time.
import pytz
import datetime
import random

sizeofzone = len(pytz.common_timezones)

# Take random sample set and converted it to a list
randomZone = random.sample(list(pytz.common_timezones),9)

while True:
    # Convert list to Dict with keys
    converted = {i + 1: randomZone[i] for i in range(0, len(randomZone))}
    for i in converted:
        print(f"{i} : {converted[i]}")

    # Convert the user input into an int since the dict is an int and input is string
    userInput = int(input("Please Select one of the Nine Timezones or 0 to quit: "))
    print("*" * 40)
    if userInput == 0:
        break
    timezone = converted.get(userInput)
    tzToDisplay = pytz.timezone(timezone)
    localTime = datetime.datetime.now(tz=tzToDisplay)
    utcTime = datetime.datetime.now()
    # Local Time formatted %A Full Weekday name %x preferred date representation without the time %X Preferred time rep without date
    # %Z time zone name or abbreviation
    print("You Selected {}: Time local {}: Time UTC {}: ".format(timezone, localTime.strftime('%A %x %X %z'), utcTime))
    print("*" * 40)





