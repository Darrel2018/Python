# 8-10. Sending Messages: Start with a copy of your program from Exercise 8-9.
# Write a function called send_messages() that prints each text message and
# moves each message to a new list called sent_messages as it’s printed. After
# calling the function, print both of your lists to make sure the messages were
# moved correctly.

def send_messages(unsent_messages, sent_messages):

    while unsent_messages:
        cur_message = unsent_messages.pop()
        print(cur_message)
        sent_messages.append(cur_message)


unsent_messages = ["Hello, how are you?",
                   "Look out from above!",
                   "It's not me. It's you."]

sent_messages = []

send_messages(unsent_messages, sent_messages)

print(f"unsent_messages: {unsent_messages}")
print(f"sent_messages: {sent_messages}")