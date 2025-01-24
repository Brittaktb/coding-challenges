'''
From Flowchart to Python Code

A stopwatch is used to record the duration of an event as a number of seconds. 
Our stopwatch algorithm will convert/format this number of seconds to calculate
and display the matching number of hours, minutes and seconds, knowing that:

1 hour = 3600 seconds
1 minute = 60 seconds
'''

number_sec = 45015
hours = number_sec // 3600
remainder = number_sec  % 3600
minutes = remainder // 60
seconds = remainder % 60

print(f"{number_sec} seconds = {hours} hours, {minutes} minutes, {seconds} seconds." )

print(type(number_sec))
print(type(hours))
print(type(remainder))
print(type(minutes))
print(type(seconds))

