# Storing Multiple Classes in a Module
from car_module import ElectricCar

# Storing Multiple Classes in a Module

my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()
my_leaf.battery.get_range()

print("\n")