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

class Admin(User):
    
    def __init__(self, first_name, last_name, user_id, user_age):
        super().__init__(first_name, last_name, user_id, user_age)
        
        self.privileges = Privileges(first_name, ["can add post", "can delete post", "can ban user"])
    
        

class Privileges:
    
    def __init__(self, username, privileges=[]):
        self.username = username
        self.privileges = privileges
    
    def show_privileges(self):
        print(f"User: {self.username} has the following privileges:")
        for privilege in self.privileges:
            print(f"\t{privilege}")