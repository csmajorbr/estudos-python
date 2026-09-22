def describe_pet(pet_name, animal_type='dog'):
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(pet_name='nix')

describe_pet('willie')

describe_pet(pet_name='harry', animal_type='hamster')