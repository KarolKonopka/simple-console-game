import random

class Player:
	def __init__(self, world_size):
		self.__world_size = world_size
		self.__level = 0
		self.__position = random.randint(0, self.__world_size - 1)
		self.__direction = 'right'
	def get_character(self):
		return str(self.__level)
	def get_position(self):
		return self.__position
	def move(self, direction):
		if direction == 'left':
			self.__position -= 1
			if self.__position < 0:
				self.__position = self.__world_size - 1
			self.__direction = 'left'
		if direction == 'right':
			self.__position += 1
			if self.__position > self.__world_size - 1:
				self.__position = 0
			self.__direction = 'right'
	def get_direction(self):
		return self.__direction
