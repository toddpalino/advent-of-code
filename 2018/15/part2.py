#!/usr/bin/env python3

import time
from collections import deque
from operator import methodcaller, attrgetter, itemgetter

class Space:
	def __init__(self, x, y):
		self.x = x
		self.y = y

		self.up = None
		self.down = None
		self.left = None
		self.right = None

		self.occupant = None

	def adjacent_units(self):
		return [direction.occupant for direction in (self.up, self.left, self.right, self.down) if direction is not None and direction.occupant is not None]

	def adjacent_targets(self, target_klass):
		return [target for target in self.adjacent_units() if isinstance(target, target_klass)]


class Fighter:
	def __init__(self, space, attack=3):
		self.location = space
		space.occupant = self

		self.hp = 200
		self.attack = attack

	def x(self):
		return self.location.x

	def y(self):
		return self.location.y

	def is_elf(self):
		raise NotImplementedError

	def is_goblin(self):
		raise NotImplementedError

	def is_alive(self):
		return self.hp > 0

	def move(self):
		# Shortcut if we're already in range of a target
		if len(self.location.adjacent_targets(self.target_klass)) > 0:
			return

		# The first entry in the path is where we currently are. It's a little odd, but it helps with the iteration check
		paths = deque([[self.location]])
		seen = set([None, self.location])

		# Figure out which target locations are the fewest steps away
		options = {}
		target_distance = 999999
		while len(paths) > 0:
			# Get our next path to work on, and make sure we're not longer than a found target_distance yet
			path = paths.popleft()
			if len(path) > target_distance:
				break

			for direction in (path[-1].up, path[-1].left, path[-1].right, path[-1].down):
				if direction not in seen:
					seen.add(direction)
					if direction.occupant is None:
						paths.append(path + [direction])
					elif isinstance(direction.occupant, self.target_klass):
						# First entry in the path is where we are, second is where we're going
						options[(direction.x, direction.y)] = path[1]
						target_distance = len(path)

		if len(options) == 0:
			# No target found
			return

		# Order the targets found in reading order so we can pick the right one
		targets = sorted(options.keys(), key=itemgetter(0))
		targets = sorted(targets, key=itemgetter(1))

		self.location.occupant = None
		self.location = options[targets[0]]
		self.location.occupant = self

	def fight(self):
		targets = self.location.adjacent_targets(self.target_klass)
		if len(targets) == 0:
			# Aww, nobody to fight nearby
			return

		target = sorted(targets, key=attrgetter('hp'))[0]
		target.hp -= self.attack

		if target.hp <= 0:
			target.location.occupant = None


class Gnome(Fighter):
	def __init__(self, space, attack=3):
		super().__init__(space, attack)
		self.target_klass = Elf

	def is_elf(self):
		return False

	def is_goblin(self):
		return True


class Elf(Fighter):
	def __init__(self, space, attack=3):
		super().__init__(space, attack)
		self.target_klass = Gnome

	def is_elf(self):
		return True

	def is_goblin(self):
		return False


def living_targets(units, target_klass):
	c = 0
	for unit in units:
		if isinstance(unit, target_klass) and unit.is_alive():
			c += 1
	return c


def print_map(map):
	for y in range(len(map)):
		for x, space in enumerate(map[y]):
			if space is None:
				print('#', end='')
			elif space.occupant is None:
				print('.', end='')
			elif space.occupant.is_elf():
				print('E', end='')
			else:
				print('G', end='')
		print('')
	print('')


with open("input", "r") as f:
	map = [list(line.rstrip("\n")) for line in f]

units = []
for y in range(len(map)):
	for x, c in enumerate(map[y]):
		if c == '#':
			map[y][x] = None
			continue

		space = Space(x, y)
		map[y][x] = space

		# Only need to check up and to the left as we build
		if y > 0 and map[y-1][x] is not None:
			map[y-1][x].down = space
			space.up = map[y-1][x]
		if x > 0 and map[y][x-1] is not None:
			map[y][x-1].right = space
			space.left = map[y][x-1]

		if c != '.':
			units.append((c, x, y))

elf_power = 3
starting_elves = sum(1 for unit in units if unit[0] == 'E')
print("Starting Elves: {}".format(starting_elves))
living_elves = 0

while living_elves < starting_elves:
	elf_power += 1

	# Clear the map
	for y in range(len(map)):
		for x, space in enumerate(map[y]):
			if space is not None:
				space.occupant = None

	# Set the units on the map
	game_units = []
	for unit in units:
		if unit[0] == 'E':
			game_units.append(Elf(map[unit[2]][unit[1]], attack=elf_power))
		elif unit[0] == 'G':
			game_units.append(Gnome(map[unit[2]][unit[1]], attack=3))

	# Run the game
	in_combat = True
	rounds = 0
	while in_combat:
		# Order the list of units by row and column (steps in reverse)
		game_units.sort(key=methodcaller('x'))
		game_units.sort(key=methodcaller('y'))

		for unit in game_units:
			if living_targets(game_units, unit.target_klass) == 0:
				in_combat = False
				break

			if unit.is_alive():
				unit.move()
				unit.fight()

		# Increment the number of rounds if we're still in combat
		if in_combat:
			rounds += 1

	# Get the number of living elves
	living_elves = living_targets(game_units, Elf)
else:
	# All elves are still alive
	print_map(map)

	total_hp = sum(max(0, unit.hp) for unit in game_units if unit.is_alive())
	print("Elf Power: {}".format(elf_power))
	print("Living Elves: {}".format(living_elves))
	print("Rounds: {}".format(rounds))
	print("Total HP: {}".format(total_hp))
	print("Outcome: {}".format(rounds * total_hp))
