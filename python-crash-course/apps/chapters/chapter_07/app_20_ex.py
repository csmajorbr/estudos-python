prompt_0 = "\nQual produto você deseja?"
prompt_0 += "\nDigite 'quit' para sair)\nResposta: "

while True:
    compra = input(prompt_0)

    if (compra == "quit"):
        break
    else:
        print(f"{compra} foi adicionado ao carrinho!")