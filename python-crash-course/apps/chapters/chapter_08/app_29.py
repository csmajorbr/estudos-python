def show_messages(messages):
    for message in messages:
        print(message)

def send_messages(messages, sent_messages):
    for message in messages:
        print(message)
        sent_messages.append(message)


messages = [
    'Jesus é o caminho',
    'Jesus é a verdade',
    'Jesus é a vida'
    ]

sent_messages = []

print("\nshow_message:")
show_messages(messages)

print("\nsend_messages:")
send_messages(messages, sent_messages)

print(f"\nLista messages: {messages}")
print(f"\nLista sent_messages {sent_messages}")
