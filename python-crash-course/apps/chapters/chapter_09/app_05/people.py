class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"Restaurant name: {self.restaurant_name}")
        print(f"Cuisine type: {self.cuisine_type.title()}")

    def open_restaurant(self):
        print(f"The {self.restaurant_name} restaurant is open!")

    def set_number_served(self, total):
        self.number_served = total

    def increment_number_served(self, increment):
        self.number_served += increment


restaurant = Restaurant('Bom Prato', 'brazilian')
print(f"Clientes atendidos: {restaurant.number_served}")

restaurant.number_served = 100
print(f"Clientes atendidos: {restaurant.number_served}")

restaurant.set_number_served(500)
print(f"Clientes atendidos: {restaurant.number_served}")

restaurant.increment_number_served(10_000)
print(f"Clientes atendidos: {restaurant.number_served}")
