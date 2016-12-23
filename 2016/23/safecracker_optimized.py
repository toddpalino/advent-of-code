#!/usr/bin/python

keypad = int(raw_input("Keypad: "))

# This is the optimized version of the instructions provided
# Using the opcodes, we need over 3.5 billion operations
# This is *slightly* faster

a = keypad
b = a - 1
for i in range(b, 0, -1):
    a = a * i
a += 71 * 73

print "CODE: {0}".format(a)
