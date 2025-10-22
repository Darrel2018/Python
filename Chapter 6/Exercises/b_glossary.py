# 6-3. Glossary: A Python dictionary can be used to model an actual dictionary.
# However, to avoid confusion, let’s call it a glossary.
# • Think of five programming words you’ve learned about in the previous
# chapters. Use these words as the keys in your glossary, and store their
# meanings as values.
# • Print each word and its meaning as neatly formatted output. You might
# print the word followed by a colon and then its meaning, or print the word
# on one line and then print its meaning indented on a second line. Use the
# newline character (\n) to insert a blank line between each word-meaning
# pair in your output.

# variable
# Function 
# Bug

glossary = {
    "variable": "A variable in a programming langauage is similar to the math variable like x and y. But in programming it acts like a storage container to hold information we can use later in the program. We can also use it like we do in math if we want to.",
    "function": "A function in a programming language is a set of code that can be called from anywhere in the program using the function's name.",
    "bug": "A bug is an issue or error in a programming language. This can be an issue that the compiler picks up or it can be a logical error in the program itself.",
}

for item, meaning in glossary.items():
    print(f"\n{item.title()}:")
    print(f"{meaning}")

