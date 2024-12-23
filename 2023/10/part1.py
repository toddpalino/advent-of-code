#!/usr/bin/python3

class PathError(Exception):
	pass


# Read in first quickly so we know the size of the field
field = []
with open("input.txt") as f:
	for line in f:
		field.append([c for c in line[:-1]])

max_x = len(field[0])
max_y = len(field)

# Now interpret the map and find the start
start = None
for x in range(max_x):
	for y in range(max_y):
		c = field[y][x]
		if c == 'S':
			start = (x, y)
			continue
		if c == '.':
			field[y][x] = None
			continue

		n = (x, y-1)
		s = (x, y+1)
		e = (x+1, y)
		w = (x-1, y)
		node = None

		if c == '|':
			node = (n, s)
		if c == '-':
			node = (w, e)
		if c == 'L':
			node = (n, e)
		if c == 'J':
			node = (n, w)
		if c == '7':
			node = (s, w)
		if c == 'F':
			node = (s, e)

		if (0 <= node[0][0] <= max_x) and (0 <= node[0][1] <= max_y) and (0 <= node[1][0] <= max_x) and (0 <= node[1][1] <= max_y):
			field[y][x] = node
		else:
			field[y][x] = None

# Figure out possible shapes for the start point
shapes = []
x = start[0]
y = start[1]

n = (x, y-1)
s = (x, y+1)
e = (x+1, y)
w = (x-1, y)

try_nodes = [(n, s), (w, e), (n, e), (n, w), (s, w), (s, e)]
for node in try_nodes:
	n1 = node[0]
	n2 = node[1]
	if field[n1[1]][n1[0]] is None or field[n2[1]][n2[0]] is None:
		continue
	n1_l = field[n1[1]][n1[0]][0]
	n1_r = field[n1[1]][n1[0]][1]
	n2_l = field[n2[1]][n2[0]][0]
	n2_r = field[n2[1]][n2[0]][1]
	if (n1_l == start or n1_r == start) and (n2_l == start or n2_r == start):
		shapes.append(node)

start_shape = None
path = None
for s in shapes:
	# Pick a side of the start node to "come" from for starting off - it doesn't matter which
	field[start[1]][start[0]] = s
	path = [s[0], start]
	prev = s[0]

	try:
		while True:
			current = path[-1]
			node = field[current[1]][current[0]]
			next = node[0] if path[-2] == node[1] else node[1]
			if field[next[1]][next[0]] is None:
				raise PathError
			if next == path[0]:
				break
			path.append(next)

		start_shape = s
	except PathError:
		continue

print(start_shape)
print(len(path) // 2)
