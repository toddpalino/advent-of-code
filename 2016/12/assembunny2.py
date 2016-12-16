#!/usr/bin/python

import re
import sys

marker_re = re.compile("\(([0-9]+)x([0-9]+)\)")

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

instructions = []
for ln in fh.readlines():
    instructions.append(ln.strip())

fh.close()

register = {
    'a': 0,
    'b': 0,
    'c': 1,
    'd': 0
}

ptr = 0
while ptr < len(instructions):
    cmd = instructions[ptr].split(' ')
    if cmd[0] == 'cpy':
        val = register[cmd[1]] if cmd[1] in register else int(cmd[1])
        register[cmd[2]] = val
    elif cmd[0] == 'inc':
        register[cmd[1]] = register[cmd[1]] + 1
    elif cmd[0] == 'dec':
        register[cmd[1]] = register[cmd[1]] - 1
    elif cmd[0] == 'jnz':
        tst = register[cmd[1]] if cmd[1] in register else int(cmd[1])
        if tst != 0:
            ptr += int(cmd[2])
            continue
    ptr += 1

print register
