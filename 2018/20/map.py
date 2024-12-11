#!/usr/bin/python3

# We're going to put IDs on every door and room so we can track whether we've walked through it
# Note - This is NOT thread safe
global_door_id = 0
global_room_id = 0

opposite = {
	'N': 'S',
	'S': 'N',
	'E': 'W',
	'W': 'E'
}

class Choices:
	def __init__(self):
		self.choices = [[]]

	def get_side(self, side):
		return self.choices[side][-1]

	def __repr__(self):
		return f"(C: {self.choices})"


class Room:
	def __init__(self):
		global global_room_id

		self.connections = {
			'N': None,
			'S': None,
			'E': None,
			'W': None
		}
		self.door_ids = {
			'N': None,
			'S': None,
			'E': None,
			'W': None
		}
		self.room_id = global_room_id
		global_room_id += 1

	def build_walk(self, dir):
		global global_door_id

		if self.connections[dir] is None:
			self.connections[dir] = Room()
			self.door_ids[dir] = global_door_id
			self.connections[dir].connections[opposite[dir]] = self
			self.connections[dir].door_ids[opposite[dir]] = global_door_id
			global_door_id += 1
		return self.connections[dir]

	def can_walk(self, dir):
		return self.connections[dir] is not None

	def doors(self):
		return [(v, self.door_ids[k]) for k,v in self.connections.items() if v is not None]

	def walk(self, dir):
		new_room = self.connections[dir]
		if new_room is none:
			raise ValueError()
		return self.connections[dir]


def get_choice_at_depth(groups, depth):
	for i in range(len(depth) - 1):
		groups = groups.choices[depth[i]][-1]
	return groups


def append_at_depth(item, groups, depth):
	choice = depth[-1]
	groups = get_choice_at_depth(groups, depth)
	groups.choices[choice].append(item)


def add_option_at_depth(groups, depth):
	groups = get_choice_at_depth(groups, depth)
	groups.choices.append([])


# This parser assumes balanced parentheses, and so it does not error check that
def parse_directions(s):
	groups = Choices()
	len_s = len(s) - 1

	# Depth is a stack (pop/append on right) where the number is the choice side at that depth
	depth = [0]

	# Start at 1 to ignore the ^ and $
	i = 1
	while i < len_s:
		# Consume characters until we get a symbol
		j = i
		while j < len_s and s[j] not in ('(', ')', '|'):
			j += 1

		# Add the consumed string at the current depth
		append_at_depth(s[i:j], groups, depth)
		i = j

		# Handle the symbol
		if i < len_s:
			while s[i] in ('(', ')', '|'):
				if s[i] == '(':
					append_at_depth(Choices(), groups, depth)
					depth.append(0)
				elif s[i] == ')':
					depth.pop()
				else:
					add_option_at_depth(groups, depth)
					depth[-1] += 1
				i += 1

	return groups


def follow_directions(ptr, directions):
	for item in directions:
		if isinstance(item, str):
			for c in item:
				ptr = ptr.build_walk(c)
		else:
			for opt in item.choices:
				follow_directions(ptr, opt)

def build_map(dir_string):
	directions = parse_directions(dir_string)

	home = Room()
	for opt in directions.choices:
		follow_directions(home, opt)
	return home
