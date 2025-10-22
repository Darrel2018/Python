# 6-6. Polling: Use the code in favorite_languages.py (page 96).
# • Make a list of people who should take the favorite languages poll. Include
# some names that are already in the dictionary and some that are not.
# • Loop through the list of people who should take the poll. If they have
# already taken the poll, print a message thanking them for responding.
# If they have not yet taken the poll, print a message inviting them to take
# the poll.

favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "rust",
    "phil": "python"
}

needed_polls = ["jen", "jack", "sarah", "edward", "bob", "rob", "phil"]

for person in needed_polls:
    if person in favorite_languages:
        print(f"{person.title()} thank you for responding to the poll.")
    else:
        print(f"{person.title()}! You are invited to take this poll!")