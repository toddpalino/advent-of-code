#!/usr/bin/python3

from itertools import product, combinations, combinations_with_replacement

class Tile:
	def __init__(self, tile_id, grid):
		self.tile_id = tile_id
		self.grid = grid

		gridlen = len(grid)
		left  = [row[0] for row in grid]
		right = [row[-1] for row in grid]
		self.edges = [
			[grid[0], list(reversed(grid[0]))],
			[right, list(reversed(right))],
			[grid[-1], list(reversed(grid[-1]))],
			[left, list(reversed(left))]
		]

	def connections(self, other):
		return [p for p in combinations_with_replacement(product(range(4), range(2)), 2) if self.edges[p[0][0]][p[0][1]] == other.edges[p[1][0]][p[1][1]]]

tiles = {}

with open("test.txt") as f:
	tile_id = None
	tile = []
	for line in f:
		if line.startswith("Tile "):
			tile_id = int(line[5:-2])
		else:
			ln = line.strip()
			if ln == '':
				tiles[tile_id] = Tile(tile_id, tile)
				tile = []
			else:
				tile.append(list(ln))

print(tiles)
for pair in combinations(tiles.values(), 2):
	print("%d-%d: %s" % (pair[0].tile_id, pair[1].tile_id, pair[0].connections(pair[1])))
