# 7-6. Three Exits: Write different versions of either Exercise 7-4 or 7-5 that do
# each of the following at least once:
# • Use a conditional test in the while statement to stop the loop.
# • Use an active variable to control how long the loop runs.
# • Use a break statement to exit the loop when the user enters a 'quit' value.


# Conditional Test

# print("\nWelcome to the movie theater! (Type 'quit' to exit)\n")

# user_age = ""

# while user_age.lower() != "quit":
#     user_age = input("Please enter your age(Enter a number): ")

#     if user_age.lower() == "quit":
#         continue

#     user_age = int(user_age)

#     if user_age < 3:
#         print("Your ticket is free!")
#     elif user_age >= 3 and user_age <= 12:
#         print("Your ticket costs $10")
#     elif user_age > 12:
#         print("Your ticket costs $15")
    
#     user_age = ""

# --------------------------------------

# Active Variable

# print("\nWelcome to the movie theater! (Type 'quit' to exit)\n")

# active = True

# while active:
#     user_age = input("Please enter your age(Enter a number): ")

#     if user_age.lower() == "quit":
#         active = False
#         continue

#     user_age = int(user_age)

#     if user_age < 3:
#         print("Your ticket is free!")
#     elif user_age >= 3 and user_age <= 12:
#         print("Your ticket costs $10")
#     elif user_age > 12:
#         print("Your ticket costs $15")

# --------------------------------------

# Break Statement

print("\nWelcome to the movie theater! (Type 'quit' to exit)\n")

while True:
    user_age = input("Please enter your age(Enter a number): ")

    if user_age.lower() == "quit":
        break

    user_age = int(user_age)

    if user_age < 3:
        print("Your ticket is free!")
    elif user_age >= 3 and user_age <= 12:
        print("Your ticket costs $10")
    elif user_age > 12:
        print("Your ticket costs $15")