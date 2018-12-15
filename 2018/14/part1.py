#!/usr/bin/env python3

recipes = [3, 7]
elves = [0, 1]

# output_starts_idx is the puzzle input
output_starts_idx = 306281

# Test inputs
#output_starts_idx = 9
#output_starts_idx = 5
#output_starts_idx = 18
#output_starts_idx = 2018

output_count = 10

total_recipes_needed = output_starts_idx + output_count
while len(recipes) < total_recipes_needed:
	score_sum = recipes[elves[0]] + recipes[elves[1]]
	if score_sum >= 10:
		recipes.append(int(score_sum / 10))
		score_sum -= 10
	recipes.append(score_sum)

	# Move elves
	for elf, ptr in enumerate(elves):
		elves[elf] = (ptr + 1 + recipes[ptr]) % len(recipes)

print(''.join(str(score) for score in recipes[output_starts_idx:output_starts_idx+output_count]))
