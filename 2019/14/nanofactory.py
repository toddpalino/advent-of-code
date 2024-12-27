from collections import defaultdict

tests = [
	{
		'input': ("10 ORE => 10 A\n"
		          "1 ORE => 1 B\n"
		          "7 A, 1 B => 1 C\n"
		          "7 A, 1 C => 1 D\n"
		          "7 A, 1 D => 1 E\n"
		          "7 A, 1 E => 1 FUEL"),
		'ore': 31,
		'fuel': None
	},
	{
		'input': ("9 ORE => 2 A\n"
		          "8 ORE => 3 B\n"
		          "7 ORE => 5 C\n"
		          "3 A, 4 B => 1 AB\n"
		          "5 B, 7 C => 1 BC\n"
		          "4 C, 1 A => 1 CA\n"
		          "2 AB, 3 BC, 4 CA => 1 FUEL"),
		'ore': 165,
		'fuel': None
	},
	{
		'input': ("157 ORE => 5 NZVS\n"
		          "165 ORE => 6 DCFZ\n"
		          "44 XJWVT, 5 KHKGT, 1 QDVJ, 29 NZVS, 9 GPVTF, 48 HKGWZ => 1 FUEL\n"
		          "12 HKGWZ, 1 GPVTF, 8 PSHF => 9 QDVJ\n"
		          "179 ORE => 7 PSHF\n"
		          "177 ORE => 5 HKGWZ\n"
		          "7 DCFZ, 7 PSHF => 2 XJWVT\n"
		          "165 ORE => 2 GPVTF\n"
		          "3 DCFZ, 7 NZVS, 5 HKGWZ, 10 PSHF => 8 KHKGT"),
		'ore': 13312,
		'fuel': 82892753
	},
	{
		'input': ("2 VPVL, 7 FWMGM, 2 CXFTF, 11 MNCFX => 1 STKFG\n"
		          "17 NVRVD, 3 JNWZP => 8 VPVL\n"
		          "53 STKFG, 6 MNCFX, 46 VJHF, 81 HVMC, 68 CXFTF, 25 GNMV => 1 FUEL\n"
		          "22 VJHF, 37 MNCFX => 5 FWMGM\n"
		          "139 ORE => 4 NVRVD\n"
		          "144 ORE => 7 JNWZP\n"
		          "5 MNCFX, 7 RFSQX, 2 FWMGM, 2 VPVL, 19 CXFTF => 3 HVMC\n"
		          "5 VJHF, 7 MNCFX, 9 VPVL, 37 CXFTF => 6 GNMV\n"
		          "145 ORE => 6 MNCFX\n"
		          "1 NVRVD => 8 CXFTF\n"
		          "1 VJHF, 6 MNCFX => 4 RFSQX\n"
		          "176 ORE => 6 VJHF"),
		'ore': 180697,
		'fuel': 5586022
	},
	{
		'input': ("171 ORE => 8 CNZTR\n"
		          "7 ZLQW, 3 BMBT, 9 XCVML, 26 XMNCP, 1 WPTQ, 2 MZWV, 1 RJRHP => 4 PLWSL\n"
		          "114 ORE => 4 BHXH\n"
		          "14 VRPVC => 6 BMBT\n"
		          "6 BHXH, 18 KTJDG, 12 WPTQ, 7 PLWSL, 31 FHTLT, 37 ZDVW => 1 FUEL\n"
		          "6 WPTQ, 2 BMBT, 8 ZLQW, 18 KTJDG, 1 XMNCP, 6 MZWV, 1 RJRHP => 6 FHTLT\n"
		          "15 XDBXC, 2 LTCX, 1 VRPVC => 6 ZLQW\n"
		          "13 WPTQ, 10 LTCX, 3 RJRHP, 14 XMNCP, 2 MZWV, 1 ZLQW => 1 ZDVW\n"
		          "5 BMBT => 4 WPTQ\n"
		          "189 ORE => 9 KTJDG\n"
		          "1 MZWV, 17 XDBXC, 3 XCVML => 2 XMNCP\n"
		          "12 VRPVC, 27 CNZTR => 2 XDBXC\n"
		          "15 KTJDG, 12 BHXH => 5 XCVML\n"
		          "3 BHXH, 2 VRPVC => 7 MZWV\n"
		          "121 ORE => 7 VRPVC\n"
		          "7 XCVML => 6 RJRHP\n"
		          "5 BHXH, 4 VRPVC => 5 LTCX"),
		'ore': 2210736,
		'fuel': 460664
	}
]

def process_reaction_list(data):
	reactions = {}
	for line in data.splitlines():
		parts = line.split(' => ')
		output = parts[1].split(' ')
		r = {'quantity': int(output[0]), 'reagents': []}
		reagents = parts[0].split(', ')
		for reagent in reagents:
			parts = reagent.split(' ')
			r['reagents'].append((int(parts[0]), parts[1]))
		reactions[output[1]] = r
	return reactions

def get_ore_required(qty, chem, reactions, stock=None):
	if stock is None:
		stock = defaultdict(int)
	ore = 0

	needed = defaultdict(int)
	needed[chem] = qty
	while needed:
		new_needed = defaultdict(int)
		for chemical, quantity in needed.items():
			need_to_produce = quantity
			if stock[chemical] > quantity:
				stock[chemical] -= quantity
				continue
			else:
				quantity -= stock[chemical]
				stock[chemical] = 0

			reaction = reactions[chemical]
			multiplier = quantity // reaction['quantity'] + (1 if quantity % reaction['quantity'] != 0 else 0)
			stock[chemical] += (multiplier * reaction['quantity']) - quantity
			for reagent_quantity, reagent in reaction['reagents']:
				if reagent == 'ORE':
					ore += reagent_quantity * multiplier
				else:
					new_needed[reagent] += reagent_quantity * multiplier
		needed = new_needed
	return ore, stock

def produce_fuel(ore, reactions):
	# get_ore_required is efficient for any input number of fuel, which means we can binary search for
	# an answer. Start between 0 and the amount of ore we've been given (which would be 1 ore per fuel)
	min_fuel = 0
	max_fuel = ore

	while max_fuel > min_fuel:
		if max_fuel == min_fuel + 1:
			# The correct answer is either our current min or max
			ore_used, _ = get_ore_required(max_fuel, 'FUEL', reactions)
			return min_fuel if ore_used > ore else max_fuel

		target_fuel = min_fuel + (max_fuel - min_fuel) // 2
		ore_used, _ = get_ore_required(target_fuel, 'FUEL', reactions)
		if ore_used > ore:
			max_fuel = target_fuel - 1
		elif ore_used < ore:
			min_fuel = target_fuel
		else:
			# This would be a miracle
			return target_fuel

	return max_fuel
