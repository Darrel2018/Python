# Importing an Entire Module

# # import whole module
# import pizza_module

# # when using the whole module you would call functions like this.
# pizza_module.make_pizza(14, "pepperoni",
#                         "mushrooms",
#                         "extra cheese")


# -------------------------------------

# Importing Specific Functions

# # importing a function from a module
# from pizza_module import make_pizza

# # when you only import a function from a module you can just call the function.
# make_pizza(14, "pepperoni",
#                 "mushrooms",
#                 "extra cheese")

# -------------------------------------

# Using as to Give a Function an Alias

# from pizza_module import make_pizza as mp

# mp(14, "pepperoni",
#         "mushrooms",
#         "extra cheese")

# -------------------------------------

# Using as to Give a Module an Alias

# import pizza_module as p

# p.make_pizza(16, 'pepperoni')
# p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# -------------------------------------

# Importing All Functions in a Module

# from pizza_module import *

# make_pizza(16, 'pepperoni')
# make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# -------------------------------------
