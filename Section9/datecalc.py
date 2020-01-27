import time
import random
# print(time.gmtime(0))
#
# timeHere = time.localtime()
#
# print(timeHere)
# # The underlying time function is a struct that is a tuple that can be called in various ways as shown below
# print("Year: ", timeHere[0], timeHere.tm_year)
# print("Month: ", timeHere[1], timeHere.tm_mon)
# print("Day: ", timeHere[2], timeHere.tm_mday)

input("Press enter to start")

waitTime = random.randint(1, 6)
timer = time.time()
time.sleep(waitTime)

# Amount of time for CPU to process code
time.process_time()
# Amount of time elapsed only going forward no correction for daylight savings
time.monotonic()
# Amount of time elapsed with highest precision good for benchmarking BEST FUNCTION FOR USING THIS
time.perf_counter()

input("press enter to stop")

endTime = time.time()
totalTime = endTime - timer
print("Started @ " + time.strftime("%X", time.localtime(timer)))
print("Ended @ " + time.strftime("%X", time.localtime(endTime)))
print(f"Time Elapsed: {0}", totalTime)