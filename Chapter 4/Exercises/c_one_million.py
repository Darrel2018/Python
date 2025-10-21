# 4-4. One Million: Make a list of the numbers from one to one million, and then
# use a for loop to print the numbers. (If the output is taking too long, stop it by
# pressing CTRL-C or by closing the output window.)

big_list = [num for num in range(1, 1_000_001)]

for num in big_list:
    print(num)