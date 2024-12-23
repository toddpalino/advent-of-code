#!/usr/bin/python3

import time
from collections import deque

# Real Input
filename = "input.txt"

# Test Input
#filename = "test.txt"

class Brick:
	def __init__(self, brick_id, corner1, corner2):
		self._id = brick_id
		self.x1 = corner1[0]
		self.x2 = corner2[0]
		self.y1 = corner1[1]
		self.y2 = corner2[1]
		self.z1 = corner1[2]
		self.z2 = corner2[2]

		self.supports = set([])
		self.supported_by = set([])

	def move_down(self, to):
		diff = self.z1 - to
		self.z2 -= diff
		self.z1 -= diff

	def intersects(self, brick):
		# The x and y ranges need to interact somewhere, at least once
		return (len(set(range(self.x1, self.x2+1)) & set(range(brick.x1, brick.x2+1))) > 0 and
			len(set(range(self.y1, self.y2+1)) & set(range(brick.y1, brick.y2+1))) > 0)

	def __repr__(self):
		return "(Brick %d (%d, %d, %d) - (%d, %d, %d))" % (self._id, self.x1, self.y1, self.z1, self.x2, self.y2, self.z2)


t1 = time.process_time()

i = 0
bricks = []
with open(filename) as f:
	for line in f:
		coords = line[0:-1].split('~')
		bricks.append(Brick(i, [int(x) for x in coords[0].split(',')], [int(x) for x in coords[1].split(',')]))
		i += 1

max_x = max(brick.x2 for brick in bricks) + 1
max_y = max(brick.y2 for brick in bricks) + 1
max_z = max(brick.z2 for brick in bricks) + 1

top_at_z = [set([]) for _ in range(max_z)]
for brick in bricks:
	top_at_z[brick.z2].add(brick)

# For each brick, figure out what it is supported by. Move from the bottom up
for z in range(1, max_z):
	for brick in list(top_at_z[z]):
		for dz in range(brick.z1-1, -1, -1):
			move_to = 1 if dz == 0 else None
			supports = set(lower_brick for lower_brick in top_at_z[dz] if brick.intersects(lower_brick))

			if supports:
				brick.supported_by = supports
				for lower_brick in supports:
					lower_brick.supports.add(brick)
				move_to = dz + 1
			if move_to is not None:
				top_at_z[z].remove(brick)
				brick.move_down(move_to)
				top_at_z[brick.z2].add(brick)
				break

# A brick will move if everything that supports it moves
sum_moves = 0
for brick in bricks:
	moves = set([brick])
	queue = deque(brick.supports)
	while queue:
		brick_above = queue.popleft()
		if brick_above.supported_by.issubset(moves):
			moves.add(brick_above)
			queue.extend(brick_above.supports)
	sum_moves += len(moves) - 1

t2 = time.process_time()

print("Sum of chain reactions: %d" % (sum_moves))
print("Time: %f" % (t2 - t1))
