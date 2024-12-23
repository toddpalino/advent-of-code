#!/usr/bin/python3

head_x = 0
head_y = 0
tail_x = 0
tail_y = 0
tail_visited = set([(0, 0)])

with open("input.txt") as f:
	for line in f:
		parts = line.strip().split(' ')
		direction = parts[0]
		steps = int(parts[1])

		for i in range(steps):
			if direction == 'U':
				head_y += 1
			if direction == 'D':
				head_y -= 1
			if direction == 'R':
				head_x += 1
			if direction == 'L':
				head_x -= 1

			# This will give a right answer for the 12 possible positions
			move_x = 0
			move_y = 0
			if head_x > (tail_x+1):
				move_x = 1
				move_y = head_y - tail_y
			elif head_x < (tail_x-1):
				move_x = -1
				move_y = head_y - tail_y
			elif head_y > (tail_y+1):
				move_y = 1
				move_x = head_x - tail_x
			elif head_y < (tail_y-1):
				move_y = -1
				move_x = head_x - tail_x

			tail_x += move_x
			tail_y += move_y
			tail_visited.add((tail_x, tail_y))

print(len(tail_visited))
