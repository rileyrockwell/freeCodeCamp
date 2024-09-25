from typing import *

def add_time(initial_time: str, additional_duration: str, weekday: str):
	"""
	start: str [int:int AM/PM]
	duration: str [int:int]
	starting day: str ['weekday'] | optional
	
	notes:
	hour: any whole number
	00 <=  minutes <= 59
	(next day) v. (n days later)
	"""

	# obtain the initial time from the parameter and convert to an integer in 24-hour format
	seperate_the_bullshit = initial_time.split(' ')
	time = seperate_the_bullshit[0]
	am_pm = seperate_the_bullshit[1]

	# obtain initial hour from initial time
	initial_hour = int(time.split(':')[0])

	# obtain initial minutes from initial time
	initial_minutes = int(time.split(':')[1])

	# convert to 24-hour format
	if am_pm == 'AM' and initial_hour == 12:
		initial_hour = 0

	elif am_pm == 'PM' and initial_hour != 12:
		initial_hour += 12

	# return initial_hour, initial_minutes, am_pm
	return initial_hour


	# GET IN THE HABIT OF COMMENTING CODE W/ ABSOLUTE CLARITY.
	additional_duration_hour = int(additional_duration.split(':')[0])
	additional_duration_minutes = int(additional_duration.split(':')[1])

	remainder_hour = (initial_minutes + additional_duration_minutes) // 60
	remainder_minutes = (initial_minutes + additional_duration_minutes) % 60

	



	print(additional_duration_hour)
	print(additional_duration_minutes)
	print(remainder_hour)
	print(remainder_minutes)

	print('NEXT')


print(add_time('12:00 AM', '205:12', ''))
print(add_time('12:01 PM', '205:12', ''))
print(add_time('1:00 AM', '00:01', ''))
print(add_time('1:01 PM', '00:01', ''))

"""
add_time('3:00 PM', '3:10')
# Returns: 6:10 PM

add_time('11:30 AM', '2:32', 'Monday')
# Returns: 2:02 PM, Monday

add_time('11:43 AM', '00:20')
# Returns: 12:03 PM

add_time('10:10 PM', '3:30')
# Returns: 1:40 AM (next day)

add_time('11:43 PM', '24:20', 'tueSday')
# Returns: 12:03 AM, Thursday (2 days later)

add_time('6:30 PM', '205:12')
# Returns: 7:42 AM (9 days later)
"""
