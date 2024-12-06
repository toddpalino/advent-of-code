#!/usr/bin/python3

#fn = "test.txt"
fn = "input.txt"

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

guard_pos = None
guard_vector = (0, -1)

# Find starting position
for i, row in enumerate(grid):
	try:
		guard_pos = (row.index('^'), i)
		break
	except ValueError:
		pass

# Replace the guard's position with a .
grid[guard_pos[1]][guard_pos[0]] = '.'

# Mark the intial position as visited
visited = set()

while True:
	visited.add(guard_pos)

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

print("Visited positions: %d" % (len(visited)))
