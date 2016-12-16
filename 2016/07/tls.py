#!/usr/bin/python

import re
import sys

def has_abba(str):
    for i in range(len(str)):
        substr = str[i:i+4]
        if len(substr) < 4:
            return False
        if (substr[0] == substr[3]) and (substr[1] == substr[2]) and (substr[0] != substr[1]):
            return True
    return False

substr_re = re.compile("[a-z]+")

tls_support = []
for ln in sys.stdin.readlines():
    valid = False
    for i, sub_ip in enumerate(substr_re.findall(ln)):
        if has_abba(sub_ip):
            if i % 2 == 0:
                valid = True
            else:
                valid = False
                break

    if valid:
        tls_support.append(ln.strip())

print "---"
print "\n".join(tls_support)
print len(tls_support)
