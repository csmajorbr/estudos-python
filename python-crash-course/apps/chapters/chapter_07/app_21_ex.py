prompt = "\nEscreva uma palavra e eu vou repetir ela para você"
prompt += "\nDigite 'quit' para sair"

is_running = True

while is_running:
    palavra = input(prompt)

    if palavra == "quit":
        is_running = False
    else:
        print(palavra)