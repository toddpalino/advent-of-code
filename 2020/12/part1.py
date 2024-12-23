#!/usr/bin/python3

# Degree constants
NORTH = 0
EAST = 90
SOUTH = 180
WEST = 270

# Convert an op (N, S, E, W) to a direction
op_to_face = {
	'N': NORTH,
	'S': SOUTH,
	'E': EAST,
	'W': WEST
}

movement = {
	NORTH: (0, 1),
	SOUTH: (0, -1),
	EAST:  (1, 0),
	WEST:  (-1, 0)
}

# We're using cartesian coordinates, so start at 0, facing east
x = 0
y = 0
face = EAST

#with open("test.txt") as f:
with open("input.txt") as f:
	for line in f:
		op = line[0]
		val = int(line[1:])

		if op == 'R':
			face = (face + val) % 360
		elif op == 'L':
			face = (face - val) % 360
		else:
			mv = movement[face] if op == 'F' else movement[op_to_face[op]]
			x += mv[0] * val
			y += mv[1] * val

print(abs(x) + abs(y))
