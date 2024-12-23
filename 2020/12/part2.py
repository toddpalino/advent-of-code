#!/usr/bin/python3

movement = {
	'N': (0, 1),
	'S': (0, -1),
	'E': (1, 0),
	'W': (-1, 0)
}

# We're using cartesian coordinates, so start at 0. We don't care about facing direction now
x = 0
y = 0

# Waypoint is relative to the ship - starts 10 east and 1 north
waypoint_x = 10
waypoint_y = 1

#with open("test.txt") as f:
with open("input.txt") as f:
	for line in f:
		op = line[0]
		val = int(line[1:])

		if op in 'NSEW':
			mv = movement[op]
			waypoint_x += mv[0] * val
			waypoint_y += mv[1] * val
		elif op == 'F':
			x += waypoint_x * val
			y += waypoint_y * val
		if op == 'R':
			for _ in range(val // 90):
				temp_x = waypoint_x
				waypoint_x = waypoint_y
				waypoint_y = -temp_x
		elif op == 'L':
			for _ in range(val // 90):
				temp_x = waypoint_x
				waypoint_x = -waypoint_y
				waypoint_y = temp_x

print(abs(x) + abs(y))

