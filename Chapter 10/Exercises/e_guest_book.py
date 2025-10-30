# 10-5. Guest Book: Write a while loop that prompts users for their name. Collect
# all the names that are entered, and then write these names to a file called
# guest_book.txt. Make sure each entry appears on a new line in the file.

from pathlib import Path

names = []

print("type 'q' to stop")
while True:
    username = input("Please enter your name: ")

    if username == "q":
        break
    
    names.append(username)


path = Path("guest_book.txt")

all_names_string = ""
for name in names:
    all_names_string += name + "\n"

path.write_text(all_names_string)