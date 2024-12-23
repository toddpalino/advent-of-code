#!/usr/bin/python3

trees = []

#with open("test.txt") as f:
with open("input.txt") as f:
	for line in f:
		trees.append(line.strip())

# Starting position
x = 0
y = 0

max_x = len(trees[0])
max_y = len(trees) - 1

hits = 0
while y < max_y:
	x = (x + 3) % max_x
	y += 1
	if trees[y][x] == '#':
		hits += 1

print(hits)
