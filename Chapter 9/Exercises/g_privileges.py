# 9-8. Privileges: Write a separate Privileges class. 
# 
# The class should have one attribute, privileges, that stores a list of strings as described in Exercise 9-7.
# 
# Move the show_privileges() method to this class. 
# 
# Make a Privileges instance as an attribute in the Admin class. 
# 
# Create a new instance of Admin and use your method to show its privileges.

from b_users import User

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

print("\n\n\n\n\n\n\n\n\n\n")

admin = Admin("Jack", "brack", 7, 23)

admin.privileges.show_privileges()