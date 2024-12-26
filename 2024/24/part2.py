#!/usr/bin/env python
import time

from wires import read_input, get_wire_set, find_bad_gates


start_time = time.time()
wires, gates = read_input('input.txt')
wire_sets = {
	'x': get_wire_set(wires, 'x'),
	'y': get_wire_set(wires, 'y'),
	'z': get_wire_set(wires, 'z')
}

found_solution = find_bad_gates(wires, gates, wire_sets, set(k for k, v in wires.items() if v.wire_value is None))
if found_solution:
	# When find_bad_gates exits, the wire/gate configuration is left in the working state, with the swapped
	# wires marked
	swapped_wires = [wire.name for wire in wires.values() if wire.is_swapped()]
	swapped_wires.sort()
	print(f'Swapped wires: {','.join(swapped_wires)}')

end_time = time.time()
print("Elapsed time: %f" % (end_time - start_time))
