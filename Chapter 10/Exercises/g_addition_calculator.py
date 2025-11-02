# 10-7. Addition Calculator: Wrap your code from Exercise 10-5 in a while loop
# so the user can continue entering numbers, even if they make a mistake and
# enter text instead of a number.

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