# Write a small program to display information on the
# four clocks whose functions we have just looked at:
# i.e. time(), perf_counter, monotonic() and process_time().
#
# Use the documentation for the get_clock_info() function
# to work out how to call it for each of the clocks.
import time

performanceTime = time.perf_counter()
print(f"Performance Time: {performanceTime}")
monotonicTime = time.monotonic()
print(f"Monotonic Time: {monotonicTime}")
CPUTime = time.process_time()
print(f"CPUTime: {CPUTime}")
currentGMT = time.time()
GMT = time.localtime(currentGMT)
print(f"Current GMT: {GMT.tm_hour}")

print(time.get_clock_info('time'))
print(time.get_clock_info('monotonic'))
print(time.get_clock_info('process_time'))
print(time.get_clock_info('perf_counter'))
