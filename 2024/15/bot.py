def move_lateral(r, grid, v):
	# We know this is always left and right, so we don't need to adjust y position
	n = 0
	next_x, y = r
	while True:
		next_x = next_x+v[0]
		c = grid[y][next_x]
		if c in ('[', ']'):
			n += 1
		elif c == '#':
			n = None
			break
		elif c == '.':
			break

	if n is None:
		# Can't move, blocked by a wall
		return

	# Move Everything
	for i in range(n+1, 0, -1):
		x = r[0] + (i * v[0])
		grid[y][x] = grid[y][x-v[0]]

	# Robot's position always gets a blank spot
	grid[r[1]][r[0]] = '.'
	r[0] += v[0]


def move_vertical(r, grid, v):
	# width will contain, per row we are moving (first row is (0, 0) for the robot) a
	# range to move For example, if we move the block directly above the robot and 1
	# to the left, the # entry will be (1, 0). If it was 2 to the left and 2 to the
	# right, (2, 2)
	width = [[0, 0]]
	rx, ry = r
	while True:
		ry = ry+v[1]
		last_range = width[-1]
		next_range = width[-1].copy()
		row_empty = True

		# Using a list here so it's easy to know when we're on the first one
		check = list(range(rx - last_range[0], rx + last_range[1] + 1))

		for i, x in enumerate(check):
			c = grid[ry][x]
			if c == '#':
				# Wall in our way. No move
				width = None
				break
			elif c == ']':
				if i == 0:
					# Picked up another box
					next_range[0] += 1
				row_empty = False
			elif c == '[':
				if i == (len(check) - 1):
					# Picked up another box
					next_range[1] += 1
				row_empty = False
			elif c == '.' and row_empty:
				# This row is shorter on the "left" side
				next_range[0] -= 1

		if row_empty or width is None:
			break

		# Need to check if the row is shorter on the "right" by working backwards
		for x in check[::-1]:
			if grid[ry][x] == '.':
				next_range[1] -= 1
			else:
				break

		width.append(next_range)

	if width is None:
		# Can't move, blocked by a wall
		return

	ry = r[1] + len(width) * v[1]
	for w in range(len(width) - 1, -1, -1):
		move_range = width[w]

		for x in range(rx - move_range[0], rx + move_range[1] + 1):
			# Copy the grid block below this (if the vector is up) to this location
			grid[ry][x] = grid[ry-v[1]][x]

		if w < (len(width) - 1):
			# Except for the first row we move, we need to check if the row "above" us was wider,
			# in which case we need to write in spaces on the left and right
			last_range = width[w+1]

			for x in range(rx - last_range[0], rx - move_range[0]):
				grid[ry][x] = '.'
			for x in range(rx + move_range[1] + 1, rx + last_range[1] + 1):
				grid[ry][x] = '.'
		ry -= v[1]

	# Move the robot position
	grid[r[1]][r[0]] = '.'
	r[1] += v[1]
