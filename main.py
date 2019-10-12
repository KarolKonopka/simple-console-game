from game import Game
import argparse

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='My first Python console game!!!')
	parser.add_argument('-ws', '--world_size', help='Game world size, range: <8, 128>', type=int, default='32')
	args = parser.parse_args()
	world_size = args.world_size
	if world_size < 8 or world_size > 128:
		world_size = 32
	game = Game(world_size)
	game.run()
