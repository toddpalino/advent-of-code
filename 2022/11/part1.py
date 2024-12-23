#!/usr/bin/python3

import types


class Monkey:
	def __init__(self, monkey_id, items, test_divisor, change_modifier=None):
		self._id = monkey_id
		self.items = items
		self.test_divisor = test_divisor
		self.change_modifier = change_modifier
		self.inspected = 0

		# These will be replaced after creation
		self.target_true = None
		self.target_false = None

	def receive(self, item):
		self.items.append(item)

	def worry_change(self, item):
		# We need to replace this for at least one monkey
		return item + self.change_modifier

	def run(self):
		for _ in range(len(self.items)):
			self.inspected += 1
			item = self.items.pop(0)
			item = self.worry_change(item)
			item = item // 3
			if (item % self.test_divisor) == 0:
				self.target_true.receive(item)
			else:
				self.target_false.receive(item)


# Alternate worry_change functions
def worry_change_squared(self, item):
	return item * item
def worry_change_multiply(self, item):
	return item * self.change_modifier

# Test Setup
test_monkeys = [
	Monkey(0, [79, 98], 23, 19),
	Monkey(1, [54, 65, 75, 74], 19, 6),
	Monkey(2, [79, 60, 97], 13),
	Monkey(3, [74], 17, 3)
]
test_monkeys[0].target_true = test_monkeys[2]
test_monkeys[0].target_false = test_monkeys[3]
test_monkeys[1].target_true = test_monkeys[2]
test_monkeys[1].target_false = test_monkeys[0]
test_monkeys[2].target_true = test_monkeys[1]
test_monkeys[2].target_false = test_monkeys[3]
test_monkeys[3].target_true = test_monkeys[0]
test_monkeys[3].target_false = test_monkeys[1]
test_monkeys[0].worry_change = types.MethodType(worry_change_multiply, test_monkeys[0])
test_monkeys[2].worry_change = types.MethodType(worry_change_squared, test_monkeys[2])

# Real setup
real_monkeys = [
	Monkey(0, [63, 84, 80, 83, 84, 53, 88, 72], 13, 11),
	Monkey(1, [67, 56, 92, 88, 84], 11, 4),
	Monkey(2, [52], 2),
	Monkey(3, [59, 53, 60, 92, 69, 72], 5, 2),
	Monkey(4, [61, 52, 55, 61], 7, 3),
	Monkey(5, [79, 53], 3, 1),
	Monkey(6, [59, 86, 67, 95, 92, 77, 91], 19, 5),
	Monkey(7, [58, 83, 89], 17, 19)
]
real_monkeys[0].target_true = real_monkeys[4]
real_monkeys[0].target_false = real_monkeys[7]
real_monkeys[1].target_true = real_monkeys[5]
real_monkeys[1].target_false = real_monkeys[3]
real_monkeys[2].target_true = real_monkeys[3]
real_monkeys[2].target_false = real_monkeys[1]
real_monkeys[3].target_true = real_monkeys[5]
real_monkeys[3].target_false = real_monkeys[6]
real_monkeys[4].target_true = real_monkeys[7]
real_monkeys[4].target_false = real_monkeys[2]
real_monkeys[5].target_true = real_monkeys[0]
real_monkeys[5].target_false = real_monkeys[6]
real_monkeys[6].target_true = real_monkeys[4]
real_monkeys[6].target_false = real_monkeys[0]
real_monkeys[7].target_true = real_monkeys[2]
real_monkeys[7].target_false = real_monkeys[1]
real_monkeys[0].worry_change = types.MethodType(worry_change_multiply, real_monkeys[0])
real_monkeys[2].worry_change = types.MethodType(worry_change_squared, real_monkeys[2])
real_monkeys[7].worry_change = types.MethodType(worry_change_multiply, real_monkeys[7])

# Which set to use
monkeys = real_monkeys

for i in range(1, 21):
	for monkey in monkeys:
		monkey.run()

monkeys.sort(key=lambda x: x.inspected, reverse=True)
monkey_business = monkeys[0].inspected * monkeys[1].inspected
print(monkey_business)
