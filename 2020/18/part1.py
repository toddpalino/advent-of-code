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


#with open("test.txt") as f:
with open("input.txt") as f:
	all_sum = sum(calculate(chunk_equation(deque(line.strip().split()))) for line in f)
print(all_sum)
