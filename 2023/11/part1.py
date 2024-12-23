#!/usr/bin/python3

from itertools import combinations
class Galaxy:
	def __init__(self, galaxy_id, x, y):
		self._id = galaxy_id
		self.x = x
		self.y = y


with open("input.txt") as f:
	lines = f.readlines()

max_y = len(lines)
max_x = len(lines[0]) - 1

# True if the row or col is empty
rows = [True] * max_y
cols = [True] * max_x

galaxies = []
for y in range(max_y):
	for x in range(max_x):
		if lines[y][x] == '#':
			galaxies.append(Galaxy(len(galaxies), x, y))
			rows[y] = False
			cols[x] = False

for galaxy in galaxies:
	galaxy.x += cols[0:galaxy.x].count(True)
	galaxy.y += rows[0:galaxy.y].count(True)

distances = 0
for pair in combinations(range(len(galaxies)), 2):
	g1 = galaxies[pair[0]]
	g2 = galaxies[pair[1]]
	distances += abs(g1.x - g2.x) + abs(g1.y - g2.y)

print(distances)
