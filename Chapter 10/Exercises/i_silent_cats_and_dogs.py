# 10-9. Silent Cats and Dogs: Modify your except block in Exercise 10-7 to fail
# silently if either file is missing.

from pathlib import Path

paths = ["text_files/cats.txt", "text_files/dogs.txt"]

for path in paths:
    path = Path(path)
    try:
        contents = path.read_text()
    except FileNotFoundError:
        continue

    for line in  contents.splitlines():
        print(line)