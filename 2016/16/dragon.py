#!/usr/bin/python

def dragon(a):
    b = ['1' if c == '0' else '0' for c in a[::-1]]
    return a + ['0'] + b

def generate_data(seed, needed):
    dragon_chars = list(seed)
    while len(dragon_chars) < needed:
        dragon_chars = dragon(dragon_chars)
    return dragon_chars[:needed]

def checksum(dragon_chars):
    while True:
        sum_chars = []
        for i in range(0, len(dragon_chars), 2):
            pair = dragon_chars[i:i+2]
            sum_chars.append('1' if pair[0] == pair[1] else '0')
        if len(sum_chars) % 2 != 1:
            dragon_chars = sum_chars
        else:
            return sum_chars

#data = generate_data("10000", 20)
#data = generate_data("00111101111101000", 272)
data = generate_data("00111101111101000", 35651584)
#print "DATA: {0}".format(''.join(data))

check = checksum(data)
print "CHECKSUM: {0}".format(''.join(check))
