#!/usr/bin/env python

import time
from collections import Counter
from itertools import product
from aoc.utils.pathfinder import find_location, PathFinder

#fn = "test.txt"
fn = "input.txt"

start_time = time.time()

with open(fn, 'r') as f:
	grid = [list(line.strip()) for line in f]
start = find_location(grid, 'S')
end = find_location(grid, 'E')

# Start with finding the fastest path
pf = PathFinder(grid, start)
pf.run()

# Find all possible cheat locations and calculate the savings
# Savings for a cheat is the difference between the scores on either side minus 2 to go through it
cheats = Counter()
for x, y in product(range(1, len(grid[0])-1), range(1, len(grid)-1)):
	if grid[y][x] != '#':
		continue
	if grid[y+1][x] == grid[y-1][x] == '.':
		cheats[abs(pf.get_score((x, y+1)) - pf.get_score((x, y-1))) - 2] += 1
	elif grid[y][x+1] == grid[y][x-1] == '.':
		cheats[abs(pf.get_score((x+1, y)) - pf.get_score((x-1, y))) - 2] += 1

# Sum up all the cheats that save at least 100
num_cheats = sum(cheats[x] for x in cheats if x >= 100)
print(f"Number of cheats that save at least 100: {num_cheats}")

end_time = time.time()
print("Elapsed time: %f" % (end_time - start_time))
