#!/usr/bin/python3

import time

# Test input
#cave_depth = 510
#target = (10, 10)

# Puzzle input
cave_depth = 4080
target = (14, 785)

map_char = ['.', '=', '|']

def erosion_level(gi):
	return (gi + cave_depth) % 20183

def region_type(el):
	return el % 3

start_time = time.time()

# For part 1, we only need to keep track of the row we're on and the previous one
# We can also overwrite them as we go, rather than explicitly clearing them

max_x = target[0]
max_y = target[1]
total_risk = 0

# First row (y=0)
row_prev = [erosion_level(x * 16807) for x in range(max_x+1)]
total_risk += sum(region_type(el) for el in row_prev)
# print(''.join(map_char[region_type(el)] for el in row_prev))

# Subsequent rows
row = [0] * (max_x + 1)
for y in range(1, max_y+1):
	for x in range(max_x + 1):
		if x == 0:
			row[x] = erosion_level(48271 * y)
		elif x == max_x and y == max_y:
			# Special case for the target
			row[x] = 0
		else:
			row[x] = erosion_level(row_prev[x] * row[x-1])

	total_risk += sum(region_type(el) for el in row)
	# print(''.join(map_char[region_type(el)] for el in row))
	row_prev, row = row, row_prev

print("Total risk: %d" % (total_risk))

end_time = time.time()
print("Elapsed time: %f" % (end_time - start_time))
