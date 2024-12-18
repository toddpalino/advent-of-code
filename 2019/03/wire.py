from itertools import product

vector = {
	'U': (0, -1),
	'D': (0, 1),
	'L': (-1, 0),
	'R': (1, 0)
}

# Given a set of directions for a wire, turn it into a list of wire segments where each segment is a 3 value
# tuple: a starting point, a vector, and a distance
def create_segments(wire, origin=(0, 0)):
	x, y = origin
	segments = []

	for path_component in wire:
		vec = vector[path_component[0]]
		dist = int(path_component[1:])

		segments.append(((x, y), dist, vec))
		x += vec[0] * dist
		y += vec[1] * dist

	return segments

def val_in_range(point, dist, vec, val):
	p = point
	e = point + (dist * vec)
	if p > e:
		p, e = e, p
	return p <= val <= e

# There is a possible gotcha here - we could have parallel line segments that overlap
# Not an issue for this puzzle, however
def get_intersections(wire_a, wire_b):
	points = []

	for seg_a, seg_b in product(wire_a, wire_b):
		vec_a = seg_a[2]
		vec_b = seg_b[2]
		if vec_a[0] == vec_b[0] or vec_a[1] == vec_b[1]:
			# Segments are parallel and cannot cross
			continue

		if vec_a[0] == 0:
			# A is vertical, B is horizontal
			if (val_in_range(seg_a[0][1], vec_a[1], seg_a[1], seg_b[0][1]) and
				val_in_range(seg_b[0][0], vec_b[0], seg_b[1], seg_a[0][0])):
				# Lines cross
				points.append((seg_a[0][0], seg_b[0][1]))
		else:
			# A is horizontal, B is vertical
			if (val_in_range(seg_a[0][0], vec_a[0], seg_a[1], seg_b[0][0]) and
				val_in_range(seg_b[0][1], vec_b[1], seg_b[1], seg_a[0][1])):
				# Lines cross
				points.append((seg_b[0][0], seg_a[0][1]))

	# We don't want to count (0, 0) as an intersection
	try:
		points.remove((0, 0))
	except ValueError:
		pass
	return points

def manhattan_distance(p1, p2):
	return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def calculate_closest_intersection(wire_a, wire_b):
	segments_a = create_segments(wire_a)
	segments_b = create_segments(wire_b)
	intersections = get_intersections(segments_a, segments_b)
	return min(manhattan_distance(intersection, (0, 0)) for intersection in intersections)

def steps_to_intersection(segments, intersection):
	total_steps = 0

	for segment in segments:
		x, y = segment[0]
		dist = segment[1]
		vec_x, vec_y = segment[2]

		for nx, ny in product(range(x, x + (dist * vec_x) + (vec_x or 1), vec_x or 1),
		                      range(y, y + (dist * vec_y) + (vec_y or 1), vec_y or 1)):
			# Always skip the first location, as it's our start point
			if x == nx and y == ny:
				continue
			total_steps += 1
			if (nx, ny) == intersection:
				return total_steps
	return 0

def calculate_min_steps(wire_a, wire_b):
	segments_a = create_segments(wire_a)
	segments_b = create_segments(wire_b)
	intersections = get_intersections(segments_a, segments_b)

	min_steps = float('inf')
	for intersection in intersections:
		steps_a = steps_to_intersection(segments_a, intersection)
		steps_b = steps_to_intersection(segments_b, intersection)
		min_steps = min(min_steps, steps_a + steps_b)
	return min_steps