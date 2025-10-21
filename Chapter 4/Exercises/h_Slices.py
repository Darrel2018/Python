# 4-10. Slices: Using one of the programs you wrote in this chapter, add several
# lines to the end of the program that do the following:
# • Print the message The first three items in the list are:. Then use a slice to
# print the first three items from that program’s list.
# • Print the message Three items from the middle of the list are:. Then use a
# slice to print three items from the middle of the list.
# • Print the message The last three items in the list are:. Then use a slice to
# print the last three items in the list.

my_foods = ['pizza', 'falafel', 'carrot cake', 'chicken burger', "bacon burger"]

print(f"The first three items in the list are: {my_foods[:3]}")
print(f"Three items from the middle of the list are: {my_foods[1:4]}")
print(f"The last three items in the list are: {my_foods[2:4]}")

