#!/usr/bin/env python

import time
from aoc.utils.pathfinder import find_location, PathFinder

def points_within_distance(x, y, r):
	for dist in range(2, r + 1):
		for offset in range(dist):
			inverse_offset = dist - offset # Inverse offset
			yield (x + offset, y + inverse_offset), dist
			yield (x + inverse_offset, y - offset), dist
			yield (x - offset, y - inverse_offset), dist
			yield (x - inverse_offset, y + offset), dist


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

# Find all possible cheat locations and count them if the savings is less than 100
# Savings for a cheat is the difference between the scores on either side minus the length of the cheat
num_cheats = 0
max_cheat = 20
min_savings = 100

path = pf.get_path(end)
scores = pf.scores
remaining = set(path)
for p1 in path:
	remaining.remove(p1)
	for p2, md in points_within_distance(*p1, max_cheat):
		if p2 in remaining and (scores[p2] - scores[p1] - md >= min_savings):
			# Cheat path must be less than 20 and save at least min_savings
			num_cheats += 1

# Sum up all the cheats that save at least 100
print(f"Number of cheats that save at least {min_savings}: {num_cheats}")

end_time = time.time()
print("Elapsed time: %f" % (end_time - start_time))
