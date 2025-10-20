# Sorting a List Permanently with the sort() Method

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

cars.sort(reverse=True)
print(cars)

# Sorting a List Temporarily with the sorted() Function

cars = ['bmw', 'audi', 'toyota', 'subaru']

print(f"Here is the original list: {cars}")

print(f"\nHere is the sorted list: {sorted(cars)}")

print(f"Here is the original list again: {cars}")

# Printing a List in Reverse Order

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(f"Original list: {cars}")

cars.reverse()
print(f"Reversed list: {cars}")

# Finding the Length of a List

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars))

# Avoiding Index Errors When Working with Lists

# causes 'list index out of range' error
# motorcycles = ['honda', 'yamaha', 'suzuki']
# print(motorcycles[3])

