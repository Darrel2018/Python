# 9-14. Lottery: Make a list or tuple containing a series of 10 numbers and 5 letters.
# Randomly select 4 numbers or letters from the list and print a message saying that
# any ticket matching these 4 numbers or letters wins a prize.

from random import randint

lottery_nums = ["e", 0, 1, 2, "b", 3, 4, "a", 5, 6, "c", 7, 8, "d", 9]
winning_nums = ""

for i in range(0, 4):
    winning_nums += str(lottery_nums[randint(0, len(lottery_nums)-1)])


print(f"any ticket matching these 4 numbers or letters wins a prize: {winning_nums}")