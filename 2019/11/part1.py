#!/usr/bin/env python

import time
from intcode import Intcode, read_intcode_from_file

# Vectors - we will use an index to this. Left turn is -1, right turn is +1. Always mod 4. Start up
vectors = [(0, -1), (1, 0), (0, 1), (-1, 0)]

def run_robot(comp, part=1):
	vidx = 0

	# Keep track of what panels have been painted
	white = set()
	black = set()

	# Set the starting position and input the starting color
	x = 0
	y = 0
	comp.add_input(0 if part == 1 else 1)

	while True:
		# Restart the computer
		comp.run()

		# Computer will stop after the first output. We need two. We also need to check after every run if it finished
		if comp.is_halted():
			break
		comp.run()
		if comp.is_halted():
			break

		color, vector_change = comp.get_output()
		if color == 0:
			white.discard((x, y))
			black.add((x, y))
		else:
			black.discard((x, y))
			white.add((x, y))

		vidx = (vidx + (1 if vector_change else -1)) % 4
		x, y = x + vectors[vidx][0], y + vectors[vidx][1]

		# As the last step, we'll input the color of the panel we're on
		comp.add_input(1 if (x, y) in white else 0)

	if part == 1:
		print(f'Part 1 - Robot painted {len(black) + len(white)} squares')
	else:
		# Figure out our max X and Y
		max_x = max(max(c[0] for c in black), max(c[0] for c in white))
		max_y = max(max(c[1] for c in black), max(c[1] for c in white))
		for y in range(max_y + 1):
			for x in range(max_x + 1):
				if (x, y) in white:
					print(u"\u25A0", end='')
				else:
					print(" ", end='')
			print()

start_time = time.time()
computer = Intcode(read_intcode_from_file("input.txt"), pause_on_output=True)
run_robot(computer)
end_time = time.time()
print("Part 1 Elapsed time: %f" % (end_time - start_time))

start_time = time.time()
computer.reset()
run_robot(computer, part=2)
end_time = time.time()
print("Part 2 Elapsed time: %f" % (end_time - start_time))
