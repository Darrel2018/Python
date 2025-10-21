# IF STATEMENTS

# A Simple Example

cars = ["audi", "bmw", "subaru", "toyota"]

for car in cars:
    if car == "bmw":
        print(car.upper())
    else:
        print(car.title())

print("\n")

# Checking for Equality

car = "bmw"
print(car == "bmw")

car = "audi"
print(car == "bmw")

car = "Audi"
print(car == "audi")

car = "Audi"
print(car.lower() == "audi")

print("\n")

# Checking for Inequality

requested_topping = "mushrooms"

if requested_topping != "anchovies":
    print("Hold the anchovies!")

print("\n")

