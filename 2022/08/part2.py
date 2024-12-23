#!/usr/bin/python3

forest = []
with open("input.txt") as f:
	for line in f:
		forest.append([int(c) for c in line if c.isdigit()])

max_score = 0

for i in range(1, len(forest) - 1):
	for j in range(1, len(forest[i]) - 1):
		tree = forest[i][j]

		left = 0
		for x in range(j-1, -1, -1):
			left += 1
			if tree <= forest[i][x]:
				break
		right = 0
		for x in range(j+1, len(forest[i])):
			right += 1
			if tree <= forest[i][x]:
				break

		col = [forest[c_i][j] for c_i in range(len(forest))]
		up = 0
		for y in range(i-1, -1, -1):
			up += 1
			if tree <= col[y]:
				break
		down = 0
		for y in range(i+1, len(col)):
			down += 1
			if tree <= col[y]:
				break

		score = left * right * up * down
		if score > max_score:
			max_score = score

print(max_score)
