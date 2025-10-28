# 9-4. Number Served: Start with your program from Exercise 9-1 (page 162). 
# Add an attribute called number_served with a default value of 0. 
# Create an instance called restaurant from this class.  
# Print the number of customers the restaurant has served, and then change this value and print it again. 
# Add a method called set_number_served() that lets you set the number of customers that have been served. 
# Call this method with a new number and print the value again. 
# Add a method called increment_number_served() that lets you increment the number of customers who’ve been served. 
# Call this method with any number you like that could represent how many customers were served in, say, a day of business. 

class Restaurant:
    """A Class that models different Restaurant types"""

    # Contructor
    def __init__(self, restaurant_name, cuisine_type, number_served=0):
        """Initialize the Restaurant instance"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served
    
    def describe_restaurant(self):
        """Describes the restaurant to the user"""
        print(f"This Restaurant is called {self.restaurant_name}.")
        print(f"This Restaurant serves the cuisine {self.cuisine_type}.")
    
    def open_restaurant(self):
        """Opens the restaurant to the customers"""
        print(f"{self.restaurant_name} is now open! It is now serving {self.cuisine_type} to it's customers.")
    
    def set_number_served(self, number_served):
        self.number_served = number_served
    
    def increment_number_served(self, amount):
        self.number_served += amount



restaurant = Restaurant("Bob's Burgers", "Burgers")

print("\n")

print("---- Example 1 ----")

print(f"Number of customers {restaurant.restaurant_name} has served: {restaurant.number_served}")
restaurant.number_served = 5
print(f"Number of customers {restaurant.restaurant_name} has served: {restaurant.number_served}")

print("\n---- Example 2 ----")

restaurant.set_number_served(10)
print(f"Number of customers {restaurant.restaurant_name} has served: {restaurant.number_served}")

print("\n---- Example 3 ----")
restaurant.increment_number_served(5)
print(f"Number of customers {restaurant.restaurant_name} has served: {restaurant.number_served}")
