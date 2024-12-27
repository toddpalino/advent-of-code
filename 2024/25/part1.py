#!/usr/bin/env python

import time
from itertools import product

def read_input(filename):
	with open(filename, 'r') as f:
		data = f.readlines()

	keys = set()
	locks = set()
	i = 0
	while i < len(data):
		pin_set = tuple(sum(data[row][pin] == '#' for row in range(i+1, i+6)) for pin in range(5))
		if data[i][:5] == '#####':
			locks.add(pin_set)
		else:
			keys.add(pin_set)
		i += 8
	return keys, locks

def count_non_overlapping(keys, locks):
	return sum(1 for lock, key in product(locks, keys) if all(lock[i] + key[i] < 6 for i in range(5)))

# Test case first
keys, locks = read_input("test.txt")
failed = False
for pin_set in ((0, 5, 3, 4, 3), (1, 2, 0, 5, 3)):
	if pin_set not in locks:
		failed = True
		print(f'Test failed - expected {pin_set} in locks')
for pin_set in ((5, 0, 2, 1, 3), (4, 3, 4, 0, 2), (3, 0, 2, 0, 1)):
	if pin_set not in keys:
		failed = True
		print(f'Test failed - expected {pin_set} in keys')
count = count_non_overlapping(keys, locks)
if count != 3:
	failed = True
	print(f'Test failed - expected 3 matches, got {count}')
if not failed:
	print('Test passed')

start_time = time.time()

keys, locks = read_input("input.txt")
print(f'Matching sets: {count_non_overlapping(keys, locks)}')

end_time = time.time()
print("Elapsed time: %f" % (end_time - start_time))
