# 9-7. Admin: An administrator is a special kind of user. 
# 
# Write a class called Admin that inherits from the User class you wrote in Exercise 9-3 (page 162)
# or Exercise 9-5 (page 167). 
# 
# Add an attribute, privileges, that stores a list of strings like "can add post", "can delete post", "can ban user", and so on.
# 
# Write a method called show_privileges() that lists the administrator’s set of
# privileges. Create an instance of Admin, and call your method.

from b_users import User

class Admin(User):
    
    def __init__(self, first_name, last_name, user_id, user_age, privileges = []):
        super().__init__(first_name, last_name, user_id, user_age)
        
        self.privileges = privileges
    
    def show_privileges(self):
        print(f"User: {self.first_name} has the following privileges:")
        for privilege in self.privileges:
            print(f"\t{privilege}")
        

print("\n\n\n\n\n\n\n\n\n\n")

admin = Admin("Jack", "brack", 7, 23, ["can add post", "can delete post", "can ban user"])

admin.show_privileges()

