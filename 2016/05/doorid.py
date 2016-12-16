#!/usr/bin/python

import md5

door_name = raw_input("Door ID: ")

idx = -1
for pos in range(8):
    while True:
        idx += 1
        hash = md5.new(door_name + str(idx)).hexdigest()

        if hash[:5] != "00000":
            continue
        print "{0} (ITER {1})".format(hash[5], idx)
        break
