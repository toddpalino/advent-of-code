#!/usr/bin/python3


def get_priority(c):
	p = ord(c) - 96
	if p < 0:
		p += 58
	return p


def get_common(c1, c2):
	for c in elf[0]:
		if c in elf[1]:
			return c


elves = []
with open('input.txt') as f:
	for line in f:
		cleaned = line.strip()

		s = len(cleaned) // 2
		elves.append((cleaned[0:s], cleaned[s:]))

total = 0
for elf in elves:
	c = get_common(elf[0], elf[1])
	p = get_priority(c)
	total += p

print(total)
