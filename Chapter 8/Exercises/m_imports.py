# 8-16. Imports: Using a program you wrote that has one function in it, store that
# function in a separate file. Import the function into your main program file, and
# call the function using each of these approaches:
# import module_name
# from module_name import function_name
# from module_name import function_name as fn
# import module_name as mn
# from module_name import *

# Example 1
# import b_favorite_book

# b_favorite_book.favorite_book("A Game of Thrones")

# -----------------------------------

# Example 2
# from b_favorite_book import favorite_book

# favorite_book("The Hobbit")

# -----------------------------------

# Example 3
# import b_favorite_book as favbook

# favbook.favorite_book("Dracula")

# -----------------------------------

# Example 4
from b_favorite_book import *

favorite_book("The Lord of the Rings")