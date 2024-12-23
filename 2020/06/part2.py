#!/usr/bin/python3

from collections import Counter

counts_sum = 0

#with open("test.txt") as f:
with open("input.txt") as f:
	counts = Counter()
	members = 0

	for line in f:
		ln = line.strip()
		if len(ln) == 0:
			counts_sum += sum(1 if counts[c] == members else 0 for c in counts)
			counts = Counter()
			members = 0
			continue

		members += 1
		counts += Counter(ln)

	# Clear the last group
	counts_sum += sum(1 if counts[c] == members else 0 for c in counts)

print(counts_sum)
