usernames = ['lucca', 'marcos', 'leonardo', 'pedro', 'gustavo', 'admin']

for username in usernames:
    if username == 'admin':
        print(f"Olá {username.title()}, gostaria de ver um relatório de status?")
    else:
        print(f"Bem-vindo {username.title()}!")
