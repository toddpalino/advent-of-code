#!/usr/bin/python

import re
import sys

marker_re = re.compile("\(([0-9]+)x([0-9]+)\)")

# String is (uncompressed part)(marker)(marked string)(String)
# (marked string) is the same
#
# func should decompress a string
#     search for marker
#     if marker
#         append uncompressed part
#         decode marker, pick off marked string
#         append decompress(marked string) repeat times
#         loop with string set to the "rest"
#     else
#         append entire string
#         return (uncompressed strings list, remainder string)
#
# Also, don't really need the string, just a count

def get_str_length(str):
    str_length = 0
    remainder = str

    while remainder != '':
        m = marker_re.search(remainder)
        if m:
            str_length += m.start()

            repeat_len = int(m.group(1))
            uncompressed_length, junk = get_str_length(remainder[m.end():m.end()+repeat_len])
            str_length += uncompressed_length * int(m.group(2))
            remainder = remainder[m.end()+repeat_len:]
        else:
            return len(remainder), ''
    return str_length, remainder[m.end()+repeat_len:]
    
fn = sys.argv[1]
fh = open(fn, "r")
compressed_str = fh.read()
fh.close()

compressed_str = compressed_str.rstrip()
uncompressed_length, remainder = get_str_length(compressed_str)
print uncompressed_length
