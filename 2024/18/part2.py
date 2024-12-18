#!/usr/bin/env python

import time
from npcomputer import read_bytes, create_grid, add_bytes, find_shortest_path

start_time = time.time()

tests = [
	{'filename': "test.txt", 'size': 7, 'max_bytes': 12, 'result': (6, 1)}
]

for i, test in enumerate(tests):
	byte_list = read_bytes(test['filename'])
	grid = create_grid(test['size'])
	add_bytes(grid, byte_list[:test['max_bytes']])
	for b in byte_list[test['max_bytes']:]:
		add_bytes(grid, [b])
		pathlen = find_shortest_path(grid, (0, 0), (len(grid) - 1, len(grid) - 1))
		if pathlen is None:
			if b == test['result']:
				print(f'Test {i} passed')
			else:
				print(f'Test {i} failed (expected {test["result"]}, got {b})')
			break

byte_list = read_bytes("input.txt")
grid = create_grid(71)
add_bytes(grid, byte_list[:1024])
for b in byte_list[1024:]:
	add_bytes(grid, [b])
	pathlen = find_shortest_path(grid, (0, 0), (len(grid) - 1, len(grid) - 1))
	if pathlen is None:
		print(f"Path does not exist after {b}")
		break

end_time = time.time()
print("Elapsed time: %f" % (end_time - start_time))
