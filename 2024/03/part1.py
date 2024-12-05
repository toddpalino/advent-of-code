#!/usr/bin/python3

import re

#fn = "test.txt"
fn = "input.txt"

mul_re = re.compile(r'mul\((\d+),(\d+)\)')

with open(fn, 'r') as f:
	mem = f.read()

total = sum(int(pair[0]) * int(pair[1]) for pair in mul_re.findall(mem))

print("Total: %d" % (total))
