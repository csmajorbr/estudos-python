alunos = [10.0, 9.0, 8.0, 7.0, 6.0]
print(f"Antes da alteração: {alunos}")

alunos[0] = 5.0
print(f"\nDepois da alteração: {alunos}")

count = 0;
for i in range(0, 5):
    if alunos[i] >= 7.0:
        count += 1

print(f"\nQuantidade de alunos com nota maior ou igual a 7.0: {count}")
