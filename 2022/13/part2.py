#!/usr/bin/python3

import functools
import json

# 0 if they are equal
# -1 if right is "larger" (right comes after left - in order)
# 1 if left is "larger" (left comes after right)
def cmp_lists(list_left, list_right):
	for i in range(max(len(list_left), len(list_right))):
		try:
			left = list_left[i]
		except IndexError:
			return -1
		try:
			right = list_right[i]
		except IndexError:
			return 1

		if type(left) is int and type(right) is int:
			if left == right:
				continue
			else:
				return 1 if left > right else -1
		else:
			if type(left) is int:
				left = [left]
			if type(right) is int:
				right = [right]
			rv = cmp_lists(left, right)
			if rv != 0:
				return rv
	return 0

packets = []
with open("input.txt") as f:
	for line in f:
		cleaned = line.strip()
		if cleaned != '':
			packets.append(json.loads(cleaned))
dividers = [[[2]], [[6]]]
packets.extend(dividers)

sorted_packets = sorted(packets, key=functools.cmp_to_key(cmp_lists))
indices = []
for i, packet in enumerate(sorted_packets):
	if packet in dividers:
		indices.append(i + 1)
		print(packet)
print(indices[0] * indices[1])
