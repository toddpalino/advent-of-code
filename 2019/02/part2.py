#!/usr/bin/env python

import time
from itertools import product
from intcode import execute

#fn = "test.txt"
fn = "input.txt"

start_time = time.time()

with open(fn, 'r') as f:
	nums = [int(x) for x in f.read().strip().split(',')]

target = 19690720

for noun, verb in product(range(100), repeat=2):
	mem = nums.copy()
	mem[1] = noun
	mem[2] = verb

	mem = execute(mem)
	if mem[0] == target:
		print("n=%d v=%d: %d" % (noun, verb, 100 * noun + verb))
		break

end_time = time.time()
print("Elapsed time: %f" % (end_time - start_time))
