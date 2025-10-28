# 9-3. Users: Make a class called User. Create two attributes called first_name
# and last_name, and then create several other attributes that are typically stored
# in a user profile. Make a method called describe_user() that prints a summary
# of the user’s information. Make another method called greet_user() that prints
# a personalized greeting to the user.
# Create several instances representing different users, and call both meth-
# ods for each user.

class User:

    def __init__(self, first_name, last_name, user_id, user_age):
        self.first_name = first_name
        self.last_name = last_name
        self.user_id = user_id
        self.user_age = user_age

    def describe_user(self):
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"User Age: {self.user_age}")
        print(f"User ID: {self.user_id}")

    def greet_user(self):
        print(f"Hello {self.first_name}, How are you today?")


print("---- User 1 ----")
user1 = User("Jack", "Boii", 1, 24)

user1.describe_user()
user1.greet_user()

print("\n---- User 2 ----")
user2 = User("Jason", "Trickster", 2, 19)

user2.describe_user()
user2.greet_user()

print("\n---- User 3 ----")
user3 = User("Emilia", "white", 3, 32)

user3.describe_user()
user3.greet_user()

