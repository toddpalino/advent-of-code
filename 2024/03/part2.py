#!/usr/bin/python3

import re

#fn = "test2.txt"
fn = "input.txt"

instruction_re = re.compile(r"(mul\((\d+),(\d+)\)|do\(\)|don't\(\))")

with open(fn, 'r') as f:
	instructions = instruction_re.findall(f.read())

total = 0
enabled = True
for instruction in instructions:
	if enabled and instruction[0].startswith("mul"):
		total += int(instruction[1]) * int(instruction[2])
	elif instruction[0] == "do()":
		enabled = True
	else:
		enabled = False

print("Total: %d" % (total))
