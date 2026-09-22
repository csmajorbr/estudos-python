class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Restaurant name: {self.restaurant_name}")
        print(f"Cuisine type: {self.cuisine_type.title()}")

    def open_restaurant(self):
        print(f"The {self.restaurant_name} restaurant is open!")


class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []

    def show_flavors(self):
        for count, flavor in enumerate(self.flavors, start=1):
            print(f"Flavor {count}: {flavor.title()}")
            count += 1

ice_cream_shop1 = IceCreamStand('Kibon', 'ice creams')
ice_cream_shop1.flavors = ['vanilla', 'chocolate', 'strawberry', 'grape']

ice_cream_shop1.show_flavors()