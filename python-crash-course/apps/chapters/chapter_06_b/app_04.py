favorite_places = {
    'mateus': ['são paulo', 'rio de janeiro'],
    'marcos': ['paris', 'londres'],
    'lucas': ['roma', 'liboa'],
    }

for pessoa in favorite_places.keys():
    print(f"\n{pessoa.title()} gosta muito das cidades de")
    for lugar in favorite_places[pessoa]:
        print(f"\t-> {lugar.title()}")