#!/usr/bin/env python

import time
import wire

fn = "input.txt"

start_time = time.time()

with open(fn, 'r') as f:
	wires = [line.strip().split(',') for line in f]

tests = [
	{'wires': [['R8','U5','L5','D3'], ['U7','R6','D4','L4']], 'answer': 30},
	{'wires': [['R75','D30','R83','U83','L12','D49','R71','U7','L72'],
	           ['U62','R66','U55','R34','D71','R55','D58','R83']], 'answer': 610},
	{'wires': [['R98','U47','R26','D63','R33','U87','L62','D20','R33','U53','R51'],
	           ['U98','R91','D20','R16','D67','R40','U7','R15','U6','R7']], 'answer': 410},
]

for i, test in enumerate(tests):
	min_steps = wire.calculate_min_steps(*test['wires'])
	if min_steps == test['answer']:
		print(f"Test {i} passed")
	else:
		print(f"Test {i} failed (expected {test['answer']}, got {min_steps})")

min_steps = wire.calculate_min_steps(*wires)
print(f"Sum of steps to intersection: {min_steps}")

end_time = time.time()
print("Elapsed time: %f" % (end_time - start_time))
