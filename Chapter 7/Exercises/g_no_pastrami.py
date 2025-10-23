# No Pastrami: Using the list sandwich_orders from Exercise 7-8, make sure
# the sandwich 'pastrami' appears in the list at least three times. Add code
# near the beginning of your program to print a message saying the deli has
# run out of pastrami, and then use a while loop to remove all occurrences of
# 'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up
# in finished_sandwiches.

sandwich_orders = ["tuna", "pastrami", "chicken mayo", "cheese salid", "pastrami", "egg", "banana", "pastrami"]
finished_sandwiches = []

print("Welcome to the sandwich deli! I will make your orders please wait a moment. Note: Dear customer, we have run out of Pastrami and will not be serving them today.\n")

# remove pastrami from sandwich_orders
while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)
    print(f"Your {current_sandwich} sandwich was made and is ready to be eaten!")
    
    finished_sandwiches.append(current_sandwich)


print("\nAll the sandwiches has been made!")