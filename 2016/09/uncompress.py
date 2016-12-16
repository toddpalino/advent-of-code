#!/usr/bin/python

import re
import sys

marker_re = re.compile("\(([0-9]+)x([0-9]+)\)")

fn = sys.argv[1]
fh = open(fn, "r")
compressed_str = fh.read()
fh.close()

compressed_str = compressed_str.rstrip()
uncompressed = []

start_idx = 0
while True:
    m = marker_re.search(compressed_str, start_idx)
    if m:
        print "{0} {1} {2}".format(start_idx, m.start(), m.end())
        uncompressed.append(compressed_str[start_idx:m.start()])
        repeat_len = int(m.group(1))
        repeat_str = compressed_str[m.end():m.end()+repeat_len]
        for i in range(int(m.group(2))):
            uncompressed.append(repeat_str)
        start_idx = m.end() + repeat_len
    else:
        uncompressed.append(compressed_str[start_idx:])
        break

str = ''.join(uncompressed)
print str
print len(str)
