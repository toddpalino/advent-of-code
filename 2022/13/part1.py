#!/usr/bin/python3

import json

def lists_in_order(list_left, list_right):
	while True:
		if len(list_left) == 0 and len(list_right) == 0:
			return None
		try:
			left = list_left.pop(0)
		except IndexError:
			return True
		try:
			right = list_right.pop(0)
		except IndexError:
			return False

		if type(left) is int and type(right) is int:
			if left == right:
				continue
			else:
				return left < right
		else:
			if type(left) is int:
				left = [left]
			if type(right) is int:
				right = [right]
			rv = lists_in_order(left, right)
			if rv is not None:
				return rv

pairs = []
packets = []
with open("input.txt") as f:
	for line in f:
		cleaned = line.strip()
		if cleaned == '':
			pairs.append(packets)
			packets = []
		else:
			packets.append(json.loads(cleaned))
pairs.append(packets)

sum_indices = 0
for i, pair in enumerate(pairs):
	rv = lists_in_order(pair[0], pair[1])
	if rv:
		print(i)
		sum_indices += i + 1

print(sum_indices)
