# 6-7. People: Start with the program you wrote for Exercise 6-1 (page 98). Make
# two new dictionaries representing different people, and store all three dictionar-
# ies in a list called people. Loop through your list of people. As you loop through
# the list, print everything you know about each person.

person1 = {
    "first_name": "jack",
    "last_name": "jackinton",
    "age": 24,
    "city": "new york"
}

person2 = {
    "first_name": "ema",
    "last_name": "rivers",
    "age": 19,
    "city": "paris"
}

person3 = {
    "first_name": "mary",
    "last_name": "miller",
    "age": 26,
    "city": "rome"
}

people = [person1, person2, person3]

for person in people:
    print("\n")
    for key, value in person.items():
        print(f"{key}: {value}")