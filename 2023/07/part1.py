#!/usr/bin/python3

from collections import Counter
import time

# Strongest hand (five of a kind) is 7. Weakest hand (high card) is 1

card_values = {
	'2': 2,
	'3': 3,
	'4': 4,
	'5': 5,
	'6': 6,
	'7': 7,
	'8': 8,
	'9': 9,
	'T': 10,
	'J': 11,
	'Q': 12,
	'K': 13,
	'A': 14
}

def get_type_for_hand(cards):
	c = Counter(cards)
	found_pair = False
	found_three = False
	for count in c.values():
		if count >= 4:
			return count + 2
		if count == 3:
			if found_pair:
				return 5
			found_three = True
		if count == 2:
			if found_pair:
				return 3
			if found_three:
				return 5
			found_pair = True
	if found_three:
		return 4
	if found_pair:
		return 2
	return 1


def key_for_hand(hand):
	val = hand['type'] * (10 ** 10)
	for i, card in enumerate(hand['cards']):
		position = 10 ** (2 * (5 - i - 1))
		val += card * position
	return val
		

t1 = time.process_time()

hands = []
with open("input.txt") as f:
	for line in f:
		hand = {
			'cards': [card_values[x] for x in line[0:5]],
			'bid': int(line[6:]),
		}
		hand['type'] = get_type_for_hand(hand['cards'])
		hands.append(hand)

hands.sort(key=lambda x: key_for_hand(x))
winnings = sum(h['bid'] * (i+1) for i, h in enumerate(hands))

t2 = time.process_time()

print(winnings)
print("Time: %f" % (t2 - t1,))

