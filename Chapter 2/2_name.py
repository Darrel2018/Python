# Strings

name = "jack jacKINton"
print(name.title())

print(name.upper())
print(name.lower())

# Using Variables in Strings

first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"

print(full_name)

print(f"Hello, {full_name.title()}!")

# Adding Whitespace to Strings with Tabs or Newlines

print("Python")
print("\tPython")

print("Languages:\nPython\nC\nJavaScript")

print("Languages:\n\tPython\n\tC\n\tJavaScript")

# Stripping Whitespace

favorite_language = "python     "
print(favorite_language)
print(favorite_language.rstrip())

favorite_language = "                  python   "
print(favorite_language)
print(favorite_language.lstrip())

favorite_language = "                  python          "
print(favorite_language)
print(favorite_language.strip())

# Removing Prefixes

nostartch_url = "https://nostarch.com"
print(nostartch_url.removeprefix("https://"))

# Avoiding Syntax Errors with Strings

message = "One of Python's strengths is its diverse community."
print(message)

# message = 'One of Python's strengths is its diverse community.'
# print(message)
