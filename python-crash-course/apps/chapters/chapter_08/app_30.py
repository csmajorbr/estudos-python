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

print("Mensagens originais:")
show_messages(messages)

print("\nEnviando cópia das mensagens:")
send_messages(messages[:], sent_messages)

print(f"\nmessages:       {messages}")
print(f"sent_messages:  {sent_messages}")