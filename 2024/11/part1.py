#!/usr/bin/python3

import time

#fn = "test.txt"
#iterations = 6

fn = "input.txt"
iterations = 25

class Stone:
	def __init__(self, num):
		self.num = num
		self.left = None
		self.right = None

def print_stones(head):
	nums = []
	ptr = head
	while ptr is not None:
		nums.append(ptr.num)
		ptr = ptr.right
	print(' '.join(nums))

def strip_extra_zeros(s):
	new_s = s.lstrip('0')
	return new_s if len(new_s) > 0 else '0'

start_time = time.time()

with open(fn, 'r') as f:
	# Storing these as strings since most of the time we want string manip
	stones = [Stone(n) for n in f.read().strip().split()]

for i in range(len(stones)):
	if i > 0:
		stones[i].left = stones[i-1]
	if i < (len(stones) - 1):
		stones[i].right = stones[i+1]
head = stones[0]

for _ in range(iterations):
	ptr = head
	next_ptr = None
	while ptr is not None:
		next_ptr = ptr.right

		num = ptr.num
		if num == '0':
			ptr.num = '1'
		elif len(num) % 2 == 0:
			halfway = len(num) // 2
			ptr.num = strip_extra_zeros(num[0:halfway])
			ptr.right = Stone(strip_extra_zeros(num[halfway:]))
			ptr.right.left = ptr
			ptr.right.right = next_ptr
		else:
			ptr.num = str(int(ptr.num) * 2024)

		ptr = next_ptr

count = 0
ptr = head
while ptr is not None:
	ptr = ptr.right
	count += 1

print("Number of stones: %d" % (count))

end_time = time.time()
print("Elapsed time: %f" % (end_time - start_time))
