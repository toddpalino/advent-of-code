#!/usr/bin/python3

seeds = []
mapping = {}
progression = {}

with open("input.txt") as f:
	source_type = None
	target_type = None
	for line in f:
		if line.startswith("seeds: "):
			seeds = [int(x) for x in line[7:-1].split(' ')]
			continue
		if "map:" in line:
			types = line[0:-6].split('-')
			source_type = types[0]
			target_type = types[2]
			progression[source_type] = target_type
			mapping[source_type] = {}
			continue

		cleaned = line.strip()
		if cleaned == '':
			continue
		nums = [int(x) for x in cleaned.split(' ')]
		mapping[source_type][(nums[1], nums[1] + nums[2])] = nums[0] - nums[1]

locations = []
for seed in seeds:
	current_val = seed
	current_type = 'seed'
	while current_type in progression:
		mapped = False
		for r, offset in mapping[current_type].items():
			if (r[0] <= current_val <= r[1]):
				current_val += offset
				current_type = progression[current_type]
				mapped = True
				break
		if not mapped:
			current_type = progression[current_type]
	locations.append(current_val)

print(min(locations))
