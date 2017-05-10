#!/usr/bin/python

from copy import deepcopy

max_x = 100
max_y = 100

def sum_neighbors(lights, x, y):
    total = 0
    for i in [x-1, x, x+1]:
        for j in [y-1, y, y+1]:
            if i == x and j == y:
                continue
            if i >= 0 and j >= 0 and i < max_x and j < max_y:
                total += lights[j][i]
    return total

lights = [[]]
with open('configuration') as f:
    for line in f:
        lights[0].append([1 if status == '#' else 0 for status in line.strip()])

# Set broken lights on
lights[0][0][0] = 1
lights[0][0][max_x-1] = 1
lights[0][max_y-1][0] = 1
lights[0][max_y-1][max_x-1] = 1

lights.append(deepcopy(lights[0]))

ticks = int(raw_input("Number of steps: "))

start = 0
finish = 1
for i in range(ticks):
    for y in range(max_y):
        for x in range(max_x):
            neighbors = sum_neighbors(lights[start], x, y)

            # Never change the 4 corners
            if x in [0, max_x-1] and y in [0, max_y-1]:
                continue

            if lights[start][y][x] == 1:
                lights[finish][y][x] = 1 if neighbors in [2, 3] else 0
            elif neighbors == 3:
                lights[finish][y][x] = 1
            else:
                lights[finish][y][x] = 0
    start, finish = finish, start

count = sum(map(sum, lights[start]))

for row in lights[start]:
    print ''.join(['#' if light == 1 else '.' for light in row])
print "LIGHTS: {0}".format(count)

