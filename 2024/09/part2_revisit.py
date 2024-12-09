#!/usr/bin/python3

# An OOP approach to handling the disk for part 2. This runs in under 6 seconds, which is a big
# improvement

import time

# We'll represent the disk with a doubly linked list. That will make it easy
# to work backwards
class SpaceBlock:
	def __init__(self, file_length, previous, file_id=None):
		# If file_id is None, it's blank space
		self.file_id = file_id
		self.file_length = file_length
		self.prev = previous
		self.next = None

	def checksum(self, disk_pos):
		if self.file_id is None:
			return 0
		return self.file_id * sum(range(disk_pos, disk_pos + self.file_length))

	def __repr__(self):
		if self.file_id is None:
			return f"EMPTY len={self.file_length}"
		else:
			return f"FILE id={self.file_id} len={self.file_length}"

# We will call this as we walk back the tail pointer. This takes care of making sure that
# we never have a cached size_ptr that is past the tail
def invalidate_cached_pointers(pointer_list, ptr):
	try:
		idx = pointer_list.index(ptr)
		pointer_list[idx] = None
	except ValueError:
		pass


#fn = "test.txt"
fn = "input.txt"

start_time = time.time()

with open(fn, 'r') as f:
	map = f.read().strip()

# Create the full disk
head = SpaceBlock(int(map[0]), None, file_id=0)
tail = head
file_id = 1
for i in range(1, len(map)):
	if i % 2:
		tail.next = SpaceBlock(int(map[i]), tail)
	else:
		tail.next = SpaceBlock(int(map[i]), tail, file_id=file_id)
		file_id += 1
	tail = tail.next

# We will use this as a cache of the earliest possible place empty space of a given size
# could be. This allows us to avoid searching from head every time.
size_ptr = [head] * 10

file_id -= 1
# Compact by moving whole files from the end to the first available block they fit in
while tail != head:
	# Move the tail to the next file back from the end
	while tail.file_id is None or tail.file_id != file_id:
		invalidate_cached_pointers(size_ptr, tail)
		tail = tail.prev

	# Find the first available block of space that fits this file
	ptr = size_ptr[tail.file_length]
	if ptr is None:
		# We've already exhausted availability for this size. Move on.
		file_id -= 1
		continue

	while ptr.file_id is not None or ptr.file_length < tail.file_length:
		ptr = ptr.next

		# If we get to the file we're working on, we need to bail
		if ptr == tail:
			break

	if ptr == tail:
		# We can't find any more space of this size. Update the cache and move on
		size_ptr[tail.file_length] = None
		file_id -= 1
		continue

	# Remove the file from where it is, replacing it with blank space
	file_to_move = tail
	if tail.prev.file_id is None and tail.next is not None and tail.next.file_id is None:
		# Remove both the file and the following blank space, adding it onto prev
		tail.prev.file_length += file_to_move.file_length + tail.next.file_length
		invalidate_cached_pointers(size_ptr, tail)
		tail = tail.prev
		tail.next = tail.next.next.next
		if tail.next is not None:
			tail.next.prev = tail
	elif tail.prev.file_id is None:
		# Add the free space onto prev
		tail.prev.file_length += file_to_move.file_length
		invalidate_cached_pointers(size_ptr, tail)
		tail = tail.prev
		tail.next = tail.next.next
		if tail.next is not None:
			tail.next.prev = tail
	elif tail.next is not None and tail.next.file_id is None:
		# Add the free space onto next
		tail.next.file_length += file_to_move.file_length
		invalidate_cached_pointers(size_ptr, tail)
		tail = tail.prev
		tail.next = tail.next.next
		tail.next.prev = tail
	else:
		# Replace the file with blank space, since it's between 2 files
		new_block = SpaceBlock(tail.file_length, tail.prev)
		tail.prev.next = new_block
		new_block.next = tail.next
		if tail.next is not None:
			tail.next.prev = new_block
		invalidate_cached_pointers(size_ptr, tail)
		tail = tail.prev

	if ptr.file_length == file_to_move.file_length:
		# Just make the blank space our file
		ptr.file_id = file_to_move.file_id
	else:
		# Insert the file before the blank space found, shortening the blank space
		ptr.file_length -= file_to_move.file_length
		ptr.prev.next = file_to_move
		file_to_move.prev = ptr.prev
		ptr.prev = file_to_move
		file_to_move.next = ptr

	# Update the size_ptr cache to where we moved the file back to
	size_ptr[file_to_move.file_length] = ptr
	file_id -= 1

# Calculate the checksum
disk_ptr = 0
checksum = 0
ptr = head
while ptr is not None:
	checksum += ptr.checksum(disk_ptr)
	disk_ptr += ptr.file_length
	ptr = ptr.next

print("Disk checksum: %d" % (checksum))

end_time = time.time()
print("Elapsed time: %f" % (end_time - start_time))
