def compras(alimentos):
    for alimento in alimentos:
        message = f"Eu comprei {alimento.title()}."
        print(message)

carnes = ['frango', 'patinho', 'picanha']

compras(carnes)
