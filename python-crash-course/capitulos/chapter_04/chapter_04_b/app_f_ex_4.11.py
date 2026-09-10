my_pizzas = ['calabresa', 'atum', 'mussarela', 'italiana']
friend_pizzas = my_pizzas[:]

my_pizzas.append('marguerita')
friend_pizzas.append('quatro queijos')

print("My favorite pizzas are:")
for pizza in my_pizzas:
    print(pizza)

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)
