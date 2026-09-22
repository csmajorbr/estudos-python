prompt = "\nInforme quais ingredientes você quer adicionar a pizza:"
prompt += "\n(Digite 'sair' para encerrar o programa)\nIngredientes: "

ingredientes = ""

while True:    
    ingredientes = input(prompt)

    if ingredientes == 'sair':
        break
    else:                
        print(f"{ingredientes} está sendo adicionado a pizza.")
