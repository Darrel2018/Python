# 4-13. Buffet: A buffet-style restaurant offers only five basic foods. Think of five
# simple foods, and store them in a tuple.
# • Use a for loop to print each food the restaurant offers.
# • Try to modify one of the items, and make sure that Python rejects the
# change.
# • The restaurant changes its menu, replacing two of the items with different
# foods. Add a line that rewrites the tuple, and then use a for loop to print
# each of the items on the revised menu.


buffet_food = ("chicken", "tuna sandwiches", "potato salid", "hot dogs", "pizza")

# task 1

for food in buffet_food:
    print(food)

# task 2
# causes error
# buffet_food[0] = "hamburger"

# task 3
buffet_food = ("chicken", "salid", "potato salid", "hot dogs", "hamburger")

for food in buffet_food:
    print(food)