# 4-5. Summing a Million: Make a list of the numbers from one to one million, and
# then use min() and max() to make sure your list actually starts at one and ends
# at one million. Also, use the sum() function to see how quickly Python can add
# a million numbers.

big_list = [num for num in range(1, 1_000_001)]

print(f"min: {min(big_list)}")
print(f"max: {max(big_list)}")
print(f"sum: {sum(big_list)}")