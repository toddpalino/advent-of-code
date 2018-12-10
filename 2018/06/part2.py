#!/usr/bin/env python3

with open('input', 'r') as f:
	coords = [line.strip().split(", ") for line in f]

max_size = 500
region = 0

for x in range(max_size):
	for y in range(max_size):
		total_distance = sum([abs(x - int(coord[0])) + abs(y - int(coord[1])) for coord in coords])
		if total_distance < 10000:
			region += 1

print("{}".format(region))
