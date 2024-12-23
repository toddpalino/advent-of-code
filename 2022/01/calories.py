#!/usr/bin/python3

elves = []
with open('input.txt') as f:

	calories = 0
	for line in f:
		cleaned = line.strip()

		if cleaned == '':
			elves.append(calories)
			calories = 0
		else:
			calories += int(cleaned)

sorted_elves = sorted(elves)
print("Top elf: %d" % (sorted_elves[-1]))
print("Top 3: %d" % (sum(sorted_elves[-3:])))
