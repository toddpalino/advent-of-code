#!/usr/bin/python3

class PathError(Exception):
	pass

class Node:
	def __init__(self, c, x, y):
		self.c = c
		self.x = x
		self.y = y

		# NOTE: a and b will not be consistent - they're just 2 connections
		self.a = None
		self.b = None

	def replace(self, node):
		self.c = node.c
		self.x = node.x
		self.y = node.y
		self.a = node.a
		self.b = node.b

	def connect(self, field):
		c = self.c
		if c == '.' or c == 'S':
			return

		node = None
		n1_x = None
		n1_y = None
		n2_x = None
		n2_y = None
		if c == '|':
			n1_x = self.x
			n1_y = self.y - 1
			n2_x = self.x
			n2_y = self.y + 1
		if c == '-':
			n1_x = self.x - 1
			n1_y = self.y
			n2_x = self.x + 1
			n2_y = self.y
		if c == 'L':
			n1_x = self.x
			n1_y = self.y - 1
			n2_x = self.x + 1
			n2_y = self.y
		if c == 'J':
			n1_x = self.x
			n1_y = self.y - 1
			n2_x = self.x - 1
			n2_y = self.y
		if c == '7':
			n1_x = self.x
			n1_y = self.y + 1
			n2_x = self.x - 1
			n2_y = self.y
		if c == 'F':
			n1_x = self.x
			n1_y = self.y + 1
			n2_x = self.x + 1
			n2_y = self.y

		max_x = len(field[0])
		max_y = len(field)
		if (0 <= n1_x < max_x) and (0 <= n1_y < max_y) and (0 <= n2_x < max_x) and (0 <= n2_y < max_y):
			self.a = field[n1_y][n1_x]
			self.b = field[n2_y][n2_x]


# Read in first quickly so we know the size of the field
field = []
with open("input.txt") as f:
	y = 0
	for line in f:
		field.append([Node(line[x], x, y) for x in range(len(line) - 1)])
		y += 1

max_x = len(field[0])
max_y = y

# Now connect the map and find the start
orig_start = None
for x in range(max_x):
	for y in range(max_y):
		node = field[y][x]
		if node.c == 'S':
			orig_start = node
			continue
		if node.c == '.':
			continue
		node.connect(field)

# Figure out possible shapes for the start point
starts = []
for shape in ('|', '-', 'L', 'J', '7', 'F'):
	node = Node(shape, orig_start.x, orig_start.y)
	node.connect(field)
	a = node.a
	b = node.b
	if a is not None and (a.a == orig_start or a.b == orig_start) and (b.a == orig_start or b.b == orig_start):
		starts.append(node)

path = None
for start in starts:
	orig_start.replace(start)

	# Pick a side of the start node to "come" from for starting off - it doesn't matter which
	path = [orig_start.a, orig_start]

	try:
		while True:
			current = path[-1]
			next = current.a if path[-2] == current.b else current.b
			if next is None:
				raise PathError
			if next == path[0]:
				break
			path.append(next)
	except PathError:
		continue

# Get rid of all the junk pipe
for x in range(max_x):
	for y in range(max_y):
		node = field[y][x]
		if node not in path:
			node.c = '.'
			node.a = None
			node.b = None

# Expand the field by adding a node before and after each real node (2x + 1)

print(len(path) // 2)
