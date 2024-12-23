#!/usr/bin/env python

import time
from itertools import combinations
from math import lcm
from planets import tests, planets

# Slightly different approach here, so we need to repeat the simulation code.
# The axes are all independent, which gives us the clue to what we need to look for - repetition in the
# state of an axes. If we find that for all 3, we can get the LCM*2 and that will be when all 3 axes
# repeat at the same time (not just the LCM, verified by testing)

def find_cycle_length(planets):
	# Save the initial position for comparison. Velocities are all zero
	init_pos = [p['position'] for p in planets]

	i = 0
	found = [None, None, None]
	while True:
		i += 1
		# First apply gravity
		for p1, p2 in combinations(planets, 2):
			for axis in range(3):
				if p1['position'][axis] < p2['position'][axis]:
					p1['velocity'][axis] += 1
					p2['velocity'][axis] -= 1
				elif p1['position'][axis] > p2['position'][axis]:
					p1['velocity'][axis] -= 1
					p2['velocity'][axis] += 1

		# Now apply velocity
		for p1 in planets:
			for axis in range(3):
				p1['position'][axis] += p1['velocity'][axis]

		for axis in range(3):
			if all(planet['velocity'][axis] == 0 and planet['position'][axis] == init_pos[p][axis]
			       for p, planet in enumerate(planets)):
				if found[axis] is None:
					found[axis] = i

		if all(axis is not None for axis in found):
			break
	return lcm(*found) * 2

for i, test in enumerate(tests):
	failed = False
	cycle = find_cycle_length(test['planets'])
	if cycle != test['repeat']:
		print(f'Test {i} Failed (expected cycle {test['repeat']}, got {cycle})')
	else:
		print(f'Test {i} passed')

start_time = time.time()

print(f'Planetary cycle repeats at step: {find_cycle_length(planets)}')

end_time = time.time()
print("Elapsed time: %f" % (end_time - start_time))
