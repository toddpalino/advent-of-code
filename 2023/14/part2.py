#!/usr/bin/python3

def calculate_load(platform):
	row_count = len(platform)
	return sum(row.count('O') * (row_count - i) for i, row in enumerate(platform))

def print_platform(platform):
	for row in platform:
		print(''.join(row))

def tilt_east(platform):
	for y in range(len(platform)):
		space = 0
		for x in range(len(platform[y]) - 1, -1, -1):
			c = platform[y][x]
			if c == '#':
				space = 0
			elif c == '.':
				space += 1
			else:
				if space > 0:
					platform[y][x+space] = 'O'
					platform[y][x] = '.'
	return platform

def tilt_west(platform):
	for y in range(len(platform)):
		space = 0
		for x in range(len(platform[y])):
			c = platform[y][x]
			if c == '#':
				space = 0
			elif c == '.':
				space += 1
			else:
				if space > 0:
					platform[y][x-space] = 'O'
					platform[y][x] = '.'
	return platform

def tilt_north(platform):
	for x in range(len(platform[0])):
		space = 0
		for y in range(len(platform)):
			c = platform[y][x]
			if c == '#':
				space = 0
			elif c == '.':
				space += 1
			else:
				if space > 0:
					platform[y-space][x] = 'O'
					platform[y][x] = '.'
	return platform

def tilt_south(platform):
	for x in range(len(platform[0])):
		space = 0
		for y in range(len(platform) - 1, -1, -1):
			c = platform[y][x]
			if c == '#':
				space = 0
			elif c == '.':
				space += 1
			else:
				if space > 0:
					platform[y+space][x] = 'O'
					platform[y][x] = '.'
	return platform

def spin_cycle(platform):
	platform = tilt_north(platform)
	platform = tilt_west(platform)
	platform = tilt_south(platform)
	platform = tilt_east(platform)
	return platform


platform = []
with open("input.txt") as f:
	for line in f:
		platform.append(list(line[0:-1]))

target_cycle = 1000000000
load_history = []
for c in range(target_cycle):
	platform = spin_cycle(platform)
	current_load = calculate_load(platform)

	# Run a minimum number of cycles so we don't get a false positive
	if c < 1000:
		load_history.append(current_load)
		continue

	# Cycle detection with length > 10
	try:
		# Find last instance of the current_load (at least 10 back)
		load_history.reverse()
		last = load_history[10:].index(current_load)
		load_history.reverse()
		last = len(load_history) - last - 11

		cycle_found = True
		len_history = len(load_history)
		for i in range(len_history - last):
			if load_history[last - i - 1] != load_history [len_history - 1 - i]:
				cycle_found = False
				break
		if cycle_found:
			cycle_len = len_history - last
			target_load = load_history[last + ((target_cycle - len_history) % cycle_len) - 1]
			print("Target load: %d" % (target_load))
			break
	except ValueError:
		pass
	load_history.append(current_load)

