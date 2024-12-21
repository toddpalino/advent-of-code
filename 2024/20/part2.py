#!/usr/bin/env python

import time
from itertools import combinations
from pathfinder import find_location, PathFinder

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
# Savings for a cheat is the difference between the scores on either side minus the length of the cheat
path = pf.get_path(end)
num_cheats = 0
max_cheat = 20
min_savings = 100
for p1, p2 in combinations(path, 2):
	md = abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
	if md > max_cheat or (abs(pf.get_score(p1) - pf.get_score(p2)) - md) < min_savings:
		# Cheat path must be less than 20 and save at least min_savings
		continue
	num_cheats += 1

# Sum up all the cheats that save at least 100
print(f"Number of cheats that save at least {min_savings}: {num_cheats}")

end_time = time.time()
print("Elapsed time: %f" % (end_time - start_time))
