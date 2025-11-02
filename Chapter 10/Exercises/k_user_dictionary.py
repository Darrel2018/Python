# 10-13. User Dictionary: The remember_me.py example only stores one piece of
# information, the username. Expand this example by asking for two more pieces
# of information about the user, then store all the information you collect in a
# dictionary. Write this dictionary to a file using json.dumps(), and read it back
# in using json.loads(). Print a summary showing exactly what your program
# remembers about the user.

from pathlib import Path
import json

def get_stored_userinformation(path):
    """Get stored user information if available."""
    if path.exists():
        contents = path.read_text()
        contents = json.loads(contents)
        return contents
    else:
        return None

def get_new_userinformation(path):
    """Prompt for new user data"""
    username = input("What is your name?: ")
    userage = input("What is your age?: ")
    userpass = input("What is your password?: ")

    user_dictionary = {"username": username,
                       "userage": userage,
                       "userpass": userpass}

    contents = json.dumps(user_dictionary)
    path.write_text(contents)
    return username

def greet_user():
    """Greet the user by name and give them their information"""

    path = Path('text_files/userdata.json')
    userdata = get_stored_userinformation(path)
    
    if userdata:
        print(f"Welcome back, {userdata["username"]}!")
        print(f"You are {userdata["userage"]} years old.")
        print(f"Your password is '{userdata["userpass"]}'")
    else:
        userdata = get_new_userinformation(path)
        print(f"We'll remember you when you come back, {userdata["username"]}!")

greet_user()