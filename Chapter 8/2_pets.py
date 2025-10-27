# Positional Arguments

def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet("hamster", "harry")
describe_pet("dog", "willie")

# Order Matters in Positional Arguments
describe_pet("harry", "hamster")

print("\n")

# ----------------------------------------------

# Keyword Arguments

describe_pet(animal_type="cat", pet_name="mitsy")
describe_pet(pet_name="boii", animal_type="green alien")

print("\n")

# ----------------------------------------------

# Default Values

def describe_pet(pet_name, animal_type="dog"):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(pet_name="willie")
describe_pet("wonker")
describe_pet(pet_name='harry', animal_type='hamster')

print("\n")

# ----------------------------------------------

# Equivalent Function Calls

# A dog named Willie.
describe_pet('willie')
describe_pet(pet_name='willie')

# A hamster named Harry.
describe_pet('harry', 'hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')

print("\n")

# ----------------------------------------------

# Avoiding Argument Errors

def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

# ERROR: TypeError: describe_pet() missing 2 required positional arguments: 'animal_type' and 'pet_name
# describe_pet()


# ----------------------------------------------


