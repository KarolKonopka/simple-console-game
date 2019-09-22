class Bullet:
	def __init__(self, direction, position):
		self.__direction = direction
		self.__position = position
	def update(self):
		if self.__direction == 'left':
			self.__position -= 1
		elif self.__direction == 'right':
			self.__position += 1
	def get_position(self):
		return self.__position
	def get_character(self):
		return '~'
