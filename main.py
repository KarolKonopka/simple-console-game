from game import Game
import argparse

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='My first Python console game!!!')
	parser.add_argument('-ws', '--world_size', help='Game world size', type=int, default='32')
	args = parser.parse_args()
	game = Game(args.world_size)
	game.run()
