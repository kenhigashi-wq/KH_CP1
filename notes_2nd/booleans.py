# KH Booleans Notes

over = False

print(over)

name = "E"

print(bool(name))
print(name.isdecimal()) # returns false if not decimal and so on for the rest
print(name.isnumeric())
print(name.isalpha())
print(name.isupper())
print(name.islower())

import time
import datetime as d

current_time = time.time()
readable_time = time.ctime(current_time)

print(f"Time in seconds sice January 1, 1970(epoch time): {current_time}")
print(f"Current Time: {readable_time}")

now = d.datetime.today()
hour = now.strftime("%H")
# Month = %m or ( %b, %B )
# day = %d
#year = %Y, %y
#hour = %h
#minutes = %M
#seconds = %S

print(f"Current time: {now} ")
print(f"Hour: {hour}")

print(f"My hour variable is a string: {isinstance(hour, str)}")
print(f"My hour variable is a integer: {isinstance(hour, int)}")
print(f"My hour variable is a float: {isinstance(hour, float)}")