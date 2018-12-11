#!/usr/bin/env python3

import sys

class Marble:
	def __init__(self, val):
		self.val = val
		self.clockwise = None
		self.counter_clockwise = None

	def insert_after(self, new_val):
		new_marble = Marble(new_val)
		new_marble.clockwise = self.clockwise
		self.clockwise = new_marble
		new_marble.clockwise.counter_clockwise = new_marble
		new_marble.counter_clockwise = self
		return new_marble

	def remove_before(self):
		old_marble = self.counter_clockwise
		old_marble.counter_clockwise.clockwise = self
		self.counter_clockwise = old_marble.counter_clockwise
		old_marble.clockwise = None
		old_marble.counter_clockwise = None
		return old_marble


if len(sys.argv) != 3:
	print("usage: marbles <players> <max value>")

num_players = int(sys.argv[1])
max_value = int(sys.argv[2])

score = [0] * num_players

# Marble 0 is a special case
player = -1
current = Marble(0)
current.clockwise = current
current.counter_clockwise = current

for marble in range(1, max_value + 1):
	player = (player + 1) % num_players

	if marble % 23 == 0:
		for i in range(6):
			current = current.counter_clockwise
		discard = current.remove_before()
		score[player] += marble + discard.val
			
	else:
		current = current.clockwise.insert_after(marble)

winning_score = max(score)
winning_player = score.index(winning_score) + 1
print("Winner: Player {} (scored {})".format(winning_player, winning_score))
