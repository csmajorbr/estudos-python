current_users = ['mateus', 'marcos', 'lucas', 'joão', 'paulo']
new_users = ['mateus', 'marcos', 'pedro', 'tito', 'judas']

current_users_lower = [user.lower() for user in current_users]


for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"{new_user} precisará inserir um novo nome de usuário!")
    else:
        print(f"O usuário {new_user} está diponível!")
