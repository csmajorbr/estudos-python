def city_country(city, country):
    return f"{city.title()}, {country.title()}"


city_0 = city_country('paris', 'frança')
city_1 = city_country('brooklin', 'estados unidos')
city_2 = city_country('são paulo', 'brasil')

print(f"{city_0}")
print(f"{city_1}")
print(f"{city_2}")
