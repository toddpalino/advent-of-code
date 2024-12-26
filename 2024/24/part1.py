#!/usr/bin/env python

import time
from wires import read_input, get_wire_set_value, get_wire_set

test = [
	{'filename': 'test0.txt', 'value': 4},
	{'filename': 'test1.txt', 'value': 2024},
]

for i, test in enumerate(test):
	wires, gates = read_input(test['filename'])
	wire_sets = {
		'x': get_wire_set(wires, 'x'),
		'y': get_wire_set(wires, 'y'),
		'z': get_wire_set(wires, 'z')
	}
	val = get_wire_set_value(wire_sets['z'])
	if val != test['value']:
		print(f'Test {i} failed: expected {test["value"]}, got {val}')
	else:
		print(f'Test {i} passed')

start_time = time.time()

wires, gates = read_input('input.txt')
wire_sets = {
	'x': get_wire_set(wires, 'x'),
	'y': get_wire_set(wires, 'y'),
	'z': get_wire_set(wires, 'z')
}
val = get_wire_set_value(wire_sets['z'])
print(f'Output value: {val}')

end_time = time.time()
print("Elapsed time: %f" % (end_time - start_time))
