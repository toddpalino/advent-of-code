#!/usr/bin/python3

import time

#fn = "test.txt"
fn = "input.txt"

start_time = time.time()

with open(fn, 'r') as f:
	map = f.read().strip()

# Create the full disk
disk_length = sum(int(i) for i in map)
disk = [None] * disk_length

ptr = 0
file_id = 0
for i, num in enumerate(map):
	if i % 2:
		ptr += int(num)
	else:
		file_len = int(num)
		for j in range(file_len):
			disk[ptr+j] = file_id
		ptr += file_len
		file_id += 1

# Compact by moving file blocks from the end to the first available block
tail_ptr = 0
head_ptr = disk_length - 1
while tail_ptr < head_ptr:
	# Move the tail_ptr to point to the first None
	while disk[tail_ptr] is not None:
		tail_ptr += 1

	# Move the head_ptr to point to the last file block
	while disk[head_ptr] is None:
		head_ptr -= 1

	if tail_ptr > head_ptr:
		break

	# Move the block we're on
	disk[tail_ptr] = disk[head_ptr]
	disk[head_ptr] = None

# Calculate the checksum
checksum = sum(disk[i] * i for i in range(tail_ptr))

print("Disk checksum: %d" % (checksum))

end_time = time.time()
print("Elapsed time: %f" % (end_time - start_time))
