def add_time(start, duration, starting_day=None):
	# Convert 12-hour time to minutes
	def time_to_minutes(time):
		parts = time.split()
		time_parts = parts[0].split(':')
		hours = int(time_parts[0])
		minutes = int(time_parts[1])
		if parts[1] == 'PM' and hours != 12:
			hours += 12
		if parts[1] == 'AM' and hours == 12:
			hours = 0
		return hours * 60 + minutes

	# Convert minutes to 12-hour time
	def minutes_to_time(minutes):
		hours = (minutes // 60) % 24
		minutes = minutes % 60
		period = 'AM' if hours < 12 else 'PM'
		hours = hours % 12
		if hours == 0:
			hours = 12
		return f"{hours}:{minutes:02d} {period}"

	# Get the day of the week
	def get_day_of_week(day, days_later):
		days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
		day_index = days_of_week.index(day.capitalize())
		return days_of_week[(day_index + days_later) % 7]

	# Convert start time to minutes
	start_minutes = time_to_minutes(start)
	
	# Convert duration to minutes
	duration_parts = duration.split(':')
	duration_minutes = int(duration_parts[0]) * 60 + int(duration_parts[1])

	# Add start time and duration
	new_minutes = start_minutes + duration_minutes
	
	# Calculate days later
	days_later = new_minutes // (24 * 60)
	
	# Get the new time in minutes
	new_minutes = new_minutes % (24 * 60)

	# Convert new time back to 12-hour format
	new_time = minutes_to_time(new_minutes)

	# Prepare the result string
	result = new_time
	if starting_day:
		new_day = get_day_of_week(starting_day, days_later)
		result += f", {new_day}"
	if days_later == 1:
		result += " (next day)"
	elif days_later > 1:
		result += f" ({days_later} days later)"

	return result


if __name__ == "__main__":
	print(add_time('3:00 PM', '3:10'))  # Returns: 6:10 PM
	print(add_time('11:30 AM', '2:32', 'Monday'))  # Returns: 2:02 PM, Monday
	print(add_time('11:43 AM', '00:20'))  # Returns: 12:03 PM
	print(add_time('10:10 PM', '3:30'))  # Returns: 1:40 AM (next day)
	print(add_time('11:43 PM', '24:20', 'tueSday'))  # Returns: 12:03 AM, Thursday (2 days later)
	print(add_time('6:30 PM', '205:12'))  # Returns: 7:42 AM (9 days later)