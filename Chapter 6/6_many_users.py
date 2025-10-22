# A Dictionary in a Dictionary

# Summary:

# This code defines a dictionary of users, each with a first name, 
# last name, and location. It loops through the users and prints their 
# username, full name (title-cased), and location (also title-cased)

users = {
    "aeinstein": {
        "first": "albert",
        "last": "einstein",
        "location": "princeton",
    },
    "jackinton": {
        "first": "jack",
        "last": "jackinton",
        "location": "paris",
    },
}

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info["first"]} {user_info["last"]}"
    location = user_info["location"]

    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")


print("\n")


