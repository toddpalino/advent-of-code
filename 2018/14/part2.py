#!/usr/bin/env python3

recipes = [3, 7]
elves = [0, 1]

# match_sequence is the puzzle input
match_sequence = [3, 0, 6, 2, 8, 1]

# Test inputs
#match_sequence = [5, 1, 5, 8, 9]
#match_sequence = [0, 1, 2, 4, 5]
#match_sequence = [9, 2, 5, 1, 0]
#match_sequence = [5, 9, 4, 1, 4]

# We potentially added 2 recipies, so we have to match possibly ignoring the final one
while recipes[-len(match_sequence):] != match_sequence and recipes[-len(match_sequence)-1:-1] != match_sequence:
	score_sum = recipes[elves[0]] + recipes[elves[1]]
	if score_sum >= 10:
		recipes.append(int(score_sum / 10))
		score_sum -= 10
	recipes.append(score_sum)

	# Move elves
	for elf, ptr in enumerate(elves):
		elves[elf] = (ptr + 1 + recipes[ptr]) % len(recipes)

if recipes[-len(match_sequence):] == match_sequence:
	print("Sequence {} appears after {} recipes".format(''.join(str(score) for score in match_sequence), len(recipes) - len(match_sequence)))
else:
	print("Sequence {} appears after {} recipes".format(''.join(str(score) for score in match_sequence), len(recipes) - len(match_sequence) - 1))
