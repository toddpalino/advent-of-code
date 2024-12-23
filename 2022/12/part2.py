#!/usr/bin/python3

map = []
with open("input.txt") as f:
	for line in f:
		map.append([{'elevation': ord(c) - 97} for c in line.strip()])

len_x = len(map[0])
len_y = len(map)

goal = None
for i, row in enumerate(map):
	for j, spot in enumerate(row):
		if spot['elevation'] == -14:
			spot['elevation'] = 0
		if spot['elevation'] == -28:
			spot['elevation'] = 25
			goal = (i, j)

for i, row in enumerate(map):
	for j, spot in enumerate(row):
		spot['moves'] = []
		for c in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
			if (0 <= c[0] < len_y) and (0 <= c[1] < len_x) and (0 <= map[c[0]][c[1]]['elevation'] <= spot['elevation'] + 1):
				spot['moves'].append(c)

# Cheat - elevation b only exists in column 1. Therefore, we could only possibly start from an a in columns 0 or 2
starts = set([])
for j in (0, 2):
	for i in range(len_y):
		if map[i][j]['elevation'] == 0:
			starts.add((i, j))

min_steps = 9999999
for start in starts:
	steps = [[None] * len_x for _ in range(len_y)]
	steps[start[0]][start[1]] = 0
	queue = [start]
	while queue:
		spot = queue.pop(0)
		if spot == goal:
			break
		for move in map[spot[0]][spot[1]]['moves']:
			if steps[move[0]][move[1]] is None:
				steps[move[0]][move[1]] = steps[spot[0]][spot[1]] + 1
				queue.append(move)
	min_steps = min(min_steps, steps[goal[0]][goal[1]])

print(min_steps)
