#!/usr/bin/python3

import time
from collections import Counter

def get_prev_in_sequence(sequence):
	differences = [sequence[i] - sequence[i-1] for i in range(1, len(sequence))]
	if len(Counter(differences)) == 1:
		return sequence[0] - differences[0]
	return sequence[0] - get_prev_in_sequence(differences)


t1 = time.process_time()

prevs = []
with open("input.txt") as f:
	for line in f:
		prevs.append(get_prev_in_sequence([int(x) for x in line[:-1].split(' ')]))

t2 = time.process_time()

print(sum(prevs))
print("Time: %f" % (t2 - t1))
