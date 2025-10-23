# Introducing while Loops

# The while Loop in Action

# current_number = 1

# while current_number <= 5:
#     print(current_number)
#     current_number += 1

#----------------------------

# Letting the User Choose When to Quit

# Example 1
# prompt = "\nTell me something, and I will repeat it back to you:"
# prompt += "\nEnter 'quit' to end the program. "

# message = ""

# while message.lower() != "quit":
#     message = input(prompt)

#     if message.lower() != "quit":
#         print(f"\nMessage: {message}")



# Example 2
# prompt = "\nTell me something, and I will repeat it back to you:"
# prompt += "\nEnter 'quit' to end the program. "

# active = True
# while active:
#     message = input(prompt)

#     if message.lower() == "quit":
#         active = False 
#     else:
#         print(f"\nMessage: {message}")

#----------------------------

# Using break to Exit a Loop

# prompt = "\nPlease enter the name of a city you have visited:"
# prompt += "\n(Enter 'quit' when you are finished.) "

# while True:
#     city = input(prompt)

#     if city.lower() == "quit":
#         break
#     else:
#         print(f"I'd love to go to {city.title()}!")

#----------------------------

# Using continue in a Loop

current_number = 0

while current_number < 10:
    current_number += 1

    if current_number % 2 == 0: # if num is even continue
        continue

    print(current_number)

#----------------------------

