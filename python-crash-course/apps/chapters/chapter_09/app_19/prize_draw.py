from random import sample

valores = (1000, 2500, 3541, 1548, 9875, 3548, 6541, 1552, 3587, 9542, 'j', 'k', 'l', 'n', 'm')

sorteados = sample(valores, 4)

print(f"Qualquer bilhete que corresponda a esses 4 números ou letras ganha um prêmio:")

for count, valor in enumerate(sorteados, start=1):
    print(f"{count}º Valor: {valor}")
