import random

class Enemy:
	def __init__(self, player_position, world_size):
		self.__world_size = world_size
		self.__set_position(player_position)
		self.__last_position = None
	def __set_position(self, player_position):
		self.__position = random.randint(0, self.__world_size - 1)
		while self.__position >= player_position - 1 and self.__position <= player_position + 1:
			self.__position = random.randint(0, self.__world_size - 1)
	def get_position(self):
		return self.__position
	def get_character(self):
		return '*'
	def move(self):
		self.__position += random.randint(-1, 1)
		if self.__position >= self.__world_size:
			self.__position = 0
		elif self.__position < 0:
			self.__position = self.__world_size - 1
	def kill(self, player_position):
		self.__last_position = self.__position
		self.__set_position(player_position)
