# Looping Through All Key-Value Pairs

#Example 1
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}

for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")

print("\n")

#Example 2

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

print("\n")

# Looping Through All the Keys in a Dictionary

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

# Example 1
for name in favorite_languages.keys():
    print(name.title())

print("\n")

# Example 2
friends = ["phil", "sarah"]

for name in favorite_languages.keys():
    print(f"Hi {name.title()}.")

    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")

print("\n")

# Example 3
if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")

print("\n")



# Looping Through a Dictionary’s Keys in a Particular Order

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

print("\n")




# Looping Through All Values in a Dictionary

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

# Example 1
print("The following langauages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

print("\n")

# Example 2 using set for unique values
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())

print("\n")

