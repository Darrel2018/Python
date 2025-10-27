# 8-4. Large Shirts: Modify the make_shirt() function so that shirts are large
# by default with a message that reads I love Python. Make a large shirt and a
# medium shirt with the default message, and a shirt of any size with a different
# message.

def make_shirt(size="large", text="I love Python."):
    print(f"Making shirt of size {size} and has the text '{text}' on it.")


make_shirt()

make_shirt(size="medium")

make_shirt(text="Whatcha looking at?")