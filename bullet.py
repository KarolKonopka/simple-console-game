class Bullet:
	def __init__(self, direction, position):
		self.__direction = direction
		self.__position = position
		self.__destroyed = False
	def update(self):
		if self.__direction == 'left':
			self.__position -= 1
		elif self.__direction == 'right':
			self.__position += 1
	def get_position(self):
		return self.__position
	def get_character(self):
		return '~'
	def set_destroyed(self):
		self.__destroyed = True
	def is_destroyed(self):
		return self.__destroyed
