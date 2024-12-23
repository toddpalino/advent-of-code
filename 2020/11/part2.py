#!/usr/bin/python3

class Seat:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.occupied = False
		self.next_occupied = False
		self.adjacent = []

	# Set the next state for this seat, and return True if there is a change
	def set_next_state(self):
		neighbors = sum(neighbor.occupied for neighbor in self.adjacent)
		if not self.occupied and neighbors == 0:
			self.next_occupied = True
			return True
		if self.occupied and neighbors >= 5:
			self.next_occupied = False
			return True
		return False

	def switch_state(self):
		self.occupied = self.next_occupied


#with open("test.txt") as f:
with open("input.txt") as f:
	grid = [list(line.strip()) for line in f]

max_y = len(grid)
max_x = len(grid[0])
max_incr = max(max_x, max_y)

# Create seats
seats = {}
for y in range(max_y):
	for x in range(max_x):
		if grid[y][x] == 'L':
			seats[(x, y)] = Seat(x, y)

# Link visible seats
for seat in seats.values():
	x = seat.x
	y = seat.y
	for change in ((-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, 1), (1, -1)):
		for incr in range(1, max_incr):
			try_x = x + (change[0] * incr)
			try_y = y + (change[1] * incr)
			if (0 <= try_x < max_x) and (0 <= try_y < max_y):
				try:
					seat.adjacent.append(seats[(try_x, try_y)])
					break
				except KeyError:
					continue
			else:
				break

while True:
	changes = sum(seat.set_next_state() for seat in seats.values())
	if changes == 0:
		# Reached a stable state
		break
	for seat in seats.values():
		seat.switch_state()

print(sum(seat.occupied for seat in seats.values()))
