numeros_favoritos = {
    'mateus': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'marcos': [11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    'lucas': [21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
    'paulo': [31, 32, 33, 34, 35, 36, 37, 38 ,39 ,40]
    }

for pessoa in numeros_favoritos.keys():
    print(f"\nNome: {pessoa.title()}\nNúmeros favoritos:", end=" ")
    for numeros in numeros_favoritos[pessoa]:
        print(f"{numeros}", end=" ") 
print("\n...")