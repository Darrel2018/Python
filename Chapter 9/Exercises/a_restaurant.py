# 9-1. Restaurant: Make a class called Restaurant. The __init__() method for
# Restaurant should store two attributes: a restaurant_name and a cuisine_type.
# Make a method called describe_restaurant() that prints these two pieces of
# information, and a method called open_restaurant() that prints a message indi-
# cating that the restaurant is open.
# Make an instance called restaurant from your class. Print the two attri-
# butes individually, and then call both methods

class Restaurant:
    """A Class that models different Restaurant types"""

    # Contructor
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize the Restaurant instance"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        """Describes the restaurant to the user"""
        print(f"This Restaurant is called {self.restaurant_name}.")
        print(f"This Restaurant serves the cuisine {self.cuisine_type}.")
    
    def open_restaurant(self):
        """Opens the restaurant to the customers"""
        print(f"{self.restaurant_name} is now open! It is now serving {self.cuisine_type} to it's customers.")


restaurant = Restaurant("My Dad's grill", "BBQ Meat")

print("\n---- Attributes ----")

print(f"Restaurant name: {restaurant.restaurant_name}")
print(f"Cuisine type: {restaurant.cuisine_type}")

print("\n---- Method Calls ----")

restaurant.describe_restaurant()
restaurant.open_restaurant()

print("\n")

#===============================================================
#===============================================================

# 9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three
# different instances from the class, and call describe_restaurant() for each
# instance.

restaurant_2 = Restaurant("Mikes Kitchen", "Italian")
restaurant_3 = Restaurant("Ocean Basket", "Fish")

print("9-2. Three Restaurants")

restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()