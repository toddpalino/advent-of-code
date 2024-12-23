#!/usr/bin/python3

import time

t1 = time.process_time()

seeds = []
mapping = {}
progression = {}

# mapping: dict with keys being stage names and the value being a list of tuples => (range start, range end, offset)

with open("input.txt") as f:
	source_type = None
	target_type = None
	for line in f:
		if len(line) == 1:
			continue
		if line[5] == ':':
			seeds = [int(x) for x in line[7:-1].split(' ')]
			continue
		if line[-2] == ':':
			types = line[0:-6].split('-')
			source_type = types[0]
			progression[source_type] = types[2]
			mapping[source_type] = []
			continue

		nums = [int(x) for x in line[:-1].split(' ')]
		mapping[source_type].append((nums[1], nums[1] + nums[2] - 1, nums[0] - nums[1]))

t2 = time.process_time()

for t, ranges in mapping.items():
	ranges.sort()

current_type = 'seed'
ranges = [(seeds[i], seeds[i] + seeds[i+1] - 1) for i in range(0, len(seeds), 2)]
ranges.sort()

while current_type in progression:
	new_ranges = []
	m = mapping[current_type].pop(0)
	m_start = m[0]
	m_end = m[1]
	m_offset = m[2]

	r = None
	r_start = 0
	r_end = -1
	while True:
		if r_end < r_start:
			if not ranges:
				break
			r = ranges.pop(0)
			r_start = r[0]
			r_end = r[1]

		if r_start < m_start:
			if r_end < m[0]:
				new_ranges.append((r_start, r_end))
				r_start = r_end + 1
			else:
				new_ranges.append((r_start, m_start - 1))
				r_start = m_start
		elif m_start <= r_start <= m_end:
			if r_end <= m_end:
				new_ranges.append((r_start + m_offset, r_end + m_offset))
				r_start = r_end + 1
			else:
				new_ranges.append((r_start + m_offset, m_start + m_offset))
				r_start = m_end + 1
		else:
			if mapping[current_type]:
				m = mapping[current_type].pop(0)
				m_start = m[0]
				m_end = m[1]
				m_offset = m[2]
			else:
				new_ranges.append((r_start, r_end))
				r_start = r_end + 1

	ranges = sorted(new_ranges)
	current_type = progression[current_type]

t3 = time.process_time()
print(ranges[0][0])
print("Times: %f %f" % (t2 - t1, t3 - t2))
