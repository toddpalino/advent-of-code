#!/usr/bin/python3

from collections import deque

def calculate_area(array):
	a = 0
	ox,oy = array[0]
	for x,y in array[1:]:
		a += (x*oy-y*ox)
		ox,oy = x,y
	return a/2

x = 0
y = 0
points = deque([(0, 0)])

# Since we're tracking the cartesian coordinates of the OUTSIDE of the shape,
# we need to track when we are creating outside corners vs inside corners
prev_corner = True
last_direction = None

with open("input.txt") as f:
	for line in f:
		direction = int(line[-3])
		dist = int(line[-8:-3], 16)

		if last_direction is not None:
			# Calculate the last corner type (last_direction and current direction)
			last_corner = ((last_direction == 0 and direction == 1) or (last_direction == 1 and direction == 2) or
					(last_direction == 2 and direction == 3) or (last_direction == 3 and direction == 0))

			# Adjust last point only if the last 2 corners are the same type
			if not (prev_corner ^ last_corner):
				adjustment = 1 if last_corner else -1
				if last_direction == 3:
					points[-1] = (points[-1][0], points[-1][1] + adjustment)
				elif last_direction == 1:
					points[-1] = (points[-1][0], points[-1][1] - adjustment)
				elif last_direction == 2:
					points[-1] = (points[-1][0] - adjustment, points[-1][1])
				elif last_direction == 0:
					points[-1] = (points[-1][0] + adjustment, points[-1][1])

			prev_corner = last_corner

		current = points[-1]
		if direction == 0:
			points.append((current[0] + dist, current[1]))
		if direction == 2:
			points.append((current[0] - dist, current[1]))
		if direction == 3:
			points.append((current[0], current[1] + dist))
		if direction == 1:
			points.append((current[0], current[1] - dist))
		last_direction = direction

# To calculate area, we should close the last line
points.append((0, 0))

print(calculate_area(list(points)))
