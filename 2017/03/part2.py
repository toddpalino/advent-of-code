#!/usr/bin/python

import sys

target = 347991

cols = 11
matrix = []
for i in range(cols):
	matrix.append([0] * cols)

matrix[cols / 2][cols / 2] = 1
x = (cols / 2) + 1
y = cols / 2

for n in range((cols * cols) - 1):
	matrix[x][y] = sum([matrix[a][b] for a in (x-1, x, x+1) for b in (y-1, y, y+1) if (a < len(matrix)) and (b < len(matrix[a]))])
	if matrix[x][y] > target:
		print(matrix[x][y])
		sys.exit(0)
	if ((y - 1 >= 0) and (matrix[x][y-1] == 0)) and ((x - 1 >= 0) and (matrix[x-1][y] != 0)):
		y -= 1
	elif ((y + 1 < cols) and (matrix[x][y+1] == 0)) and ((x + 1 < cols) and (matrix[x+1][y] != 0)):
		y += 1
	elif ((y + 1 < cols) and (matrix[x][y+1] != 0)) and ((x - 1 >= 0) and (matrix[x-1][y] == 0)):
		x -= 1
	elif ((y - 1 >= 0) and (matrix[x][y-1] != 0)) and ((x + 1 < cols) and (matrix[x+1][y] == 0)):
		x += 1
