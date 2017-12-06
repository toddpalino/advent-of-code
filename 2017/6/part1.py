#!/usr/bin/python

# Read in input
with open("input", "r") as f:
	banks = [int(x) for x in f.read().strip().split()]

# Test input
# banks = [0, 2, 7, 0]

def max_blocks(banks):
	m = 0
	for i in range(1, len(banks)):
		if banks[i] > banks[m]:
			m = i
	return m


num_banks = len(banks)
seen = {tuple(banks): 0}
count = 0

while True:
	i = max_blocks(banks)
	blocks = banks[i]
	banks[i] = 0
	while blocks > 0:
		i = (i + 1) % num_banks
		banks[i] = banks[i] + 1
		blocks -= 1
	count += 1

	k = tuple(banks)
	if k in seen:
		print("Loop size: {0}".format(count - seen[k]))
		break
	seen[k] = count

print("Count: {0}".format(count))
