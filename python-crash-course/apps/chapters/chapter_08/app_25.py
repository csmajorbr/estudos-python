def roupas(camisetas):
    for camiseta in camisetas:
        message = f"Eu comprei {camiseta.title()}."
        print(message)

marcas = ['alpha', 'armybr', 'crown']

roupas(marcas)