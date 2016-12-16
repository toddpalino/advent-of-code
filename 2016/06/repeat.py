#!/usr/bin/python

import sys

frequency = []
for ln in sys.stdin.readlines():
    line = ln.strip()
    for pos, char in enumerate(line):
        if pos >= len(frequency):
            frequency.append({})
        frequency[pos][char] = 1 if char not in frequency[pos] else frequency[pos][char] + 1

message = []
for letters in frequency:
    message.append(sorted(letters, key=letters.get, reverse=True)[0])

print "{0}".format(''.join(message))
