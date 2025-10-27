# Modifying a List in a Function

# Example 1 with no functions

unprinted_designs = ["phone case", "robot pendant", "dodecahedron"]
completed_models = []

while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing model: {current_design}")
    completed_models.append(current_design)


print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)

print("\n")

# Example 2 with functions

# Summary
# This program simulates the process of "printing" 3D models.
# It defines two functions:
# print_models(unprinted_designs, completed_models):
# Removes each design from the unprinted_designs list, prints a message saying it’s being printed, and adds it to the completed_models list.
# show_completed_models(completed_models):
# Displays all models that have been printed.
# The program first prints three initial designs ('phone case', 'robot pendant', 'dodecahedron') and shows them as completed.
# Then it prints three new designs ('X', 'Y', 'Z') and shows the updated list of all completed models.

# In short:
# It simulates moving items from a “to-do” list to a “done” list, printing updates along the way.

def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until none are left.
    144 Chapter 8
    Move each design to completed_models after printing.
    """
    
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Show all the models that were printed."""
    
    print("\nThe following models have been printed:")
    
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

new_designs = ["X", "Y", "Z"]

print_models(new_designs, completed_models)
show_completed_models(completed_models)

print("\n")

# --------------------------------

# Preventing a Function from Modifying a List

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []
copy_of_list = unprinted_designs[:]

print_models(copy_of_list, completed_models)
show_completed_models(completed_models)
print(f"\nOriginal List: {unprinted_designs}")
print(f"\nCopy of Original List: {copy_of_list}")

# --------------------------------