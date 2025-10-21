# 5-1. Conditional Tests: Write a series of conditional tests. Print a statement
# describing each test and your prediction for the results of each test. Your code
# should look something like this:
# car = 'subaru'
# print("Is car == 'subaru'? I predict True.")
# print(car == 'subaru')
# print("\nIs car == 'audi'? I predict False.")
# print(car == 'audi')
# • Look closely at your results, and make sure you understand why each line
# evaluates to True or False.
# • Create at least 10 tests. Have at least 5 tests evaluate to True and another
# 5 tests evaluate to False.

nums = [1, 2, 3, 5, 4, 6, 7, 8, 9, 10]

print(nums[0] == 1)      # true
print(nums[1] == 2)      # true
print(nums[2] > nums[0]) # true
print(nums[3] == 4)      # false
print(nums[4] < nums[3]) # true
print(nums[5] != nums[2])# true
print(nums[6] > nums[7]) # false
print(nums[7] != 8)      # false
print(nums[8] == 7)      # false
print(nums[9] >= 11)     # false