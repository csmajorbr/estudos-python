# Argumentos nomeados
def describe_pet(animal_type, pet_name):
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet(animal_type='dog', pet_name='sol')
describe_pet(pet_name='nix', animal_type='dog')