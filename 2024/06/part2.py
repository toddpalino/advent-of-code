#!/usr/bin/python3

import time

# This is a brute force approach to part 2 - we just try placing a block in every possible
# position and walk through the entire thing. It's slow, but not incredibly slow and does
# return an answer in under a minute

#fn = "test.txt"
fn = "input.txt"

start_time = time.time()

with open(fn, 'r') as f:
	grid = [list(line.strip()) for line in f]

max_x = len(grid[0])
max_y = len(grid)

right_turn = {
	(0, -1): (1, 0),
	(1, 0): (0, 1),
	(0, 1): (-1, 0),
	(-1, 0): (0, -1)
}

initial_guard_pos = None
initial_guard_vector = (0, -1)
loopers = 0

# Find starting position
for i, row in enumerate(grid):
	try:
		initial_guard_pos = (row.index('^'), i)
		break
	except ValueError:
		pass

# Replace the guard's initial position with a .
grid[initial_guard_pos[1]][initial_guard_pos[0]] = '.'

for x in range(max_x):
	for y in range(max_y):
		if (x, y) != initial_guard_pos and grid[y][x] != '#':
			# Replace the suggested position with a block
			grid[y][x] = '#'
		else:
			continue


		# Instead of tracking visited location, we want to track visited locations AND vector
		guard_pos = initial_guard_pos
		guard_vector = initial_guard_vector
		visited = set()

		while True:
			# Check if we are looping (pos+vector already visited)
			pos_vector = (guard_pos[0], guard_pos[1], guard_vector[0], guard_vector[1])
			if pos_vector in visited:
				loopers += 1
				break
			else:
				visited.add((guard_pos[0], guard_pos[1], guard_vector[0], guard_vector[1]))

			# Check if next step is off grid
			next_pos = (guard_pos[0] + guard_vector[0], guard_pos[1] + guard_vector[1])
			if (0 <= next_pos[0] < max_x) and (0 <= next_pos[1] < max_y):
				pass
			else:
				break

			if grid[next_pos[1]][next_pos[0]] == '.':
				guard_pos = next_pos
			else:
				guard_vector = right_turn[guard_vector]

		# Replace the new block with a .
		grid[y][x] = '.'

print("Potential Loops: %d" % (loopers))

end_time = time.time()
print("Elapsed time: %f" % (end_time - start_time))
