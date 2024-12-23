#!/usr/bin/python3

map = []
with open("input.txt") as f:
	for line in f:
		map.append([{'elevation': ord(c) - 97} for c in line.strip()])

len_x = len(map[0])
len_y = len(map)

start = None
goal = None
for i, row in enumerate(map):
	for j, spot in enumerate(row):
		spot['steps'] = None
		if spot['elevation'] == -14:
			spot['elevation'] = 0
			start = (i, j)
			spot['steps'] = 0
		if spot['elevation'] == -28:
			spot['elevation'] = 25
			goal = (i, j)

for i, row in enumerate(map):
	for j, spot in enumerate(row):
		spot['moves'] = []
		for c in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
			if (0 <= c[0] < len_y) and (0 <= c[1] < len_x) and (0 <= map[c[0]][c[1]]['elevation'] <= spot['elevation'] + 1):
				spot['moves'].append(c)

queue = [start]
while queue:
	spot = queue.pop(0)
	if spot == goal:
		break
	for move in map[spot[0]][spot[1]]['moves']:
		new_spot = map[move[0]][move[1]]
		if new_spot['steps'] is None:
			new_spot['steps'] = map[spot[0]][spot[1]]['steps'] + 1
			queue.append(move)

print(map[goal[0]][goal[1]]['steps'])
