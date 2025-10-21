# Making Numerical Lists

# Using the range() Function

for value in range(1, 6):
    print(value)

print("\n")

# Using range() to Make a List of Numbers

numbers = list(range(1, 6))
print(numbers)

print("\n")

even_numbers = list(range(2, 11, 2))
print(even_numbers)

print("\n")

squares = []

for value in range(1, 11):
    squares.append(value ** 2)

print(squares)

print("\n")

# Simple Statistics with a List of Numbers

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

print(f"min(digits): {min(digits)}")
print(f"max(digits): {max(digits)}")
print(f"sum(digits): {sum(digits)}")

print("\n")

# List Comprehensions

squares = [value**2 for value in range(1, 11)]
print(squares)