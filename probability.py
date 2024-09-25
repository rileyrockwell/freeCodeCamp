import copy
import random

class Hat:
	def __init__(self, **kwargs):
		self.contents = []

		for key, value in kwargs.items():
			setattr(self, key, value)

			for number_of_balls in range(value):
				self.contents.append(key)


	def draw(self, number_to_draw):
		"""
		remove balls at random from contents
		and return those balls as a list of string

		the balls should not go back into the hat during the draw, 
		similar to an urn experiment without replacement.

		if the number of balls to draw exceeds the available quantity, 
		return all of the balls.
		"""

		# determine the length of the list of elements

		# if the number of balls to draw exceeds the available quantity, return all of the balls.
		if number_to_draw > len(self.contents):
			return self.contents

		# remove the ith element (generated randomly) from the list based on parameter value ('number to draw')
		for ith_removed_ball in range(number_to_draw):
			length = len(self.contents)

			# generate a random index in the list, for each iteration
			random_index = random.randint(0, length - 1)

			# remove the ith element in the list, based on the value of 'random index'
			del self.contents[random_index]

		return self.contents


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
	# generate a copy of the original list of balls to be selected
	total_balls = hat.contents

	# convert num_balls_drawn to a list, from the dictionary passed in in the parameter
	


hat = Hat(red=0, orange=1, yellow=2)
print(hat)
print(hat.contents)
hat = Hat(red=0, orange=1, yellow=2, green=3, blue=4, purple=5)
print(hat)
print(hat.contents)