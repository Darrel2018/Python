# 10-14. Verify User: The final listing for remember_me.py assumes either that the
# user has already entered their username or that the program is running for the
# first time. We should modify it in case the current user is not the person who last
# used the program.
# Before printing a welcome back message in greet_user(), ask the user if
# this is the correct username. If it’s not, call get_new_username() to get the correct
# username.

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

def check_same_user(username, path):
    """Ask the user if their username is correct."""

    while True:
        same_user = input(f"Is your username {username}? (yes/no): ")

        if same_user.lower() == "yes" or same_user.lower() == "y":
            print(f"Welcome back, {username}!")
        elif same_user.lower() == "no" or same_user.lower() == "n":
            username = get_new_username(path)
            print(f"We'll remember you when you come back, {username}!")
        else:
            continue

        break


def greet_user(): # now greet_user is shorter and simpler to follow
    """Greet the user by name."""

    path = Path('text_files/username.json')
    username = get_stored_username(path)
    
    if username:
        check_same_user(username, path)
    else:
        username = get_new_username(path)
        print(f"We'll remember you when you come back, {username}!")

greet_user()