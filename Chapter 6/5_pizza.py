# A List in a Dictionary

#Example 1
# Store the information about a pizza being ordered.
pizza = {
    "crust": "thick",
    "toppings": ["mushrooms", "extra cheese"]
}

# Summarize the order.
print(f"You ordered a {pizza["crust"]}-crust pizza with the following toppings:")

for topping in pizza["toppings"]:
    print(f"\t{topping}")

print("\n")

#Example 2
favorite_languages = {
    'jen': ['python', 'rust'],
    'sarah': ['c'],
    'edward': ['rust', 'go'],
    'phil': ['python', 'haskell'],
}

for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")


print("\n")

