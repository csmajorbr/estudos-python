# Exercise 6.7, p.194
people = []

person_0 = {
    'fname': 'mateus',
    'lname': 'silva',
    'location': 'santos',
    }

person_1 = {
    'fname': 'maria',
    'lname': 'santana',
    'location': 'porto',
    }

person_2 = {
    'fname': 'pedro',
    'lname': 'piper',
    'location': 'new orleans',
    }

people.append(person_0)
people.append(person_1)
people.append(person_2)

for person in people:
    print(f"\nFull Name: {person['fname'].title()} {person['lname'].title()}")
    print(f"Location: {person['location'].title()}")
