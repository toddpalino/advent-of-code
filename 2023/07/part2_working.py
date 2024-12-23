#!/usr/bin/python3

import time
from collections import Counter
from operator import itemgetter

# Strongest hand (five of a kind) is 7. Weakest hand (high card) is 1

card_values = {
	'J': 1,
	'2': 2,
	'3': 3,
	'4': 4,
	'5': 5,
	'6': 6,
	'7': 7,
	'8': 8,
	'9': 9,
	'T': 10,
	'Q': 12,
	'K': 13,
	'A': 14
}

joker_transform = {
	0: {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7},
	1: {1: 2, 2: 4, 3: 5, 4: 6, 6: 7},
	2: {1: 4, 2: 6, 4: 7},
	3: {1: 6, 2: 7},
	4: {1: 7},
}

def process_hand(line):
	cards = [card_values[card] for card in line[0:5]]

	counts = Counter(cards)
	jokers = counts[1]
	del counts[1]
	hand_type = 7
	if jokers < 5:
		ordered = sorted(counts.values(), reverse=True)
		count_max = ordered[0]
		if count_max == 1:
			hand_type = joker_transform[jokers][1]
		elif count_max >= 4:
			hand_type = joker_transform[jokers][count_max + 2]
		else:
			try:
				count_2 = ordered[1]
				if count_max == 2:
					hand_type = joker_transform[jokers][3 if count_2 == 2 else 2]
				else:
					hand_type = joker_transform[jokers][5 if count_2 == 2 else 4]
			except IndexError:
				hand_type = joker_transform[jokers][2 if count_max == 2 else 4]
	
	# hand type, list of cards, bid
	return (hand_type, *cards, int(line[6:]))


times = []
for _ in range(1000):
	t1 = time.process_time()
	with open("input.txt") as f:
		hands = [process_hand(line) for line in f]
	winnings = sum(h[6] * (i+1) for i, h in enumerate(sorted(hands)))
	t2 = time.process_time()
	times.append(t2 - t1)

print(winnings)
print("Time: %f" % (sum(times) / 1000))

