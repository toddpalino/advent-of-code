#!/usr/bin/python

code_len = 0
mem_len = 0
enc_len = 0
with open('strings') as f:
    for line in f:
        line_len = len(line)
        code_len += line_len - 1

        mem_len += len(line[1:line_len-2].decode('string_escape'))
        enc_len += len(line[0:line_len-1].encode('string_escape')) + 2 + line[0:line_len-1].count('"')

print "CODE: {0}".format(code_len)
print "MEM: {0}".format(mem_len)
print "ENC: {0}".format(enc_len)
print "CODE - MEM: {0}".format(code_len - mem_len)
print "ENC - CODE: {0}".format(enc_len - code_len)
