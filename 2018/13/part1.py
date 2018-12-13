#!/usr/bin/env python3

from operator import attrgetter

class Cart:
	def __init__(self, x, y, c):
		self.x = x
		self.y = y
		self.next_turn = -1

		if c == '^':
			self.move_x = 0
			self.move_y = -1
		elif c == 'v':
			self.move_x = 0
			self.move_y = 1
		elif c == '<':
			self.move_x = -1
			self.move_y = 0
		elif c == '>':
			self.move_x = 1
			self.move_y = 0
		else:
			raise NotImplementedError("Bad cart character: {}".format(c))

	# Possible tracks: - | / \ +
	def move(self, map):
		# Move first - we're already facing the right way
		self.x += self.move_x
		self.y += self.move_y

		# Figure out if we need to turn
		track = map[self.y][self.x]
		if track == '+':
			self.intersection()
		elif track == '/':
			self.turn(1 if self.move_x == 0 else -1)
		elif track == '\\':
			self.turn(-1 if self.move_x == 0 else 1)

	def intersection(self):
		self.turn(self.next_turn)

		# This is a little trickery understanding that an index of -1 gives the last element
		self.next_turn = (1, -1, 0)[self.next_turn]

	# left = -1, right = +1, straight = 0
	def turn(self, direction):
		if direction == 0:
			return

		self.move_x, self.move_y = self.move_y, self.move_x
		if direction == -1 and self.move_x == 0:
			self.move_y = -self.move_y
		elif direction == 1 and self.move_y == 0:
			self.move_x = -self.move_x


def detect_crash(carts):
	positions = {}
	for cart in carts:
		coords = (cart.x, cart.y)
		if coords in positions:
			return coords
		else:
			positions[coords] = cart
	return None


with open("input", "r") as f:
	map = [list(line.rstrip("\n")) for line in f]

# Remove the carts from the map and create them
carts = []
for y in range(len(map)):
	for x in range(len(map[y])):
		if map[y][x] in ('^', 'v'):
			carts.append(Cart(x, y, map[y][x]))
			map[y][x] = '|'
		elif map[y][x] in ('<', '>'):
			carts.append(Cart(x, y, map[y][x]))
			map[y][x] = '-'

t = 0
crash_detected = False
while not crash_detected:
	# Order the list of carts by row and column (steps in reverse)
	carts.sort(key=attrgetter('x'))
	carts.sort(key=attrgetter('y'))

	# Move carts in turn
	for cart in carts:
		cart.move(map)

		# Check for a crash
		crash_at = detect_crash(carts)
		if crash_at is not None:
			print("Crash detected at tick {}: {}".format(t, crash_at))
			crash_detected = True
			break

	t += 1
