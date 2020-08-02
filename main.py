import argparse
import numpy as np
from random_walker import Walker

parser = argparse.ArgumentParser(description = "Program that graph a random walker")
parser.add_argument('-w', '--walkers', required = True, type = int, help = "The number of walkers")
parser.add_argument('-s', '--steps', required = True, type = int, help = "The number of steps")
args = parser.parse_args()

def main(walkers,steps):
    colors = ['blue','yellow','red','green','black','gray']
    for walker,color in zip(range(walkers),colors):
        walk = Walker()
        walk.run_walk(steps)
        walk.create_graph(color)
    walk.show_walkers()


if __name__ == "__main__":
    walkers = args.walkers
    steps = args.steps 
    main(walkers, steps)
        