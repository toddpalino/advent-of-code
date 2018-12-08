#!/usr/bin/env python3

import re

class OverlappingClaim(Exception):
	pass


max_size = 1500
fabric = [[[] for i in range(max_size)] for j in range(max_size)]

claim_re = re.compile('^#(\d+)\s+@\s+(\d+),(\d+):\s+(\d+)x(\d+)$')
claims = []
with open('input', 'r') as f:
	for line in f:
		m = claim_re.match(line)
		if m:
			claim = int(m.group(1))
			start_x = int(m.group(2))
			start_y = int(m.group(3))
			width = int(m.group(4))
			height = int(m.group(5))
			claims.append((start_x, start_y, width, height))

			for x in range(start_x, start_x + width):
				for y in range(start_y, start_y + height):
					fabric[x][y].append(claim)

multiple_claims = 0
for x in range(max_size):
	for y in range(max_size):
		if len(fabric[x][y]) > 1:
			multiple_claims += 1
print("Overlapping sqft: {}".format(multiple_claims))

good_claim = None
for i, claim in enumerate(claims):
	try:
		for x in range(claim[0], claim[0] + claim[2]):
			for y in range(claim[1], claim[1] + claim[3]):
				if len(fabric[x][y]) > 1:
					raise OverlappingClaim
		print("Good claim: {}".format(i + 1))
	except OverlappingClaim:
		continue
