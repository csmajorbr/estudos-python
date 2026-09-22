# Exercise 7.5

prompt = "\nDigite a sua idade:"
prompt += "\n(Digite '0' para sair)\nIdade: "

while True:
    idade=int(input(prompt))

    if idade == 0:
        break
    elif idade < 0:
        print("Idade inválida, digite um valor maior que 0.")
        continue
    elif idade < 3:
        print("Ingresso gratuito!")
    elif idade <= 12:
        custo = 10
        print(f"Valor do ingresso: U${custo:.1f}.")
    else:
        custo = 15
        print(f"Valor do ingresso: U${custo:.1f}.")