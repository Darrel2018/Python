# Saving and Reading User-Generated Data # 1

from pathlib import Path
import json

# Example 1
# username = input("What is your name? ")

# path = Path("username.json")
# contents = json.dumps(username)
# path.write_text(contents)

# print(f"We'll remember you when you come back, {username}!")

# Example 2

# path = Path("username.json")

# if path.exists():
#     contents = path.read_text()
#     username = json.loads(contents)
#     print(f"Welcome back, {username}")
# else:
#     username = input("What is your name? ")
#     contents = json.dumps(username)
#     path.write_text(contents)
#     print(f"We'll remember you when you come back, {username}!")

# -------------------------------------------------

# Refactoring

# Example 1
# from pathlib import Path
# import json

# def greet_user():
#     """Greet the user by name."""

#     path = Path('username.json')
#     if path.exists():
#         contents = path.read_text()
#         username = json.loads(contents)
#         print(f"Welcome back, {username}!")
#     else:
#         username = input("What is your name? ")
#         contents = json.dumps(username)
#         path.write_text(contents)
#         print(f"We'll remember you when you come back, {username}!")

# greet_user()

# Example 2

# from pathlib import Path
# import json

# def get_stored_username(path): # new funtion to simplifie things
#     """Get stored username if available."""
#     if path.exists():
#         contents = path.read_text()
#         username = json.loads(contents)
#         return username
#     else:
#         return None

# def greet_user():
#     """Greet the user by name."""

#     path = Path('username.json')
#     username = get_stored_username(path)
    
#     if username:
#         print(f"Welcome back, {username}!")
#     else:
#         username = input("What is your name? ")
#         contents = json.dumps(username)
#         path.write_text(contents)
#         print(f"We'll remember you when you come back, {username}!")

# greet_user()

# Example 3

from pathlib import Path
import json

def get_stored_username(path):
    """Get stored username if available."""
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
        return None

def get_new_username(path): # new funtion to simplify things
    """Prompt for a new username."""
    username = input("What is your name? ")
    contents = json.dumps(username)
    path.write_text(contents)
    return username

def greet_user(): # now greet_user is shorter and simpler to follow
    """Greet the user by name."""

    path = Path('username.json')
    username = get_stored_username(path)
    
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = get_new_username(path)
        print(f"We'll remember you when you come back, {username}!")

greet_user()

# Summary

# This Python program stores and recalls a user’s name using a JSON file.

# It checks whether a file named username.json already exists.

# If the file exists, it reads and loads the stored username, then greets the user with “Welcome back, [username]!”.

# If the file doesn’t exist, it asks the user to input their name, saves it to username.json, and then says “We’ll remember you when you come back, [username]!”.