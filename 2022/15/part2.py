#!/usr/bin/python3

import re

sensor_re = re.compile("Sensor at x=([\d-]+), y=([\d-]+): closest beacon is at x=([\d-]+), y=([\d-]+)")

sensors = []
with open("input.txt") as f:
	for line in f:
		m = sensor_re.match(line)
		sensors.append({
			'sensor': (int(m.group(1)), int(m.group(2))),
			'beacon': (int(m.group(3)), int(m.group(4)))
		})

max_coord = 4000000
beacon = None
for check_y in range(max_coord):
	# list of tuples => (ID, x). These are the start and end points of coverage
	points = []

	for i, sensor in enumerate(sensors):
		dist = abs(sensor['sensor'][0] - sensor['beacon'][0]) + abs(sensor['sensor'][1] - sensor['beacon'][1])
		if check_y > sensor['sensor'][1]:
			dist -= check_y - sensor['sensor'][1]
		else:
			dist -= sensor['sensor'][1] - check_y

		if dist >= 0:
			points.append((i, sensor['sensor'][0] - dist))
			points.append((i, sensor['sensor'][0] + dist))

	points.sort(key=lambda a: a[1])

	uncovered_since = 0
	inside = set([points[0][0]])
	if points[0][1] > 0:
		# I guess we found it
		beacon = (0, check_y)
		break

	for i in range(1, len(points)):
		point = points[i]

		if point[0] in inside:
			inside.remove(point[0])
			if len(inside) == 0:
				uncovered_since = point[1] + 1
		else:
			if (0 <= point[1] <= max_coord) and (len(inside) == 0) and (point[1] > uncovered_since):
				beacon = (uncovered_since, check_y)
				break
			inside.add(point[0])

	if beacon is not None:
		break

print(beacon)
print((beacon[0] * 4000000) + beacon[1])
