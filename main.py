import keyboard
import random
import os
import time
import argparse

class Player:
	def __init__(self, world_size):
		self.__world_size = world_size
		self.__level = 0
		self.__position = random.randint(0, self.__world_size - 1)
	def get_character(self):
		return str(self.__level)
	def get_position(self):
		return self.__position
	def move(self, direction):
		if direction == 'left':
			self.__position -= 1
			if self.__position < 0:
				self.__position = self.__world_size - 1
		if direction == 'right':
			self.__position += 1
			if self.__position > self.__world_size - 1:
				self.__position = 0

class Game:
	def __init__(self, world_size):
		self.__world_size = world_size
		self.__player = Player(self.__world_size)
		self.__floor = ''.join('_' for i in range(self.__world_size))
		self.__last_world = None
	def run(self):
		while True:
			if keyboard.is_pressed('q'):
				print("quit_game")
				break
			if keyboard.is_pressed('a'):
				self.__player.move('left')
			elif keyboard.is_pressed('d'):
				self.__player.move('right')
			self.__print_world()
	def __clear_terminal(self):
   		os.system('cls' if os.name == 'nt' else 'clear')
	def __print_world(self):
		floor_list = list(self.__floor)
		floor_list[self.__player.get_position()] = self.__player.get_character()
		world = ' '.join(floor_list)
		if world != self.__last_world:
			self.__clear_terminal()
			print(world)
		self.__last_world = world

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='My first Python console game!!!')
	parser.add_argument('-ws', '--world_size', help='Game world size', type=int, default='16')
	args = parser.parse_args()
	game = Game(args.world_size)
	game.run()
