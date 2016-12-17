#!/usr/bin/python

import md5

salt = raw_input("Salt: ")

hash_5 = None

idx = 0
while True:
    idx += 1
    hash = md5.new(salt + str(idx)).hexdigest()

    if hash[:5] == "00000":
        if hash[5] == "0":
            print "HASH (6): {0} ({1})".format(hash, idx)
            break
        if hash_5 is None:
            print "HASH (5): {0} ({1})".format(hash, idx)
            hash_5 = hash
