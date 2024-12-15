#!/usr/bin/env python

import time
from intcode import execute

#fn = "test.txt"
fn = "input.txt"

start_time = time.time()

with open(fn, 'r') as f:
	nums = [int(x) for x in f.read().strip().split(',')]

# Replacements from puzzle text
nums[1] = 12
nums[2] = 2

nums = execute(nums)
print("Value at position 0: %d" % (nums[0]))

end_time = time.time()
print("Elapsed time: %f" % (end_time - start_time))
