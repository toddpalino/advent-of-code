#!/usr/bin/env python3

def max_with_none(l):
	return max([item for item in l if item is not None])


with open('input', 'r') as f:
	coords = [line.strip().split(", ") for line in f]

max_size = 500
space = [0] * len(coords)
edges = set()

for x in range(max_size):
	for y in range(max_size):
		distances = [abs(x - int(coord[0])) + abs(y - int(coord[1])) for coord in coords]
		min_distance = min(distances)
		if distances.count(min_distance) == 1:
			closest = distances.index(min_distance)
			space[closest] = space[closest] + 1

			# Mark anything along the edges
			if x == 0 or x == max_size-1 or y == 0 or y == max_size-1:
				edges.add(closest)

for i in range(len(space)):
	if i in edges:
		space[i] = None

largest_space = space.index(max_with_none(space))
print("{}: {}".format(largest_space, space[largest_space]))
