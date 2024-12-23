#!/usr/bin/env python

import time
from itertools import product
from aoc.utils.intcode import Intcode, read_intcode_from_file

#fn = "test.txt"
fn = "input.txt"

start_time = time.time()

target = 19690720
intcode = Intcode(read_intcode_from_file(fn))

for noun, verb in product(range(100), repeat=2):
	intcode.reset()
	intcode._mem[1] = noun
	intcode._mem[2] = verb

	intcode.run()
	if intcode._mem[0] == target:
		print("n=%d v=%d: %d" % (noun, verb, 100 * noun + verb))
		break

end_time = time.time()
print("Elapsed time: %f" % (end_time - start_time))
