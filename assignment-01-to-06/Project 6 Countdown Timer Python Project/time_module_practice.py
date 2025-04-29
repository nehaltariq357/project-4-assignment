

import time

# pause program for the given time
# print("start")
# time.sleep(2)
# print("end afer 2 seconds")

#return the current unix timestamp (seconds since jan 1 1970)
current_time = time.time()
# print("current time stamp:",current_time)

#convert a timestamp to a readable format
#print("current time:",time.ctime())

#You can also use it with a timestamp:

timestamp =  1700000000

# print("Readable time:", time.ctime(timestamp))
#Format the current time nicely.
local_time = time.localtime()
formatted = time.strftime("%y-%m-%d %H:%M:%S", local_time)
# print("Formatted time:", formatted)

import time

start = time.perf_counter()
time.sleep(1.5)  # Simulate a task
end = time.perf_counter()

print("Time taken:", end - start, "seconds")
