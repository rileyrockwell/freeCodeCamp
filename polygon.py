class Rectangle:
	def __init__(self, width, height):
		self.width = width
		self.height = height

	def __str__(self):
		return f'Rectangle(width={self.width}, height={self.height})'

	def set_width(self, new_width):
		self.width = new_width

	def set_height(self, new_height):
		self.height = new_height

	def get_area(self):
		return self.width * self.height

	def get_perimeter(self):
		return 2 * self.width + 2 * self.height

	def get_diagonal(self):
		return ((self.width ** 2 + self.height ** 2) ** 0.5)

	def get_picture(self):
		for row in range(self.height):
			print("*" * self.width)

		return ""

	def get_amount_inside(self, instance):
		# print(instance)
		# print(instance)

		a = instance.height
		b = instance.width
		
		# print("instance.height:", a)
		# print("instance.width:", b)
		# print(a, b)

		# find the min length of the attributes
		min_side_length = min(a, b)
		# print('min_side_length:', min_side_length)

		# print('self.height (parent class):', self.height)
		# print('self.width (parent class):', self.width)

		# but you pass in the square instance, treating the square 
		# instance as a subset of the rectangle instance

		# take the 'parent side.length' and 'parent side.width'
		# attributes and determine how many times the square
		# instance (defined in the parameter) fits into a rectangle
		# defined by the 'parent side.length' and 'parent side.width'
		c = self.height // min_side_length
		d = self.width // min_side_length

		# print(c, d)
		return c * d


class Square(Rectangle):
	def __init__(self, side):
		self.side = side
		# redefine the attributes from the Rectangle class
		self.width = self.side
		self.height = self.side

	def __str__(self):
		return f'Square(side={self.side})'
		
	def set_side(self, new_side_length):
		self.side = new_side_length
		self.width = self.side
		self.height = self.side


rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)

print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))