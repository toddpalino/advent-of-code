#!/usr/bin/env python

import time
from collections import Counter
from itertools import batched

def decode_layers(data, width, height):
	return tuple(batched(batched(data, width), height))

def decode_image(data, width, height):
	return [''.join(row) for row in
	        batched([''.join(stack).lstrip('2')[0] for stack in zip(*batched(data, width * height))], width)]

start_time = time.time()

# Test first
data = '123456789012'
width = 3
height = 2

layers = decode_layers(data, width, height)
if len(layers) != 2:
	print(f"Test failed (expected 2 layers, got {len(layers)})")
if layers != ((('1', '2', '3'), ('4', '5', '6')), (('7', '8', '9'), ('0', '1', '2'))):
	print(f"Test failed (did not get expected layers)")

# Puzzle input
width = 25
height = 6
with open('input.txt', 'r') as f:
	data = f.read()
layers = decode_layers(data, width, height)

min_counter = None
min_zeros = float('inf')
for layer in layers:
	c = Counter()
	for row in layer:
		c.update(row)
	if c['0'] < min_zeros:
		min_zeros = c['0']
		min_counter = c

print(f'Checksum: {min_counter['1'] * min_counter['2']}')
print()

img = decode_image(data, width, height)
for row in img:
	print(row.translate(str.maketrans("01",u" \u25A0")))

end_time = time.time()
print("Elapsed time: %f" % (end_time - start_time))
