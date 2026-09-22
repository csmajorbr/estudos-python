favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

for name in favorite_languages.keys():
    print(name.title())

# esse código geraria exatamente a mesma saída se você escrevesse:
print()
for name in favorite_languages:
    print(name.title())
