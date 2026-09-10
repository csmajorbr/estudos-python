# 6.4 p.186
glossary = {
    'linux': 'free, open-source operating system core',
    'windows': 'a graphical operating system developed by microsoft',
    'python': 'a high-level, general-purpose programming language',
    'sql': 'a standardized programming language',
}

glossary.update({
    'loop': 'a block of code that repeats until a condition is met',
    'variable': 'a name that stores a value',
    'function': 'a reusable block of code',
    'list': 'an ordered collection of items',
    'string': 'a sequence of characters'
})

for k, v in glossary.items():
    print(f"{k.title()}: {v}")