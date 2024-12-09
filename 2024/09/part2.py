#!/usr/bin/python3

# Brute force was fine for part 1, and it works OK here but takes 16+ seconds to run
# Speeding this up will take refactoring how we're tracking the disk

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

# Compact by moving whole files from the end to the first available block they fit in
file_end_ptr = disk_length - 1
file_start_ptr = None
while file_id > 1:
	file_id -= 1

	while disk[file_end_ptr] != file_id:
		file_end_ptr -= 1

	# Find the start of the current file
	file_start_ptr = file_end_ptr
	while disk[file_start_ptr-1] == file_id:
		file_start_ptr -= 1
	file_len = (file_end_ptr - file_start_ptr) + 1

	# Move the tail pointer to the first available space
	tail_ptr = 0
	found_space = False
	while not found_space:
		while disk[tail_ptr] is not None:
			tail_ptr += 1
		if tail_ptr > file_start_ptr:
			break

		# Speculative - we'll set this to False if it's not found
		found_space = True

		for i in range(1, file_len):
			if disk[tail_ptr+i] is not None:
				# Try again, skipping forward
				tail_ptr += i + 1
				found_space = False
				break
		if found_space or tail_ptr > file_start_ptr:
			break

	# Skip this file if we couldn't find space for it
	if tail_ptr > file_start_ptr:
		continue

	# Move the file
	for i in range(file_len):
		disk[tail_ptr+i] = file_id
		disk[file_start_ptr+i] = None

# Calculate the checksum
checksum = sum(disk[i] * i for i in range(disk_length) if disk[i] is not None)

print("Disk checksum: %d" % (checksum))

end_time = time.time()
print("Elapsed time: %f" % (end_time - start_time))
