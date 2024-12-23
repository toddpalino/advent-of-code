#!/usr/bin/python3

cards = []
with open("input.txt") as f:
	for line in f:
		idx_win = line.index(':')
		idx_mine = line.index('|')
		cards.append({
			'winning': [int(n) for n in line[idx_win+1:idx_mine].strip().split()],
			'mine': [int(n) for n in line[idx_mine+1:].strip().split()],
			'matches': 0,
			'copies': 1
		})

for i, card in enumerate(cards):
	for n in card['mine']:
		if n in card['winning']:
			card['matches'] += 1
	for j in range(i + 1, i + 1 + card['matches']):
		cards[j]['copies'] += card['copies']

print(sum(card['copies'] for card in cards))
