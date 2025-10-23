# 7-4. Pizza Toppings: Write a loop that prompts the user to enter a series of
# pizza toppings until they enter a 'quit' value. As they enter each topping, print
# a message saying you’ll add that topping to their pizza.

active = True

customer_toppings = []

print("\nWelcome to my pizza shop! What toppings do you want?\n")
while active:
    pizza_topping = input("Enter Topping(type 'quit' to stop): ")

    if pizza_topping.lower() == "quit":
        active = False
    else:
        customer_toppings.append(pizza_topping)


print("\nGreat I will add those to your pizza!\n")
for pizza_topping in customer_toppings:
    print(f"Adding {pizza_topping} to the pizza.")

print("\nAll done! Here's your pizza!\n")