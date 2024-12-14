def chunk_list(lst, n):
	"""Yield successive n-sized chunks from lst."""
	for i in range(0, len(lst), n):
		yield lst[i:i + n]

def position_at_tick(tick, len_x, len_y, x, y, dx, dy):
	new_x = (x + (tick * dx)) % len_x
	new_y = (y + (tick * dy)) % len_y
	return (new_x, new_y)

def quadrant_counts(positions, len_x, len_y):
	mid_x = len_x // 2
	mid_y = len_y // 2
	counts = [0, 0, 0, 0]

	for p in positions:
		if p[0] == mid_x or p[1] == mid_y:
			continue

		q = 0
		if p[0] < mid_x:
			q = 1
		elif p[0] > mid_x:
			q = 2
		if p[1] < mid_y:
			pass
		elif p[1] > mid_y:
			q += 2
		counts[q-1] += 1

	return counts

def print_bots(positions, len_x, len_y):
	for y in range(len_y):
		print(''.join('*' if (x, y) in positions else ' ' for x in range(len_x)))
