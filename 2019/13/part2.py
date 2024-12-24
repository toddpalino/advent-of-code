#!/usr/bin/env python

import time
from itertools import batched
from aoc.utils.intcode import Intcode, read_intcode_from_file
from recording import keystrokes


start_time = time.time()

computer = Intcode(read_intcode_from_file("input.txt"), pause_for_input=True)
computer.set_memory_location(0, 2)
computer.add_input(keystrokes)
computer.run()

score = 0
screen = {}
recording = []
while not computer.is_halted():
	for x, y, num in batched(computer.get_output(), 3):
		if x == -1 and y == 0:
			score = num
		else:
			screen[(x, y)] = num

	# Draw the screen
	print(f'Score: {score}')
	max_x = max(s[0] for s in screen.keys())
	max_y = max(s[1] for s in screen.keys())
	for y in range(max_y+1):
		for x in range(max_x+1):
			if (x, y) in screen:
				num = screen[(x, y)]
				if num == 0:
					print(' ', end='')
				elif num == 1:
					print('#', end='')
				elif num == 2:
					print('*', end='')
				elif num == 3:
					print('-', end='')
				elif num == 4:
					print('.', end='')
		print()

	# Get input from the user and continue
	joystick = None
	while joystick is None:
		try:
			joystick = int(input("Move joystick (Left: -1, Neutral: 0, Right: 1): "))
		except ValueError:
			joystick = None

	recording.append(joystick)
	computer.add_input(joystick)
	computer.run()

print(f'Input recording: {recording}')
out = computer.get_output()
print(f'Final score: {out[-1]}')

end_time = time.time()
print("Part 1 Elapsed time: %f" % (end_time - start_time))
