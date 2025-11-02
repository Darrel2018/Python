# Working with Multiple Files

from pathlib import Path

def count_words(filename):
    """Count the approximate number of words in a file."""

    try:
        contents = filename.read_text(encoding='utf-8')
    except FileNotFoundError:
        # print(f"Sorry, the file {filename} does not exist.")
        pass # Failing Silently
    else:
        # Count the approximate number of words in the file:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")


# Example 1 # just one file
# path = Path('alice.txt')
# count_words(path)

# Example 2 # multiple files
filenames = ["alice.txt", "text_files/little_women.txt", "text_files/moby_dick.txt", "text_1.txt"]

for filename in filenames:
    path = Path(filename)
    count_words(path)

# ----------------------------------------------

