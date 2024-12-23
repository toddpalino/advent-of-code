#!/usr/bin/python3

forest = []
with open("input.txt") as f:
	for line in f:
		forest.append([int(c) for c in line if c.isdigit()])

# Exterior trees
visible_trees = (len(forest) * 2) + (len(forest[0]) * 2) - 4

for i in range(1, len(forest) - 1):
	for j in range(1, len(forest[i]) - 1):
		tree = forest[i][j]
		if tree > max(forest[i][:j]) or tree > max(forest[i][j+1:]):
			visible_trees += 1
			continue

		col = [forest[c_i][j] for c_i in range(len(forest))]
		if tree > max(col[:i]) or tree > max(col[i+1:]):
			visible_trees += 1
			continue

print(visible_trees)
