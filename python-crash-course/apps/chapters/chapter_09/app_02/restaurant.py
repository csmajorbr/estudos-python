class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Restaurant name: {self.restaurant_name}")
        print(f"Cuisine type: {self.cuisine_type.title()}")

    def open_restaurant(self):
        print(f"The {self.restaurant_name} restaurant is open!")


restaurant = Restaurant('Baratie', 'seafood')

print(f"Restaurant name: {restaurant.restaurant_name}")
print(f"Cuisine type: {restaurant.cuisine_type.title()}")

print()
restaurant.describe_restaurant()
restaurant.open_restaurant()

print()
new_restaurant_0 = Restaurant('A Casa do Porco', 'brazilian')
new_restaurant_0.describe_restaurant()

print()
new_restaurant_1 = Restaurant('Maido', 'nikkei')
new_restaurant_1.describe_restaurant()

print()
new_restaurant_2 = Restaurant('Figlmüller', 'austrian')
new_restaurant_2.describe_restaurant()
