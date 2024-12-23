#!/usr/bin/python3

with open('input.txt') as f:
	buffer = f.read().strip()

packet = None
message = None
for i in range(len(buffer)):
	if packet is None and i >= 4:
		if len(set(buffer[i-4:i])) == 4:
			packet = i
	if message is None and i >= 14:
		if len(set(buffer[i-14:i])) == 14:
			message = i

print("Start of packet after: %d" % (packet))
print("Start of message after: %d" % (message))
