prompt = "\nQuais recheios você quer na sua pizza?"
prompt += "\nDigite 'quit' para sair\nRecheios: "

recheio = ""

while recheio != "quit":
    recheio = input(prompt)

    if recheio != "quit":
        print(f"{recheio.title()} foi adicionado a sua pizza!")
