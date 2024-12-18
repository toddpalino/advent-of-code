#!/usr/bin/env python

import time
from npcomputer import read_bytes, create_grid, add_bytes, find_shortest_path

start_time = time.time()

tests = [
	{'filename': "test.txt", 'size': 7, 'max_bytes': 12, 'result': 22}
]

for i, test in enumerate(tests):
	byte_list = read_bytes(test['filename'])
	grid = create_grid(test['size'])
	add_bytes(grid, byte_list[:test['max_bytes']])
	pathlen = find_shortest_path(grid, (0, 0), (len(grid) - 1, len(grid) - 1))
	if pathlen == test['result']:
		print(f'Test {i} passed')
	else:
		print(f'Test {i} failed (expected {test["result"]}, got {pathlen})')

byte_list = read_bytes("input.txt")
grid = create_grid(71)
add_bytes(grid, byte_list[:1024])
pathlen = find_shortest_path(grid, (0, 0), (len(grid) - 1, len(grid) - 1))
print(f'Shortest path cost: {pathlen}')

end_time = time.time()
print("Elapsed time: %f" % (end_time - start_time))
