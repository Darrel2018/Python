# Using json.dumps() and json.loads() # 2

from pathlib import Path
import json

path = Path("numbers.json")
contents = path.read_text()
numbers = json.loads(contents)

print(numbers)
print(type(numbers))