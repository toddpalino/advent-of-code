#!/usr/bin/python3

from collections import deque

def print_grid(grid):
	for row in grid:
		print(''.join(['.' if c is None else '#' for c in row]))

def flood_fill(grid, start, color):
	max_y = len(grid)
	max_x = len(grid[0])

	visited = set([start])
	queue = deque([start])
	grid[start[1]][start[0]] = color
	while queue:
		node = queue.popleft()
		for neighbor in ((node[0]-1, node[1]), (node[0]+1, node[1]), (node[0], node[1]-1), (node[0], node[1]+1)):
			if (0 <= neighbor[0] < max_x) and (0 <= neighbor[1] < max_y):
				if (neighbor not in visited) and (grid[neighbor[1]][neighbor[0]] is None):
					grid[neighbor[1]][neighbor[0]] = color
					visited.add(neighbor)
					queue.append(neighbor)

cubes = {}
x = 0
y = 0

with open("input.txt") as f:
	for line in f:
		parts = line[0:-1].split(' ')
		direction = parts[0]
		dist = int(parts[1])
		color = parts[2][1:-1]

		if direction == 'R':
			for new_x in range(x + 1, x + dist + 1):
				cubes[(new_x, y)] = color
			x += dist
		if direction == 'L':
			for new_x in range(x - 1, x - dist - 1, -1):
				cubes[(new_x, y)] = color
			x -= dist
		if direction == 'U':
			for new_y in range(y + 1, y + dist + 1):
				cubes[(x, new_y)] = color
			y += dist
		if direction == 'D':
			for new_y in range(y - 1, y - dist - 1, -1):
				cubes[(x, new_y)] = color
			y -= dist

# Transform the coordinates to be positive
max_x = max(coord[0] for coord in cubes.keys())
offset_x = abs(min(coord[0] for coord in cubes.keys()))
max_y = max(coord[1] for coord in cubes.keys())
offset_y = abs(min(coord[1] for coord in cubes.keys()))
grid = [[None for _ in range(0, (max_x + offset_x) + 1)] for _ in range(0, (max_y + offset_y) + 1)]

for coord, color in cubes.items():
	grid[abs(coord[1] - max_y)][coord[0] + offset_x] = color

# Find an inside point so we can flood fill
inside = None
for y, row in enumerate(grid):
	if row[0] is not None and row[1] is None:
		inside = (1, y)
		break

flood_fill(grid, inside, '#000000')

# Count pit size
pit_size = 0
for row in grid:
	for c in row:
		if c is not None:
			pit_size +=1

print(pit_size)
