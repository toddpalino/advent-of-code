#!/usr/bin/python

from copy import deepcopy

input = ".^^.^^^..^.^..^.^^.^^^^.^^.^^...^..^...^^^..^^...^..^^^^^^..^.^^^..^.^^^^.^^^.^...^^^.^^.^^^.^.^^.^."
rowlen = len(input)
room = [[True if c == '^' else False for c in list(input)]]

rows = int(raw_input("Number of rows: "))

for i in range(1, rows):
    room.append(deepcopy(room[i-1]))
    for j in range(rowlen):
        left = False if j == 0 else (True if room[i-1][j-1] else False)
        center = room[i-1][j]
        right = False if j == (rowlen-1) else (True if room[i-1][j+1] else False)
        room[i][j] = (left and center and (not right)) or (center and right and (not left)) or (left and (not right) and (not center)) or (right and (not left) and (not center))

safe = 0
for i in range(len(room)):
    for j in range(len(room[i])):
        if not room[i][j]:
            safe += 1

print "SAFE: {0}".format(safe)
