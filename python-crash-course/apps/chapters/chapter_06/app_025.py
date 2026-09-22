favorite_languages = {
    'mateus': 'python',
    'marcos': 'java',
    'lucas' : 'c',
    'paulo' : 'python',
}

people = ['mateus', 'marcos', 'judas', 'tito']

for person in people:
    if person in favorite_languages:
        print(f"Thank you for participating in our poll, {person.title()}.")
    else:
        print(f"Please, {person.title()}, participate in our poll.")