# 9-5. Login Attempts: Add an attribute called login_attempts to your User class from Exercise 9-3 (page 162). 
# Write a method called increment_login_attempts() that increments the value of login_attempts by 1. 
# Write another method called reset_login_attempts() that resets the value of login_attempts to 0. 
# Make an instance of the User class and call increment_login_attempts() several times. 
# Print the value of login_attempts to make sure it was incremented properly, and then call reset_login_attempts(). 
# Print login_attempts again to make sure it was reset to 0.


class User:

    def __init__(self, first_name, last_name, user_id, user_age, login_attempts):
        self.first_name = first_name
        self.last_name = last_name
        self.user_id = user_id
        self.user_age = user_age
        self.login_attempts = login_attempts

    def describe_user(self):
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"User Age: {self.user_age}")
        print(f"User ID: {self.user_id}")

    def greet_user(self):
        print(f"Hello {self.first_name}, How are you today?")
    
    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


user_1 = User("Bob", "Bobby", 1, 20, 0)

user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()

print(f"Number of logins by user '{user_1.first_name}': {user_1.login_attempts}")

user_1.reset_login_attempts()

print(f"Number of logins by user '{user_1.first_name}': {user_1.login_attempts}")