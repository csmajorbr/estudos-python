animal_0 = {'animal': 'avestruz', 'dono': 'arlindo'}
animal_1 = {'animal': 'raposa', 'dono': 'luan'}
animal_2 = {'animal': 'elefante', 'dono': 'misha'}

pets = [animal_0, animal_1, animal_2]

for animal in pets:
    print(f"\nAnimal: {animal['animal'].title()}")
    print(f"Dono: {animal['dono'].title()}")
