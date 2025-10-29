# Inheritance

# 1. The __init__() Method for a Child Class

# 1. Parent class/Super class
class Car:
    """A simple attempt to represent a car."""
    
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles
    
    def fill_gas_tank(self):
        """Simulate filling up a gas tank."""
        print("\nFilling up a gas tank")

# ===========================================================
# ===========================================================
# ===========================================================

# 4. Instances as Attributes

class Battery:
    """A simple attempt to model a battery for an electic car."""

    def __init__(self, brand, battery_size=40):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size
        self.brand = brand
    
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")
    
    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225
        
        print(f"This car can go about {range} miles on a full charge.")

# ===========================================================
# ===========================================================
# ===========================================================

# 1. Child class/Subclass
class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        
        
        self.battery_size = 20 # 2. Defining Attributes and Methods for the Child Class

        self.battery = Battery("k1") # 4. Instances as Attributes
    
    # 2. Defining Attributes and Methods for the Child Class
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")
    
    def fill_gas_tank(self): # 3. Overriding Methods from the Parent Class
        """Electric cars don't have gas tanks."""
        print("This car doesn't have a gas tank!")

# Summary:
# The ElectricCar class is a subclass of Car that models features specific to electric vehicles. It:
# Inherits attributes and methods from the Car class using super().
# Adds new attributes such as battery_size and a battery object (an instance of the Battery class).
# Includes a describe_battery() method to display the battery’s capacity.
# Overrides the fill_gas_tank() method from Car to indicate that electric cars don’t use gas tanks.


# 1.
my_leaf = ElectricCar("nissan", "leaf", 2024)
print(my_leaf.get_descriptive_name())

print("\n")

# --------------------------------

# 2. Defining Attributes and Methods for the Child Class

my_leaf.describe_battery()

print("\n")

# --------------------------------

# 3. Overriding Methods from the Parent Class

my_leaf.fill_gas_tank()

print("\n")

# --------------------------------

# 4. Instances as Attributes

my_leaf.battery.describe_battery()
my_leaf.battery.get_range()

print("\n")

# --------------------------------

