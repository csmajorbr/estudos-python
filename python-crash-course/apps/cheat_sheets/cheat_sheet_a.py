# ===================================================
# Capítulo 2 — Variáveis e Tipos de Dados Simples
# ===================================================

# --- Variáveis ---
message = "Hello Python world!"
print(message)
# Nomes de variáveis podem conter letras, números e underscore (_),
# mas não podem começar com número.
# Não podem conter espaços (use _ no lugar).
# Evite usar palavras reservadas do Python (print, class, list, etc).

# --- Strings ---
name = "ada lovelace"

name.title()      # "Ada Lovelace" — primeira letra de cada palavra maiúscula
name.upper()       # "ADA LOVELACE" — tudo maiúsculo
name.lower()       # "ada lovelace" — tudo minúsculo

# Combinando strings (concatenação)
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
print(f"Hello, {full_name.title()}!")   # f-strings

# Espaços em branco
"\t"    # tab
"\n"    # nova linha

# Removendo espaços
favorite_language = " python "
favorite_language.rstrip()   # remove espaços à direita
favorite_language.lstrip()   # remove espaços à esquerda
favorite_language.strip()    # remove espaços dos dois lados

# --- Números ---
2 + 3    # soma
3 - 2    # subtração
2 * 3    # multiplicação
3 / 2    # divisão
3 ** 2   # potenciação (3²)

# Ordem de operações: segue a matemática tradicional
# (parênteses, expoentes, multiplicação/divisão, soma/subtração)

# Convertendo números para string (evitar erro em concatenação)
age = 23
message = "Happy " + str(age) + "rd Birthday!"

# --- Comentários ---
# Isso é um comentário
print("Hello Python people!")

# --- O Zen do Python ---
import this


# ===================================================
# Capítulo 3 — Introdução às Listas
# ===================================================

# --- Criando e acessando listas ---
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0])        # 'trek' — índice começa em 0
print(bicycles[0].title())
print(bicycles[-1])       # último item da lista

# --- Modificando elementos ---
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles[0] = 'ducati'

# --- Adicionando elementos ---
motorcycles.append('ducati')          # adiciona no final
motorcycles.insert(0, 'ducati')       # insere em posição específica

# --- Removendo elementos ---
del motorcycles[0]                     # remove pelo índice (não recupera o valor)

popped_motorcycle = motorcycles.pop()  # remove o último item e retorna seu valor
popped_motorcycle = motorcycles.pop(0) # remove item de índice específico

motorcycles.remove('ducati')           # remove pelo valor

# --- Organizando uma lista ---

# Permanentemente
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()                # ordem alfabética (A-Z)
cars.sort(reverse=True)    # ordem alfabética reversa (Z-A)

# Temporariamente (sem alterar a original)
print(sorted(cars))
print(sorted(cars, reverse=True))

# Invertendo a ordem original
cars.reverse()   # inverte a ordem atual da lista (permanente)

# --- Tamanho da lista ---
len(cars)   # número de itens na lista

# --- Evitando erros de índice ---
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles[3])   # IndexError, pois só existem índices 0, 1, 2