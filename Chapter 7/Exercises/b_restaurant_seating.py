# 7-2. Restaurant Seating: Write a program that asks the user how many people
# are in their dinner group. If the answer is more than eight, print a message say-
# ing they’ll have to wait for a table. Otherwise, report that their table is ready.

amount_of_people = input("How many people do you have in your dinner group? Enter a number: ")

amount_of_people = int(amount_of_people)

if amount_of_people > 8:
    print("I'm sorry you will have to wait till a table large enough becomes available.")
else:
    print("Great! Your table is ready. Please come this way.")


