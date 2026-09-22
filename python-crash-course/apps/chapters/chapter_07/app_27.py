pedidos = {}

is_running= True

while is_running:
    nome = input("Digite o seu nome: ")
    pedido = input("Qual o seu pedido de oração? ")

    pedidos[nome] = pedido

    outros_pedidos = input("Mais alguém tem pedidos ('s' ou 'n')? ")
    if outros_pedidos == 'n':
        is_running = False    

print("\n---Pedidos de Oração---")

for nome, pedido in pedidos.items():
    print(f"\nNome: {nome.title()}:")
    print(f"Pedido: {pedido}")