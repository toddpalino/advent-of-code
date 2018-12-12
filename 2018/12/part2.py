#!/usr/bin/env python3

import re

# Puzzle input
pots = "#......##...#.#.###.#.##..##.#.....##....#.#.##.##.#..#.##........####.###.###.##..#....#...###.##"
rules = {
	"#####": ".",
	"####.": "#",
	"###.#": ".",
	"###..": "#",
	"##.##": "#",
	"##.#.": ".",
	"##..#": ".",
	"##...": "#",
	"#.###": "#",
	"#.##.": ".",
	"#.#.#": "#",
	"#.#..": ".",
	"#..##": "#",
	"#..#.": ".",
	"#...#": ".",
	"#....": ".",
	".####": ".",
	".###.": "#",
	".##.#": "#",
	".##..": "#",
	".#.##": ".",
	".#.#.": "#",
	".#..#": "#",
	".#...": "#",
	"..###": ".",
	"..##.": "#",
	"..#.#": "#",
	"..#..": "#",
	"...##": ".",
	"...#.": "#",
	"....#": ".",
	".....": "."
}
total_generations = 50000000000

# Add some padding
padding = 100
pots = list(('.' * 5) + pots + ('.' * padding * 2))
values = [i - 5 for i in range(len(pots))]

glider_re = re.compile('^\.{3,}(###\.{3,})+$')

for generation in range(total_generations):
	new_pots = list(pots)
	for i in range(2, len(pots) - 2):
		new_pots[i] = rules[''.join(pots[i-2:i+3])]
	pots = new_pots

	# Do we need more padding?
	if ''.join(new_pots[-5:]) != ".....":
		pots = new_pots + (['.'] * padding)
		values = values + [i + values[-1] for i in range(padding)]
	else:
		pots = new_pots

	# 3 full pots with 3 or more empties on either side will be a glider
	# If that's all we have left, we can shortcut
	# regexp is kinda slow, but we should collapse to gliders pretty quickly
	if glider_re.match(''.join(pots)):
		print("Glider detected at generation {}".format(generation + 1))

		# Figure out how many more generations we need to go, and offset the values
		offset = total_generations - generation - 1
		for i in range(len(values)):
			values[i] += offset
		break

total = sum(values[i] for i, c in enumerate(pots) if c == '#')
print("Total: {}".format(total))
