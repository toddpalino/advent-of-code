#!/usr/bin/python3

from collections import Counter

def get_next_in_sequence(sequence):
	differences = [sequence[i] - sequence[i-1] for i in range(1, len(sequence))]
	if len(Counter(differences)) == 1:
		return sequence[-1] + differences[0]
	return sequence[-1] + get_next_in_sequence(differences)


nexts = []
with open("input.txt") as f:
	for line in f:
		nexts.append(get_next_in_sequence([int(x) for x in line[:-1].split(' ')]))

print(sum(nexts))
