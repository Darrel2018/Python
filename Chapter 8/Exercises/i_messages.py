# 8-9. Messages: Make a list containing a series of short text messages. Pass the
# list to a function called show_messages(), which prints each text message.

def show_messages(messages):
    for msg in messages:
        print(msg)

messages = ["Hello, how are you?",
            "Look out from above!",
            "It's not me. It's you."]

show_messages(messages)