# import time module
import time
# define func
def countdown (t): # taking parameter for seconds
    while t: # This means “as long as t is not 0”, keep looping.
        min,sec = divmod(t,60) # divide t by 60 
        timer = "{:02d}:{:02d}".format(min,sec) # add 0 digits 
        print(timer,end="\r")# print time, end='\r' makes it overwrite the previous line, instead of printing a new line every second.
        time.sleep(1) # pause for 1 second
        t -=1 # decreasing seconds on every loop
    print("Time is up")
t = int(input("Enter the time in seconds: "))

countdown(t)