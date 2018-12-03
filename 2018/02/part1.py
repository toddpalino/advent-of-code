#!/usr/bin/env python3

def checksum(box_id):
	counts = {}
	for c in box_id:
		counts[c] = counts.get(c, 0) + 1

	results = [0, 0]
	for c in counts:
		if counts[c] == 2:
			results[0] = 1
		if counts[c] == 3:
			results[1] = 1
	return results


box_ids = {}
with open("input", "r") as f:
	for line in f:
		box_id = line.rstrip()
		box_ids[box_id] = checksum(box_id)

# Calculate checksums
sum_twos = sum(box_ids[box_id][0] for box_id in box_ids)
sum_threes = sum(box_ids[box_id][1] for box_id in box_ids)
print("Checksum: " + str(sum_twos * sum_threes))
