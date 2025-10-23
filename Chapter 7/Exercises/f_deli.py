# 7-8. Deli: Make a list called sandwich_orders and fill it with the names of various
# sandwiches. Then make an empty list called finished_sandwiches. Loop through
# the list of sandwich orders and print a message for each order, such as I made
# your tuna sandwich. As each sandwich is made, move it to the list of finished
# sandwiches. After all the sandwiches have been made, print a message listing
# each sandwich that was made.

sandwich_orders = ["tuna", "chicken mayo", "cheese salid", "egg", "banana"]
finished_sandwiches = []

print("Welcome to the sandwich deli! I will make your orders please wait a moment.\n")

while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)
    print(f"Your {current_sandwich} sandwich was made and is ready to be eaten!")
    
    finished_sandwiches.append(current_sandwich)


print("\nAll the sandwiches has been made!")

