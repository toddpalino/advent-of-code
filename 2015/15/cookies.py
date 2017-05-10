#!/usr/bin/python

import operator
import itertools

ingredients = []

# Sugar: capacity 3, durability 0, flavor 0, texture -3, calories 2
# Sprinkles: capacity -3, durability 3, flavor 0, texture 0, calories 9
# Candy: capacity -1, durability 0, flavor 4, texture 0, calories 1
# Chocolate: capacity 0, durability 0, flavor -2, texture 2, calories 8

class Ingredient:
    def __init__(self, name, capacity, durability, flavor, texture, calories):
        self.name = name
        self.capacity = capacity
        self.durability = durability
        self.flavor = flavor
        self.texture = texture
        self.calories = calories

def print_recipe(recipe, score, kcal):
    print "{0} - score={1} calories={2}".format(', '.join(["{0}={1}".format(ingredient.name, recipe[i]) for i, ingredient in enumerate(ingredients)]), score, kcal)

quantity = int(raw_input("Teaspoons: "))
calorie_target = int(raw_input("Calories: "))
with open('ingredients') as f:
    for line in f:
        parts = line.strip().split(' ')
        ingredients.append(Ingredient(parts[0][:-1], int(parts[2][:-1]), int(parts[4][:-1]), int(parts[6][:-1]), int(parts[8][:-1]), int(parts[10])))

recipes = {}
calories = {}
for quantities in itertools.product(range(0, quantity+1), repeat=len(ingredients)):
    if sum(quantities) == quantity:
        recipes[quantities] = 0

print "RECIPES: {0}".format(len(recipes))
for recipe in recipes.keys():
    capacity = max(0, sum([ingredient.capacity * recipe[i] for i, ingredient in enumerate(ingredients)], 0))
    durability = max(0, sum([ingredient.durability * recipe[i] for i, ingredient in enumerate(ingredients)], 0))
    flavor = max(0, sum([ingredient.flavor * recipe[i] for i, ingredient in enumerate(ingredients)], 0))
    texture = max(0, sum([ingredient.texture * recipe[i] for i, ingredient in enumerate(ingredients)], 0))
    kcal = max(0, sum([ingredient.calories * recipe[i] for i, ingredient in enumerate(ingredients)], 0))
    score = capacity * durability * flavor * texture
    if score == 0:
        del recipes[recipe]
    else:
        recipes[recipe] = score
        calories[recipe] = kcal

recipes = sorted(recipes.items(), key=operator.itemgetter(1), reverse=True)
print_recipe(recipes[0][0], recipes[0][1], calories[recipes[0][0]])
print_recipe(recipes[-1][0], recipes[-1][1], calories[recipes[-1][0]])

for recipe in recipes:
    if calories[recipe[0]] == calorie_target:
        print_recipe(recipe[0], recipe[1], calories[recipe[0]])
