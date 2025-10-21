# Copying a List

my_foods = ["pizza", "falafel", "carrot cake"]
friend_foods = my_foods[:]

# This doesn't work
# friend_foods = my_foods

my_foods.append("cannoli")
friend_foods.append("ice cream")

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

print("\n")

# Defining a Tuple. You cannot alter a tuple.

dimensions = (200, 50)

# ERROR: 'tuple' object does not support item assignment
# dimensions[0] = 250

print(dimensions[0])
print(dimensions[1])

print("\n")

# Looping Through All Values in a Tuple
# Writing Over a Tuple
dimensions = (400, 150)

for dimension in dimensions:
    print(dimension)

