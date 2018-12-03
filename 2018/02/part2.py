#!/usr/bin/env python3

from itertools import combinations

def differ_by_one(string_pair):
	idx_of_difference = None
	for idx, char_pair in enumerate(zip(string_pair[0], string_pair[1])):
		if char_pair[0] != char_pair[1]:
			if idx_of_difference is not None:
				return None
			idx_of_difference = idx
	return idx_of_difference


with open("input", "r") as f:
	box_ids = [line.rstrip() for line in f]

for pair in combinations(box_ids, 2):
	idx = differ_by_one(pair)
	if idx is not None:
		print("Common characters: " + pair[0][:idx] + pair[0][idx+1:])
		break
