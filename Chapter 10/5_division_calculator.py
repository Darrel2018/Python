# Exceptions

# Handling the ZeroDivisionError Exception

# causes ZeroDivisionError Exception
# print(5/0)

# -----------------------------------------

# Using try-except Blocks

# try:
#     print(5/0)
# except ZeroDivisionError:
#     print("You can't divide by zero!")

# -----------------------------------------

# Using Exceptions to Prevent Crashes

# Example 1 no try except block.
# print("Give me two numbers, and I'll divide them.")
# print("Enter 'q' to quit.")

# while True:
#     first_number = input("\nFirst number: ")
#     if first_number == 'q':
#         break

#     second_number = input("Second number: ")
#     if second_number == 'q':
#         break

#     answer = int(first_number) / int(second_number)
#     print(answer)

# Example 2 with try except block
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break

    second_number = input("Second number: ")
    if second_number == 'q':
        break

    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else: # The else Block. if no error then do the else block
        print(answer)
    
