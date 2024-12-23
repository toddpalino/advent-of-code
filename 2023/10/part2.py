#!/usr/bin/python3

from collections import deque

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

		# We're going to use this for the flood fill
		self.visited = False

	def replace(self, node):
		self.c = node.c
		self.x = node.x
		self.y = node.y
		self.a = node.a
		self.b = node.b

	def connect(self, field):
		c = self.c
		if c == '.' or c == ' ' or c == 'S':
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


def print_field(field):
	for y in range(len(field)):
		line = ''.join([n.c for n in field[y]])
		print(line)

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
for y in range(max_y):
	for x in range(max_x):
		node = field[y][x]
		if node not in path:
			node.c = '.'
			node.a = None
			node.b = None

# Expand the field by adding a node before and after each real node (2x + 1)
# Added empty nodes will be ' ' so we can distinguish them from original empty nodes
new_field = [[None] * ((2 * max_x) + 1) for y in range((2 * max_y) + 1)]
for y in range(len(field)):
	for x in range(len(field[0])):
		new_field[(2 * y) + 1][(2 * x) + 1] = field[y][x]
for y in range(len(new_field)):
	for x in range(len(new_field[0])):
		if new_field[y][x] is None:
			new_field[y][x] = Node(' ', x, y)

max_x = len(new_field[0])
max_y = len(new_field)

# Fill in the gaps (add horizontal pipes)
for y in range(1, max_y, 2):
	for x in range(2, max_x - 2, 2):
		left = new_field[y][x-1]
		right = new_field[y][x+1]
		if left.c in 'FL-' and right.c in 'J7-':
			node = Node('-', x, y)
			node.a = left
			node.b = right
			new_field[y][x] = node
			if left.a == right:
				left.a = node
			else:
				left.b = node
			if right.a == left:
				right.a = node
			else:
				right.b = node
		else:
			new_field[y][x] = Node(' ', x, y)

# Fill in the gaps (add vertical pipes)
for y in range(2, max_y - 2, 2):
	for x in range(1, max_x):
		if x % 2 == 0:
			new_field[y][x] = Node(' ', x, y)
			continue
		up = new_field[y-1][x]
		down = new_field[y+1][x]
		if up.c in '7F|' and down.c in 'LJ|':
			node = Node('|', x, y)
			node.a = up
			node.b = down
			new_field[y][x] = node
			if up.a == right:
				up.a = node
			else:
				up.b = node
			if down.a == left:
				down.a = node
			else:
				down.b = node
		else:
			new_field[y][x] = Node(' ', x, y)

# Flood fill the outside with ' '
# Note - you can't trust the Node x,y coordinates now. They only applied to the original field
queue = deque([(0, 0)])
start.visited = True
while queue:
	node = queue.popleft()
	for neighbor in ((node[0]-1, node[1]), (node[0]+1, node[1]), (node[0], node[1]-1), (node[0], node[1]+1)):
		if (0 <= neighbor[0] < max_x) and (0 <= neighbor[1] < max_y):
			n = new_field[neighbor[1]][neighbor[0]]
			if (not n.visited) and (n.c in '. '):
				n.c = ' '
				n.visited = True
				queue.append(neighbor)

# Count the remaining '.'
c = 0
for y in range(len(new_field)):
	for x in range(len(new_field[0])):
		if new_field[y][x].c == '.':
			c += 1

print(c)
