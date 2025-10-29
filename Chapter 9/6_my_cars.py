# Importing Multiple Classes from a Module

# from car_module import Car, ElectricCar

# my_mustang = Car('ford', 'mustang', 2024)
# print(my_mustang.get_descriptive_name())
# my_leaf = ElectricCar('nissan', 'leaf', 2024)
# print(my_leaf.get_descriptive_name())


# ----------------------------------------

# Importing an Entire Module

# import car_module

# my_mustang = car_module.Car('ford', 'mustang', 2024)
# print(my_mustang.get_descriptive_name())

# my_leaf = car_module.ElectricCar('nissan', 'leaf', 2024)
# print(my_leaf.get_descriptive_name())

# ----------------------------------------

# Importing All Classes from a Module

# from car_module import *

# my_mustang = Car('ford', 'mustang', 2024)
# print(my_mustang.get_descriptive_name())

# my_leaf = ElectricCar('nissan', 'leaf', 2024)
# print(my_leaf.get_descriptive_name())

# ---------------------------------------

# Importing a Module into a Module
from car_module import Car
from electric_car_module import ElectricCar

my_mustang = Car('ford', 'mustang', 2024)
print(my_mustang.get_descriptive_name())
my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())

# ---------------------------------------

# Using Aliases

# Example 1
# from electric_car_module import ElectricCar as EC
# my_leaf = EC('nissan', 'leaf', 2024)

# Example 2
# import electric_car_module as ec
# my_leaf = ec.ElectricCar('nissan', 'leaf', 2024)

