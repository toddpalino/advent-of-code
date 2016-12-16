#!/usr/bin/python

import md5
import sys

door_name = raw_input("Door ID: ")

def show_code(code):
    sys.stdout.write("{0} (ITER {1})\r".format(''.join(code), idx))
    #sys.stdout.flush()

idx = -1
code = ['_', '_', '_', '_', '_', '_', '_', '_']
locked = [False, False, False, False, False, False, False, False]

for c in range(8):
    while True:
        idx += 1
        hash = md5.new(door_name + str(idx)).hexdigest()

        try:
            pos = int(hash[5])
        except ValueError:
            continue
        if pos > 7:
            continue

        if not locked[pos]:
            code[pos] = hash[6]
        show_code(code)
        if hash[:5] != "00000":
            continue

        if not locked[pos]:
            locked[pos] = True
            show_code(code)
            break

sys.stdout.write("{0} (ITER {1})\n".format(''.join(code), idx))
