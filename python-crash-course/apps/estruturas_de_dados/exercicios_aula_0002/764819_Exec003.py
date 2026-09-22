notas = []

for i in range(1, 6):
    nota = float(input(f"Digite a nota do {i}º aluno: "))
    notas.append(nota)

media = sum(notas) / len(notas)

print(f"\nA média da turma é: {media:.2f}\n")

for index, nota in enumerate(notas):
    print(f"Índice {index} -> Nota: {nota:.2f}")
