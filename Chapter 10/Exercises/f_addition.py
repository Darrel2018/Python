# 10-6. Addition: One common problem when prompting for numerical input
# occurs when people provide text instead of numbers. When you try to convert
# the input to an int, you’ll get a ValueError. Write a program that prompts for
# two numbers. Add them together and print the result. Catch the ValueError if
# either input value is not a number, and print a friendly error message. Test your
# program by entering two numbers and then by entering some text instead of a
# number.

def get_num_from_user(first_or_second):
    while True:
        try:
            num = input(f"Enter {first_or_second} number: ")
            num = int(num)
        except ValueError:
            print(f"Please enter a number for the {first_or_second} value.")
            continue
        
        break

    return num



num1 = get_num_from_user("first")
num2 = get_num_from_user("second")

sum = num1 + num2

print(f"The result of {num1} + {num2} is {sum}.")