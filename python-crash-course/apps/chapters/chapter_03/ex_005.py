convidados = ['Paulo', 'Pedro', 'João', 'Davi']

print(f"Gostaria de jantar comigo {convidados[0]}?")
print(f"Gostaria de jantar comigo {convidados[1]}?")
print(f"Gostaria de jantar comigo {convidados[2]}?")
print(f"Gostaria de jantar comigo {convidados[3]}?")

print(f"\n{convidados[3]} não irá ao jantar.")

convidados[3] = 'Salomão'
print("\nConvidados: ", convidados)

print(f"\nGostaria de jantar comigo {convidados[3]}?")

convidados.append('Mateus')
convidados.append('Marcos')
convidados.append('Lucas')

print(f"\nEncontrei uma mesa maior {convidados[4]}, {convidados[5]} e {convidados[6]}.\n")

convidados.insert(0, 'Jesus')
convidados.insert(4, 'Judas')
convidados.append('Maria')

for convidado in convidados:
    print(f"Gostaria de jantar comigo {convidado}?")

print("\nInfelizmente posso convidar somente duas pessoas para o jantar.")

while len(convidados) > 2:
    ultimo_removido = convidados.pop()
    print(f"\nLamento por não poder convidá-lo para o jantar {ultimo_removido}")

print("\nConvidados restantes:", convidados, "\n")

print("Estão convidados: ")
for index, convidado in enumerate(convidados):
    print(f"{convidado}")

del convidados[-1]
del convidados[-1]

print("\nConvidados restantes:", convidados)
