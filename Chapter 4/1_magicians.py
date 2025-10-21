# Looping Through an Entire List

magicians = ["alice", "david", "carolina"]

for magician in magicians:
    print(magician)


# Doing More Work Within a for Loop

magicians = ["alice", "david", "carolina"]

for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.")

# Doing Something After a for Loop

magicians = ["alice", "david", "carolina"]

for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.")

print("Thank you, everyone. That was a great magic show!")


# Forgetting to Indent
# causes ERROR: indentation

# magicians = ['alice', 'david', 'carolina']

# for magician in magicians:
# print(magician)


# Forgetting to Indent Additional Lines

magicians = ['alice', 'david', 'carolina']

for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
print(f"I can't wait to see your next trick, {magician.title()}.\n")


# Indenting Unnecessarily
# ERROR: unexpected indent

# message = "Hello Python world!"
#     print(message)


# Indenting Unnecessarily After the Loop

magicians = ['alice', 'david', 'carolina']

for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

    print("Thank you everyone, that was a great magic show!")


# Forgetting the Colon
# SyntaxError: expected ':'

# magicians = ['alice', 'david', 'carolina']

# for magician in magicians
#     print(magician)


