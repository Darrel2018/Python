# Modifying Elements in a List

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = "ducati"
print(motorcycles)

# Adding Elements to a List

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles.append("ducati")
print(motorcycles)

motorcycles = []
print(motorcycles)

motorcycles.append("honda")
motorcycles.append("yamaha")
motorcycles.append("suzuki")
print(motorcycles)

# Inserting Elements into a List

motorcycles = ['honda', 'yamaha', 'suzuki']

motorcycles.insert(0, "ducati")
print(motorcycles)

# Removing an Item Using the del Statement

motorcycles = ['honda', 'yamaha', 'suzuki']
del motorcycles[0]
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
del motorcycles[1]
print(motorcycles)

# Removing an Item Using the pop() Method

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print("popped_motorcycle: " + popped_motorcycle)

# Popping Items from Any Position in a List

motorcycles = ['honda', 'yamaha', 'suzuki']

first_owned = motorcycles.pop(1)
print(f"The first motorcycle I owned was a {first_owned.title()}.")

# Removing an Item by Value

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

motorcycles.remove("honda")
print(motorcycles)

too_expensive = "ducati"
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")
