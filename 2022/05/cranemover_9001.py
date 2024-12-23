#!/usr/bin/python3

import re

stacks = [
	['Z', 'T', 'F', 'R', 'W', 'J', 'G'],
	['G', 'W', 'M'],
	['J', 'N', 'H', 'G'],
	['J', 'R', 'C', 'N', 'W'],
	['W', 'F', 'S', 'B', 'G', 'Q', 'V', 'M'],
	['S', 'R', 'T', 'D', 'V', 'W', 'C'],
	['H', 'B', 'N', 'C', 'D', 'Z', 'G', 'V'],
	['S', 'J', 'N', 'M', 'G', 'C'],
	['G', 'P', 'N', 'W', 'C', 'J', 'D', 'L']
]

move_re = re.compile("^move (\d+) from (\d+) to (\d+)")

with open('input.txt') as f:
	for line in f:
		m = move_re.match(line)
		if m is not None:
			count = int(m.group(1))
			s_from = int(m.group(2)) - 1
			s_to = int(m.group(3)) - 1

			crane = stacks[s_from][-count:]
			for _ in range(count):
				stacks[s_from].pop()
			stacks[s_to].extend(crane)

print("Top of stacks: %s" % ([s[-1] for s in stacks]))
