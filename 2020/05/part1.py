#!/usr/bin/python3

seat_ids = []

#with open("test.txt") as f:
with open("input.txt") as f:
	for line in f:
		ln = line.strip()

		# Swap F to 0, B to 1
		row = int(ln[0:7].translate({70: 48, 66: 49}), 2)

		# Swap L to 0, R to 1
		col = int(ln[7:].translate({76: 48, 82: 49}), 2)

		seat_ids.append((row * 8) + col)

print("Max seat ID: %d" % (max(seat_ids)))

seat_ids.sort()
for i in range(1, len(seat_ids) - 1):
	if seat_ids[i] - seat_ids[i-1] == 2:
		print(seat_ids[i] - 1)
