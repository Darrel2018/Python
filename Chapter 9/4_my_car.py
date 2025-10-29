# Importing Classes

# Importing a Single Class
from car_module import Car

# Importing a Single Class
my_new_car = Car("audi", "a4", 2024)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

print("\n")