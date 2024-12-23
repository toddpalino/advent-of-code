#!/usr/bin/python3

from functools import reduce
from collections import deque

def get_hash(step):
	return reduce(lambda hash, c: ((hash + ord(c)) * 17) % 256, step, 0)

def print_boxes(boxes, box_focal):
	for hash, labels in enumerate(boxes):
		if len(labels) == 0:
			continue
		print("Box %d: %s" % (hash, ' '.join(['[' + label + ' ' + str(box_focal[hash][label]) + ']' for label in labels])))


with open("input.txt") as f:
	steps = f.read().strip().split(',')

boxes = [deque() for _ in range(256)]

# Use this to track the focal length of lens labels in each box. box_focal[box][label] => focal length
box_focal = {i: {} for i in range(256)}

for step in steps:
	if step[-1] == '-':
		try:
			label = step[0:-1]
			boxes[get_hash(label)].remove(label)
		except ValueError:
			pass
	else:
		parts = step.split('=')
		label = parts[0]
		focal = int(parts[1])
		hash = get_hash(label)

		if label not in boxes[hash]:
			boxes[hash].append(label)
		box_focal[hash][label] = focal

power = sum(sum((hash + 1) * (i + 1) * box_focal[hash][label] for i, label in enumerate(labels)) for hash, labels in enumerate(boxes))
print("Focusing Power: %d" % (power))
