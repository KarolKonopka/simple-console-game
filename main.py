import keyboard
import random
import os
import time
import argparse

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

class Game:
	def __init__(self, world_size):
		self.__world_size = world_size
		self.__player = Player(self.__world_size)
		self.__bullets = []
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
			elif keyboard.is_pressed('space'):
				self.__bullets.append(Bullet(self.__player.get_direction(), self.__player.get_position()))
			self.__update_bullets()
			self.__print_world()
			time.sleep(0.05)
	def __clear_terminal(self):
   		os.system('cls' if os.name == 'nt' else 'clear')
	def __print_world(self):
		floor_list = list(self.__floor)
		floor_list[self.__player.get_position()] = self.__player.get_character()
		for i in self.__bullets:
			floor_list[i.get_position()] = i.get_character()
		world = ' '.join(floor_list)
		if world != self.__last_world:
			self.__clear_terminal()
			print(world)
		self.__last_world = world
	def __update_bullets(self):
		for bullet in self.__bullets:
			bullet.update()
		self.__bullets = list(filter(lambda bullet: bullet.get_position() >= 0 and bullet.get_position() < self.__world_size, self.__bullets))


if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='My first Python console game!!!')
	parser.add_argument('-ws', '--world_size', help='Game world size', type=int, default='32')
	args = parser.parse_args()
	game = Game(args.world_size)
	game.run()
