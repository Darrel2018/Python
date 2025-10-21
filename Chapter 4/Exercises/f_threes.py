# 4-7. Threes: Make a list of the multiples of 3, from 3 to 30. Use a for loop to
# print the numbers in your list.

multiples_of_three = [num * 3 for num in range(1, 11)]

for num in multiples_of_three:
    print(num)