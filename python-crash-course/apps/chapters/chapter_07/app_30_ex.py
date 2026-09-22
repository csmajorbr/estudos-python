ferias = {}

while True:
    nome = input("\nDigite o seu nome: ")
    lugar = input("Qual lugar do mundo sonha em conhecer: ")

    if nome not in ferias:
        ferias[nome] = []

    ferias[nome].append(lugar)

    quer_continuar = input("Mais alguém ira responder('s' ou 'n')? ")

    if quer_continuar == 'n':
        break

print("\n---Resultado da Pesquisa---")

for nome, lugares in ferias.items():
    print(f"\nNome: {nome.title()}")
    print(f"Lugares dos sonhos: {', '.join(lugares)}")
