#!/usr/bin/python3

max_x = 1000
max_y = 200
grid = [[0] * max_x for _ in range(max_y)]

with open("input.txt") as f:
	for line in f:
		points = line.strip().split(' -> ')
		a = [int(x) for x in points[0].split(',')]
		for point in points[1:]:
			b = [int(x) for x in point.split(',')]
			if a[0] == b[0]:
				for y in range(min(a[1], b[1]), max(a[1], b[1]) + 1):
					grid[y][a[0]] = 1
			else:
				for x in range(min(a[0], b[0]), max(a[0], b[0]) + 1):
					grid[a[1]][x] = 1
			a = b

# Find the floor
for y in range(max_y - 1, 0, -1):
	try:
		_ = grid[y].index(1)
	except ValueError:
		continue
	grid[y + 2] = [1] * max_x
	break

grains = 0
while True:
	sand = [500, 0]
	while True:
		if grid[sand[1]+1][sand[0]] == 0:
			sand[1] += 1
		elif grid[sand[1]+1][sand[0]-1] == 0:
			sand[1] += 1
			sand[0] -= 1
		elif grid[sand[1]+1][sand[0]+1] == 0:
			sand[1] += 1
			sand[0] += 1
		else:
			break
	grains += 1
	if (sand[0] == 500) and (sand[1] == 0):
		break
	else:
		grid[sand[1]][sand[0]] = -1

print(grains)
