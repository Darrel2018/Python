# What Is a List?

bicycles = ["trek", "cannondale", "redline", "specialized"]
print(bicycles)

# Accessing Elements in a List

print(f"bicycles[0] = {bicycles[0]}")

print(f"bicycles[0] = {bicycles[0].title()}")

# Index Positions Start at 0, Not 1

print(f"bicycles[1] = {bicycles[1]}")

print(f"bicycles[3] = {bicycles[3]}")

# Gets last element in the list
print(f"bicycles[-1] = {bicycles[-1]}")

print(f"bicycles[-2] = {bicycles[-2]}")

# Using Individual Values from a List

message = f"My first bicycle was a {bicycles[0].title()}."
print(message)