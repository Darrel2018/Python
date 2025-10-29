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