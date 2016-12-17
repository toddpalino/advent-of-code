#!/usr/bin/python

import re

start = raw_input("Input: ")
times = int(raw_input("Times: "))

group_re = re.compile(r'((\d)\2*)')

print "STEP 0 - LEN {0}".format(len(start))
for i in range(times):
    newstring = ''
    for group in group_re.finditer(start):
        newstring += str(len(group.group(1))) + group.group(2)
    start = newstring
    print "STEP {0} - LEN {1}".format(i, len(start))
