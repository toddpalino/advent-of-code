#!/usr/bin/env python

import time

#fn = "test.txt"
fn = "input.txt"

start_time = time.time()

groups = set()
computer = {}
with open(fn, 'r') as f:
	for line in f:
		c1, c2 = line.strip().split('-')
		if c1 not in computer:
			computer[c1] = {c2}
		else:
			computer[c1].add(c2)
		if c2 not in computer:
			computer[c2] = {c1}
		else:
			computer[c2].add(c1)
		for c3 in computer[c1] & computer[c2]:
			groups.add(frozenset((c1, c2, c3)))

print(f'Number of triples with a computer starting with "t": {sum(1 for c1, c2, c3 in groups
                                                                  if 't' in (c1[0], c2[0], c3[0]))}')
print("Part 1 Elapsed time: %f" % (time.time() - start_time))
print()

while len(groups) > 1:
	groups = set(frozenset.union(group, [c1])
	             for group in groups for c1 in set.intersection(*[computer[c] for c in group]))

print(f'LAN Party Password: {','.join(sorted(groups.pop()))}')

end_time = time.time()
print("Elapsed time: %f" % (end_time - start_time))
