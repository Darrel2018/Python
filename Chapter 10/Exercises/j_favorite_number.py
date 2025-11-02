# 10-11. Favorite Number: Write a program that prompts for the user’s favorite
# number. Use json.dumps() to store this number in a file. Write a separate pro-
# gram that reads in this value and prints the message “I know your favorite
# number! It’s _____.”
# AND ------------------------------------------------------------------------------------
# 10-12. Favorite Number Remembered: Combine the two programs you wrote in
# Exercise 10-11 into one file. If the number is already stored, report the favorite
# number to the user. If not, prompt for the user’s favorite number and store it in a
# file. Run the program twice to see that it works.

from pathlib import Path
import json

path = Path("text_files/favorite_number.txt")

if path.exists() == False:
    fav_num = input("What is your favorite number?: ")
    fav_num = json.dumps(fav_num)
    path.write_text(fav_num)
else:
    fav_num = path.read_text()
    fav_num = json.loads(fav_num)
    print(f"I know your favorite number! It's {fav_num}.")