#!/usr/bin/python

import re
import sys

name_re = re.compile("^([a-z-]+)-([0-9]+)\[([a-z]+)\]$")

real_rooms = []
for ln in sys.stdin.readlines():
    line = ln.strip()
    m = name_re.match(line)
    if m is None:
        print "BAD: {0}".format(line)
        continue

    counts = {}
    for letter in list(m.group(1)):
        if letter == "-":
            continue
        counts[letter] = 1 if letter not in counts else counts[letter] + 1
    letters = counts.keys()
    s1 = sorted(letters)
    s2 = sorted(s1, key=lambda x: counts[x], reverse=True)
    #print "{0} -> {1} -> {2}".format(counts, ''.join(s1), ''.join(s2))

    checksum_calc = ''.join(s2)[0:5]
    if checksum_calc == m.group(3):
         print "REAL:  {0}".format(line)
         real_rooms.append((m.group(1), int(m.group(2))))

for room in real_rooms:
    room_name = []
    rot = room[1] % 26
    for letter in list(room[0]):
        if letter == "-":
            room_name.append(" ")
        else:
            room_name.append(chr((((ord(letter) - 97) + rot) % 26) + 97))

    print "{0} ({1})".format(''.join(room_name), room[1])
