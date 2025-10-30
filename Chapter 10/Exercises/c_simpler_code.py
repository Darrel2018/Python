# 10-3. Simpler Code: The program file_reader.py in this section uses a temporary
# variable, lines, to show how splitlines() works. You can skip the temporary
# variable and loop directly over the list that splitlines() returns:
# for line in contents.splitlines():
# Remove the temporary variable from each of the programs in this section,
# to make them more concise.

from pathlib import Path

print("\n---Example 1---")
for line in Path("learning_python.txt").read_text().splitlines():
    print(line)

print("\n---Example 2---")
pi_string = ""
for line in Path("learning_python.txt").read_text().splitlines():
    pi_string += line.lstrip()

print(pi_string)