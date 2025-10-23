# 7-5. Movie Tickets: A movie theater charges different ticket prices depending on
# a person’s age. If a person is under the age of 3, the ticket is free; if they are
# between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is
# $15. Write a loop in which you ask users their age, and then tell them the cost
# of their movie ticket.

print("\nWelcome to the movie theater! (Type 'quit' to exit)\n")
while True:
    user_age = input("Please enter your age(Enter a number): ")

    if user_age.lower() == "quit":
        break

    user_age = int(user_age)

    if user_age < 3:
        print("Your ticket is free!")
    elif user_age >= 3 and user_age <= 12:
        print("Your ticket costs $10")
    elif user_age > 12:
        print("Your ticket costs $15")