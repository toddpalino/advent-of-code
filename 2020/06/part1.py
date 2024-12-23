#!/usr/bin/python3

from collections import Counter

counts_sum = 0

#with open("test.txt") as f:
with open("input.txt") as f:
	counts = Counter()

	for line in f:
		ln = line.strip()
		if len(ln) == 0:
			counts_sum += len(counts)
			counts = Counter()
			continue

		counts += Counter(ln)

	# Clear the last group
	counts_sum += len(counts)

print(counts_sum)
