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
		if self.occupied and neighbors >= 4:
			self.next_occupied = False
			return True
		return False

	def switch_state(self):
		self.occupied = self.next_occupied


#with open("test.txt") as f:
with open("input.txt") as f:
	grid = [list(line.strip()) for line in f]

# Create seats
seats = {}
for y in range(len(grid)):
	for x in range(len(grid[0])):
		if grid[y][x] == 'L':
			seats[(x, y)] = Seat(x, y)

# Link adjacent seats
for seat in seats.values():
	for neighbor in ((seat.x-1, seat.y-1), (seat.x-1, seat.y),
                         (seat.x-1, seat.y+1), (seat.x, seat.y-1),
                         (seat.x, seat.y+1), (seat.x+1, seat.y-1),
                         (seat.x+1, seat.y), (seat.x+1, seat.y+1)):
		try:
			seat.adjacent.append(seats[neighbor])
		except KeyError:
			# Just ignore seats that don't exist
			pass

while True:
	changes = sum(seat.set_next_state() for seat in seats.values())
	if changes == 0:
		# Reached a stable state
		break
	for seat in seats.values():
		seat.switch_state()

print(sum(seat.occupied for seat in seats.values()))
