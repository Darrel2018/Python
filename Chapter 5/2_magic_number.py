# Numerical Comparisons

age = 18
print(age == 18)

answer = 17

if answer != 42:
    print("That is not the correct answer. Please try again!")


age = 19
print(age < 21)
print(age <= 21)
print(age > 21)
print(age >= 21)

print("\n")

# Using and to Check Multiple Conditions

age_0 = 22
age_1 = 18

admission = age_0 >= 21 and age_1 >= 21

print(f"Are both patrons allowed to purchase?: {admission}")

age_1 = 22

admission = age_0 >= 21 and age_1 >= 21

print(f"Are both patrons allowed to purchase?: {admission}")

print("\n")

# Using or to Check Multiple Conditions

age_0 = 22
age_1 = 18

admission = age_0 >= 21 or age_1 >= 21

print(f"Can they enter the movie theatre?: {admission}")

age_0 = 18

admission = age_0 >= 21 or age_1 >= 21

print(f"Can they enter the movie theatre?: {admission}")

print("\n")


# Checking Whether a Value Is in a List

requested_toppings = ['mushrooms', 'onions', 'pineapple']

print(f"Add mushrooms?: {'mushrooms' in requested_toppings}")

print(f"Add pepperoni?: {'pepperoni' in requested_toppings}")

print("\n")

# Checking Whether a Value Is Not in a List

banned_users = ['andrew', 'carolina', 'david']
user = "marie"

if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")
else:
    print(f"{user.title()}, you can not post a response. You are banned.")

print("\n")

# Boolean Expressions

game_active = True
can_edit = False

