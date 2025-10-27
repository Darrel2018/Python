# 8-12. Sandwiches: Write a function that accepts a list of items a person wants
# on a sandwich. The function should have one parameter that collects as many
# items as the function call provides, and it should print a summary of the sand-
# wich that’s being ordered. Call the function three times, using a different num-
# ber of arguments each time.

def make_sandwiches(*sandwichs):
    for sandwich in sandwichs:
        print(f"You want the {sandwich} sandwich.")


make_sandwiches("ham")
make_sandwiches("chicken", "mayo", "lettus")
make_sandwiches("beef", "memory", "dream", "sandwich I had last time I went to my mom's house it was so good that I will always remeber it. It reminds me of a cool summer day. I bet you wish you had it didn't you? Well too bad! Thanks for reading.")