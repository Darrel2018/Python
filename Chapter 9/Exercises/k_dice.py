# 9-13. Dice: Make a class Die with one attribute called sides, which has a
# default value of 6. Write a method called roll_die() that prints a random num-
# ber between 1 and the number of sides the die has. Make a 6-sided die and
# roll it 10 times.

from random import randint

class Die:
    
    def __init__(self, sides=6):
        self.sides = sides
    
    def roll_die(self):
        return randint(1, self.sides)


dice = Die()

for index in range(0, 10):
    print(f"Rolling dice and the number is: {dice.roll_die()}")