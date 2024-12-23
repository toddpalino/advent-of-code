#!/usr/bin/python3

from itertools import product

class NonogramError(Exception):
	pass

def generate_candidates(num_gaps, num_blanks):
	candidates = []
	for c in product(range(num_blanks - num_gaps + 2), repeat=num_gaps+2):
		try:
			if sum(c) != num_blanks:
				raise NonogramError
			for i in range(1, num_gaps + 1):
				if c[i] == 0:
					raise NonogramError
			candidates.append(c)
		except NonogramError:
			pass
	return candidates


stored_candidates = {}
possible_solutions = 0
with open("input.txt") as f:
	for line in f:
		parts = line[0:-1].split(' ')
		groups = [int(x) for x in parts[1].split(',')]
		raw_row = parts[0]

		num_gaps = len(groups) - 1
		num_blanks = len(raw_row) - sum(groups)
		if (num_gaps, num_blanks) not in stored_candidates:
			stored_candidates[(num_gaps, num_blanks)] = generate_candidates(num_gaps, num_blanks)
		candidates = stored_candidates[(num_gaps, num_blanks)]

		row = [None] * len(raw_row)
		for i in range(len(raw_row)):
			if raw_row[i] == '.':
				row[i] = False
			elif raw_row[i] == '#':
				row[i] = True

		for candidate in candidates:
			try:
				pos = 0
				for i in range(len(groups)):
					for j in range(pos, candidate[i]+pos):
						if row[j]:
							raise NonogramError
					pos += candidate[i]
					for j in range(pos, groups[i]+pos):
						if row[j] is not None and not row[j]:
							raise NonogramError
					pos += groups[i]
				for j in range(pos, candidate[-1]+pos):
					if row[j]:
						raise NonogramError
				possible_solutions += 1
			except NonogramError:
				pass

print(possible_solutions)
