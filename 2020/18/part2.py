#!/usr/bin/python3

from collections import deque


def calculate(equation):
	total = 0
	do_add = True

	while equation:
		part = equation.popleft()
		if isinstance(part, deque):
			# Sub-equation - replace with the real value
			part = calculate(part)
		if part in ('+', '*'):
			do_add = part == '+'
		else:
			total = (total + part) if do_add else (total * part)
	return total


# Chunk the equation so that it is a deque, where each entry is a number, an operator, or a deque (sub-equation)
def chunk_equation(parts):
	chunked = deque()
	while parts:
		part = parts.popleft()
		if part[0] == '(':
			# Collect parts through the matching end paren (stripping the outer parens)
			sub_parts = deque(part[1:])
			depth = part.count('(')
			while depth > 0:
				p_part = parts.popleft()
				sub_parts.append(p_part)
				depth += p_part.count('(') - p_part.count(')')
			sub_parts[-1] = sub_parts[-1][:-1]
			chunked.append(chunk_equation(sub_parts))
		else:
			chunked.append(part if part in ('+', '*') else int(part))
	return chunked


# Given a chunked equation, make every addition a sub-equation so it gets calculated before multiplication
def rechunk_addition(chunked):
	new_chunked = deque()
	while chunked:
		part = chunked.popleft()
		if part == '+':
			# Remove the left side of the + and readd it as a sub-equation with the right side
			part_a = new_chunked.pop()
			part_b = chunked.popleft()

			# Make sure we rechunk the sub-equations
			if isinstance(part_a, deque):
				part_a = rechunk_addition(part_a)
			if isinstance(part_b, deque):
				part_b = rechunk_addition(part_b)

			new_chunked.append(deque([part_a, '+', part_b]))
		else:
			new_chunked.append(rechunk_addition(part) if isinstance(part, deque) else part)
	return new_chunked

all_sum = 0

#with open("test.txt") as f:
with open("input.txt") as f:
	all_sum = sum(calculate(rechunk_addition(chunk_equation(deque(line.strip().split())))) for line in f)
print(all_sum)
