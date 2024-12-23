#!/usr/bin/python3

trees = []

#with open("test.txt") as f:
with open("input.txt") as f:
	for line in f:
		trees.append(line.strip())

max_x = len(trees[0])
max_y = len(trees) - 1

prod = 1
increments = ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2))
for incr in increments:
	# Starting position
	x = 0
	y = 0

	hits = 0
	while y < max_y:
		x = (x + incr[0]) % max_x
		y += incr[1]
		if (y <= max_y) and (trees[y][x] == '#'):
			hits += 1

	print(hits)
	prod *= hits

print(prod)
