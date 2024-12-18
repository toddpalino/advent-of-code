#!/usr/bin/env python

import time
from chrono import run_program

start_time = time.time()

# There's a progression in the outputs that you can see if you watch the registers. B acts as a kind of counter,
# and we can manipulate individual digits by adding "x * 8**(digit index)" to a base of "8**(num digits), where x
# is 0-7.
#
# Following this, we can select the value for individual digits independent of the rest of the output. There is a
# trick, though - we might have two different values for a given digit that give the same output. We might need to
# select the larger one if we get to an earlier digit and can't find a solution

# Recursive method to search for the right multipliers. Returns None if no solution is found. If a recursive
# call does this, it indicates we should try another digit option if we have one
def find_digits(program, digit_idx=None, a=0):
	if digit_idx is None:
		# First call, set the digit we're working on to the last digit
		digit_idx = len(program) - 1
	if a == 0:
		# First call, so we need to set the base for a
		a = 8**digit_idx

	# Test all possible choices for this digit and save the ones that match the program
	choices = []
	for x in range(8):
		output = run_program(program, {'a': a + (x * 8**digit_idx), 'b': 0, 'c': 0})
		if output[digit_idx] == program[digit_idx]:
			choices.append(x)

	if digit_idx == 0:
		# That was our last digit to calculate
		return (a + (choices[0] * 8**digit_idx)) if choices else None

	# Test choices in increasing order until we find one that get good answers later
	for x in choices:
		ans = find_digits(program, digit_idx=digit_idx-1, a=a + (x * 8**digit_idx))
		if ans is not None:
			return ans

	# We did not find a good answer for this digit
	return None

prog_str = "2,4,1,6,7,5,4,4,1,7,0,3,5,5,3,0"
prog = [int(x) for x in prog_str.split(',')]
answer = find_digits(prog)

if answer is not None:
	print(f"Register A: {answer}")
	res = run_program(prog, {'a': answer, 'b': 0, 'c': 0})
	print("Output: ", ','.join(map(str, res)))
else:
	print("Could not find a solution")

end_time = time.time()
print("Elapsed time: %f" % (end_time - start_time))
