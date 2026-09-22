languages = ['python', 'java', 'c', 'c++',
             'cobol', 'elixir', 'lua', 'rust', 'kotlin']

print("The first three elements of the list are:")

for language in languages[:3]:
    print(language.title())

print("\nThe three elements that are in the middle of the list are:")

for language in languages[3:6]:
    print(language.title())

print("\nThe last three elements on the list are:")

for language in languages[6:]:
    print(language.title())
