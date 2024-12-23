#!/usr/bin/python3

cards = []
with open("input.txt") as f:
	for line in f:
		idx_win = line.index(':')
		idx_mine = line.index('|')
		cards.append({
			'winning': [int(n) for n in line[idx_win+1:idx_mine].strip().split()],
			'mine': [int(n) for n in line[idx_mine+1:].strip().split()]
		})

total_points = 0
for card in cards:
	matches = 0
	for n in card['mine']:
		if n in card['winning']:
			matches += 1
	if matches < 2:
		total_points += matches
	else:
		total_points += 2 ** (matches - 1)

print(total_points)
