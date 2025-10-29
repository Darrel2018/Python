# 9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant. 
# 
# Write a class called IceCreamStand that inherits from the Restaurant class you wrote in
# Exercise 9-1 (page 162) or Exercise 9-4 (page 166). 
# 
# Either version of the class will work; just pick the one you like better. Add an attribute called flavors that
# stores a list of ice cream flavors. Write a method that displays these flavors.
# 
# Create an instance of IceCreamStand, and call this method.

from a_restaurant import Restaurant

class IceCreamStand(Restaurant):
    """An ice cream stand is a specific kind of restaurant."""
    
    def __init__(self, restaurant_name, cuisine_type, flavors = []):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors
    
    def show_flavors(self):
        for flavor in self.flavors:
            print(f"We have the flavor: {flavor.title()}")

print("\n\n\n\n\n\n\n\n\n\n")

ice_cream_flavors = ["strawberry", "vanilla", "chocolate", "bubblegum", "oreo"]

ice_cream = IceCreamStand("Bob's Ice Cream", "Ice Cream", ice_cream_flavors)

ice_cream.show_flavors()
