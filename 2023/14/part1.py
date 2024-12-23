#!/usr/bin/python3

def calculate_load(platform):
	row_count = len(platform)
	return sum(row.count('O') * (row_count - i) for i, row in enumerate(platform))

def rotate_clockwise(original):
	list_of_tuples = zip(*original[::-1])
	return [list(elem) for elem in list_of_tuples]

def rotate_counterclockwise(original):
	return list(zip(*original))[::-1]

def print_platform(platform):
	for row in platform:
		print(''.join(row))

def tilt_row_right(row):
	space = 0
	for i in range(len(row) - 1, -1, -1):
		if row[i] == '#':
			space = 0
		elif row[i] == '.':
			space += 1
		else:
			if space > 0:
				row[i+space] = 'O'
				row[i] = '.'
	return row


platform = []
with open("input.txt") as f:
	for line in f:
		platform.append(list(line[0:-1]))

# Rotate CW so north points right
platform = rotate_clockwise(platform)

for i in range(len(platform)):
	platform[i] = tilt_row_right(platform[i])

# Rotate CCW so north points up
platform = rotate_counterclockwise(platform)

print(calculate_load(platform))
