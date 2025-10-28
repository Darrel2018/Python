# Working with Classes and Instances
# The Car Class

# Summary:
# Purpose: To represent a car and manage its mileage.
# Attributes:
# make, model, year: Describe the car.
# odometer_reading: Tracks mileage, starting at 0.
# Methods:
# get_descriptive_name(): Returns a formatted string with the car’s year, make, and model.
# read_odometer(): Prints the car’s current mileage.
# update_odometer(mileage): Updates the odometer, preventing rollback to a smaller value.
# increment_odometer(miles): Adds a specified number of miles to the odometer.
# In short, the class provides a basic framework for representing and managing a car’s descriptive details and mileage safely.

class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 # Setting a Default Value for an Attribute

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")
    
    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles
        


my_new_car = Car('audi', 'a4', 2024)

print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

print("\n")

# -----------------------------------------------


# Modifying an Attribute’s Value Directly

my_new_car.odometer_reading = 23
my_new_car.read_odometer()

print("\n")

# -----------------------------------------------

# Modifying an Attribute’s Value Through a Method

my_new_car.update_odometer(30)
my_new_car.read_odometer()

print("\n")

# -----------------------------------------------

# Incrementing an Attribute’s Value Through a Method

my_used_car = Car('subaru', 'outback', 2019)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23_500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()