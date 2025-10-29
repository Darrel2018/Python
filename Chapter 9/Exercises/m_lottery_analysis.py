# 9-15. Lottery Analysis: You can use a loop to see how hard it might be to win
# the kind of lottery you just modeled. Make a list or tuple called my_ticket. Write
# a loop that keeps pulling numbers until your ticket wins. Print a message report-
# ing how many times the loop had to run to give you a winning ticket.

from random import randint

lottery_nums = ["e", 0, 1, 2, "b", 3, 4, "a", 5, 6, "c", 7, 8, "d", 9]
my_ticket = "0b09"
guess_ticket = ""
attempts = 0

def get_lotto_nums():
    lotto_nums = ""
    
    for i in range(0, 4):
        lotto_nums += str(lottery_nums[randint(0, len(lottery_nums)-1)])
    
    return lotto_nums

while guess_ticket != my_ticket:
    guess_ticket = get_lotto_nums()
    attempts += 1
    print(guess_ticket)

print(f"Correctly guessed lotto ticket: {my_ticket} after {attempts} attempts.")

