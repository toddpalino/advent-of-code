#!/usr/bin/python3

def calculate(equation):
	total = 0
	do_add = True
	parts = equation.strip().split()

	i = 0
	while i < len(parts):
		part = parts[i]
		if part in ('+', '*'):
			do_add = part == '+'
			i += 1
			continue

		val = None
		if part[0] == '(':
			# find the matching end paren
			end_i = i
			depth = part.count('(')
			while depth > 0:
				end_i += 1
				p_part = parts[end_i]
				depth += p_part.count('(') - p_part.count(')')

			# Rejoin the string and recursively calculate (strip the outer parens)
			val = calculate(' '.join(parts[i:end_i+1])[1:-1])
			i = end_i
		else:
			val = int(part)

		total = (total + val) if do_add else (total * val)
		i += 1

	return total


#with open("test.txt") as f:
with open("input.txt") as f:
	all_sum = sum(calculate(line) for line in f)
print(all_sum)
