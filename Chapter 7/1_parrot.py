# How the input() Function Works

# message = input("Tell me something, and I will repeat it back to you: ")
# print(message)

#----------------------------

# Writing Clear Prompts

# Example 1
# name = input("Please enter your name: ")
# print(f"\nHello, {name}!")


# Example 2

# prompt = "If you share your name, we can personalize the messages you see."
# prompt += "\nWhat is your first name? "

# name = input(prompt)
# print(f"Hello, {name.title()}!")

#----------------------------

# Using int() to Accept Numerical Input

# Example 1
# age = input("How old are you? ") # returns string
# age = int(age) # convert to int
# print(type(age))

# Example 2
# height = input("How tall are you, in inches? ")
# height = int(height)

# if height >= 48:
#     print("\nYou're tall enough to ride!")
# else:
#     print("\nYou'll ab able to ride when you're a little older.")

#----------------------------