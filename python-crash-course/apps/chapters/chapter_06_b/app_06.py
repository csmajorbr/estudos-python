cities = {
    'são paulo': {
        'country': 'Brazil',
        'population': 12_000_000,
        'fact': 'É a maior cidade do Brazil',
    },

    'paris': {
        'country': 'França',
        'population': 15_000_000,
        'fact': 'É a capital da França',
    },

    'lisboa': {
        'country': 'Portugal',
        'population': 8_000_000,
        'fact': 'É a capital de Portugal'
    }

    }

for cidade, fatos in cities.items():
    print(f"\nCidade: {cidade.title()}")
    print(f"Informações sobre a cidade de {cidade.title()}:")
    print(f"1. Country: {fatos['country']}")
    print(f"2. Population: {fatos['population']}")
    print(f"3. Fact: {fatos['fact']}")