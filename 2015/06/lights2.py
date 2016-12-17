#!/usr/bin/python

grid = [[0 for x in range(1000)] for y in range(1000)]

def get_coords(arguments):
    coord_1 = [int(x) for x in arguments[0].split(',')]
    coord_2 = [int(x) for x in arguments[2].split(',')]
    return coord_1, coord_2

with open('instructions') as f:
    for line in f:
        cmd = line.strip().split(' ')
        
        val = None
        coord_1 = None
        coord_2 = None
        if cmd[0] == 'toggle':
            val = 2
            coord_1, coord_2 = get_coords(cmd[1:])
        elif cmd[0] == 'turn':
            val = 1 if cmd[1] == 'on' else -1
            coord_1, coord_2 = get_coords(cmd[2:])

        for x in range(coord_1[0], coord_2[0]+1):
            for y in range(coord_1[1], coord_2[1]+1):
                grid[x][y] = max(0, grid[x][y] + val)

lights = sum(map(sum, grid))
print "BRIGHTNESS: {0}".format(lights)
