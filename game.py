from player import Player
from bullet import Bullet
from enemy import Enemy
import keyboard
import time
import os

class Game:
	def __init__(self, world_size):
		self.__world_size = world_size
		self.__player = Player(self.__world_size)
		self.__bullets = []
		self.__enemy = Enemy(self.__player.get_position(), self.__world_size)
		self.__floor = ''.join('_' for i in range(self.__world_size))
		self.__last_world = None
		self.__last_bullet_time = 0
	def run(self):
		while True:
			if keyboard.is_pressed('q'):
				print("quit_game")
				break
			if keyboard.is_pressed('a'):
				self.__player.move('left')
			elif keyboard.is_pressed('d'):
				self.__player.move('right')
			if keyboard.is_pressed('space'):
				if len(self.__bullets) < 4:
					if self.__last_bullet_time > 1:
						self.__last_bullet_time = 0
						self.__bullets.append(Bullet(self.__player.get_direction(), self.__player.get_position()))
			self.__check_collisions()
			self.__enemy.move()
			self.__update_bullets()
			self.__print_world()
			time.sleep(0.05)
	def __clear_terminal(self):
   		os.system('cls' if os.name == 'nt' else 'clear')
	def __print_world(self):
		floor_list = list(self.__floor)
		for i in self.__bullets:
			floor_list[i.get_position()] = i.get_character()
		floor_list[self.__enemy.get_position()] = self.__enemy.get_character()
		floor_list[self.__player.get_position()] = self.__player.get_character()
		world = ' '.join(floor_list)
		if world != self.__last_world:
			self.__clear_terminal()
			print(world)
		self.__last_world = world
	def __update_bullets(self):
		self.__last_bullet_time += 1
		for bullet in self.__bullets:
			bullet.update()
		self.__bullets = list(filter(lambda bullet: bullet.get_position() >= 0 and bullet.get_position() < self.__world_size, self.__bullets))
	def __check_collisions(self):
		for bullet in self.__bullets:
			if bullet.get_position() == self.__enemy.get_position():
				self.__player.level_up()
				bullet.set_destroyed()
				self.__enemy.kill(self.__player.get_position())
		self.__bullets = list(filter(lambda bullet: not bullet.is_destroyed(), self.__bullets))
		if self.__enemy.get_position() == self.__player.get_position():
			self.__player.kill()
			self.__enemy.kill(self.__player.get_position())


