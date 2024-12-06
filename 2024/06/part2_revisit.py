#!/usr/bin/python3

import time

# This was an attempt to optimize part 2 by only placing blocks along the guard's path (and not testing
# every possible position). It's significantly faster than the original attempt, but it still takes a
# few seconds.

# A couple exceptions to use for indicating end states
class LoopingError(Exception):
	pass
class OffGridError(Exception):
	pass


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


def do_turn(pos, vector, visited):
	# Check if next step is off grid
	next_pos = (pos[0] + vector[0], pos[1] + vector[1])
	if not ((0 <= next_pos[0] < max_x) and (0 <= next_pos[1] < max_y)):
		raise OffGridError()

	# Calculate next guard position and vector
	if grid[next_pos[1]][next_pos[0]] == '.':
		r_pos = next_pos
		r_vector = vector
	else:
		r_pos = pos
		r_vector = right_turn[vector]

	# Check if we are looping (next pos+vector already visited)
	if (r_pos, r_vector) in visited:
		raise LoopingError()

	return r_pos, r_vector


guard_pos = None
guard_vector = (0, -1)
loopers = 0

# Find starting position
for i, row in enumerate(grid):
	try:
		guard_pos = (row.index('^'), i)
		break
	except ValueError:
		pass

# Replace the guard's initial position with a .
grid[guard_pos[1]][guard_pos[0]] = '.'

# Go through once and establish a path
path = []
visited = set()
while True:
	pos_vector = (guard_pos, guard_vector)
	path.append(pos_vector)
	visited.add(pos_vector)
	try:
		guard_pos, guard_vector = do_turn(guard_pos, guard_vector, visited)
	except OffGridError:
		break

# We need to track which new block positions we have already tested
tested = set()

# Try placing a new block at every step in the path and see what happens
for i in range(len(path) - 1):
	guard_pos = path[i][0]
	guard_vector = path[i][1]
	block_pos = (guard_pos[0] + guard_vector[0], guard_pos[1] + guard_vector[1])

	# If we already tried this position, skip it
	if block_pos in tested:
		continue

	# If there is a block in front of the guard already, skip this one
	if grid[block_pos[1]][block_pos[0]] == '#':
		continue

	# If the next step is the initial guard position, skip this one
	if block_pos[0] == path[0][0] and block_pos[1] == path[0][1]:
		continue

	# Everything up to this point in the path is visited.
	visited = set(path[0:i])

	# Replace the space in front of the guard with a block
	grid[block_pos[1]][block_pos[0]] = '#'
	tested.add(block_pos)

	# Continue the path from this point
	while True:
		visited.add((guard_pos, guard_vector))
		try:
			guard_pos, guard_vector = do_turn(guard_pos, guard_vector, visited)
		except OffGridError:
			break
		except LoopingError:
			loopers += 1
			break

	# Fix the space we put the new block in
	grid[block_pos[1]][block_pos[0]] = '.'

print("Potential Loops: %d" % (loopers))

end_time = time.time()
print("Elapsed time: %f" % (end_time - start_time))
