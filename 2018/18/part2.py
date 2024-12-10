#!/usr/bin/python3

# For part 1 we didn't need to care about loop detection. Now we do. At some
# point the grid will stabilize either with no changes or a loop. We need to
# detect that point and stop work. We'll try a history of 50 to start.

import time
from collections import deque

#fn = "test.txt"
fn = "input.txt"

iterations = 1000000000
history = 50

def get_new_grid(len_x, len_y):
	return [['.'] * len_x for _ in range(len_y)]

start_time = time.time()

with open(fn, 'r') as f:
	grid = [list(line.strip()) for line in f]
len_x = len(grid[0])
len_y = len(grid)

buf = deque([], maxlen=history)

iter = 0
while iter < iterations:
	new_grid = buf.popleft() if len(buf) == history else get_new_grid(len_x, len_y)

	for x in range(len_x):
		for y in range(len_y):
			count_open = 0
			count_lumber = 0
			count_trees = 0
			for nx in range(x-1, x+2):
				for ny in range(y-1, y+2):
					if (not (x == nx and y == ny)) and (0 <= nx < len_x) and (0 <= ny < len_y):
						loc = grid[ny][nx]
						if loc == '.':
							count_open += 1
						elif loc == '#':
							count_lumber += 1
						else:
							count_trees += 1

			
			loc = grid[y][x]
			if loc == '.' and count_trees >= 3:
				new_grid[y][x] = '|'
			elif loc == '|' and count_lumber >= 3:
				new_grid[y][x] = '#'
			elif loc == '#' and (count_lumber == 0 or count_trees == 0):
				new_grid[y][x] = '.'
			else:
				new_grid[y][x] = loc

	# Check if we have seen the new grid recently
	loop_start = 0
	loop_len = None
	for old_grid in buf:
		if old_grid == new_grid:
			# Found a loop
			print("Found loop after %d iterations" % (iter))
			loop_len = len(buf) - loop_start
			break
		loop_start += 1

	if loop_len is not None:
		# Pop items off the left of the buffer so we just have the loop in there
		# Make sure our current state is at the end of the buffer
		for _ in range(loop_start):
			buf.popleft()
		buf.rotate(-1)

		# Every loop_len iterations puts the buffer in the state it's in
		# We need to rotate it for the remainder after all the full loops
		buf.rotate(-((iterations - iter - 1) % loop_len))
		iter = iterations
	else:
		buf.append(new_grid)
		grid = new_grid
		iter += 1

grid = buf.pop()
total_trees = sum(1 for x in range(len_x) for y in range(len_y) if grid[y][x] == '|')
total_lumber = sum(1 for x in range(len_x) for y in range(len_y) if grid[y][x] == '#')

print("Total resource value: %d" % (total_trees * total_lumber))

end_time = time.time()
print("Elapsed time: %f" % (end_time - start_time))
