# 6-1. Person: Use a dictionary to store information about a person you know.
# Store their first name, last name, age, and the city in which they live. You
# should have keys such as first_name, last_name, age, and city. Print each piece
# of information stored in your dictionary.

person = {
    "first_name": "jack",
    "last_name": "jackinton",
    "age": 24,
    "city": "new york"
}

for key, value in person.items():
    print(f"{key}: {value}")