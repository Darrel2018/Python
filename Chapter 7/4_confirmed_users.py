# Moving Items from One List to Another

# unconfirmed_users = ["alice", "brian", "candace"]
# confirmed_users = []

# while unconfirmed_users:
#     current_user = unconfirmed_users.pop()

#     print(f"Verifying user: {current_user.title()}")
#     confirmed_users.append(current_user)

# print("\nThe following users have been confirmed:")
# for confirmed_user in confirmed_users:
#     print(confirmed_user.title())

#----------------------------

# Removing All Instances of Specific Values from a List

# pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
# print(pets)

# while "cat" in pets:
#     pets.remove("cat")

# print(pets)

#----------------------------

# Filling a Dictionary with User Input

responses = {}

polling_active = True

while polling_active:
    name = input("\nWhat is your name? ").title()
    response = input("Which mountain would you like to climb someday? ")

    responses[name] = response

    repeat = input("Would you like to let another person respond? (yes/no) ")

    if repeat == "no":
        polling_active = False
    

print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")

# Summary

# This Python program conducts a simple poll asking users which mountain they would like to climb.

# It repeatedly prompts users for their name and desired mountain.

# Each response is stored in a dictionary called responses, where the name is the key and the mountain is the value.

# The loop continues until a user answers "no" to the question about letting another person respond.

# After polling ends, the program prints a summary of all responses.