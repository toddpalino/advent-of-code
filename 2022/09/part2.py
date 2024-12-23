#!/usr/bin/python3


def get_next_position(head, tail):
	move_x = 0
	move_y = 0
	if head[0] > (tail[0]+1):
		move_x = 1
		move_y = head[1] - tail[1]
		if move_y > 0:
			move_y = 1
		elif move_y < 0:
			move_y = -1
	elif head[0] < (tail[0]-1):
		move_x = -1
		move_y = head[1] - tail[1]
		if move_y > 0:
			move_y = 1
		elif move_y < 0:
			move_y = -1
	elif head[1] > (tail[1]+1):
		move_y = 1
		move_x = head[0] - tail[0]
	elif head[1] < (tail[1]-1):
		move_y = -1
		move_x = head[0] - tail[0]
	new_tail = (tail[0] + move_x, tail[1] + move_y)
	return new_tail


num_knots = 10
knots = [(0, 0) for _ in range(num_knots)]
tail_visited = set([(0, 0)])

with open("input.txt") as f:
	for line in f:
		parts = line.strip().split(' ')
		direction = parts[0]
		steps = int(parts[1])

		for i in range(steps):
			# Move head
			head_x = knots[0][0]
			head_y = knots[0][1]
			if direction == 'U':
				head_y += 1
			if direction == 'D':
				head_y -= 1
			if direction == 'R':
				head_x += 1
			if direction == 'L':
				head_x -= 1
			knots[0] = (head_x, head_y)

			# Move the other knots
			for i in range(1, num_knots):
				knots[i] = get_next_position(knots[i-1], knots[i])

			tail_visited.add(knots[-1])

print(len(tail_visited))
